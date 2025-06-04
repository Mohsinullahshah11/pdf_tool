from datetime import datetime
import io
from pypdf import PdfReader, PdfWriter
import img2pdf as imgpdf 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



class pdfOperations:
    def __init__(self,path,fromPage = None, toPage = None,_pages = None):
        self.path = path
        self.fromPage = fromPage
        self.toPage = toPage
        self.pages = _pages
    
    def splitPDF(self):
        resultFilesPath = []
        pages = list(range(int(self.fromPage)-1,int(self.toPage)))

        reader = PdfReader(self.path)
        writer = PdfWriter()
        rest_writer = PdfWriter()
        for page in range(len(reader.pages)):
            if page in pages:
                writer.add_page(reader.pages[page])
            else:
                rest_writer.add_page(reader.pages[page])

        now = datetime.now()
        writerPath1 = f'{self.path}1{now}'
            
        # with open(writerPath1,'wb') as file:
        writer.write(writerPath1)
        resultFilesPath.append(writerPath1)


        writerPath2 = f'{self.path}2{now}'

        # with open(writerPath2,'wb') as file:
        rest_writer.write(writerPath2)
        resultFilesPath.append(writerPath2)

        return resultFilesPath

    def mergePDF(self):
        # resultFilePath = ''
        merger = PdfWriter()

        for pdf in self.path:
            merger.append(pdf)
        
        now = datetime.now()
        path = f'{self.path[0]}{now}'

        merger.write(path)
        merger.close()
        return path
    
    def convert_images_to_pdf(self):

        now = datetime.now()
        path = f'{self.path[0]}{now}'
        with open(path, "wb") as f:
            f.write(imgpdf.convert(self.path))
        
        return path
    

    def removePages(self,pages):

        reader = PdfReader(self.path)
        writer = PdfWriter()

        for page in range(len(reader.pages)):
            if str(page+1) not in pages:
                writer.add_page(reader.pages[int(page)])

        now = datetime.now()
        writerPath1 = f'{self.path}{now}'
            
        writer.write(writerPath1)

        return writerPath1


    def create_text_watermark(self, text):
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.setFont("Helvetica", 40)
            can.setFillAlpha(0.2) 
            can.translate(595 / 2, 842 / 2)
            can.rotate(45)
            can.drawCentredString(0, 0, text)
            can.save()
            packet.seek(0)

            return PdfReader(packet).pages[0]

    def addTextWatermark(self, watermark_text):
        reader = PdfReader(self.path)
        writer = PdfWriter()

        watermark_page = self.create_text_watermark(watermark_text)
        for page in reader.pages:
            page.merge_page(watermark_page,over=False)
            writer.add_page(page)
        now = datetime.now()
        output_path = f'{self.path}_{now}'

        with open(output_path, 'wb') as out_file:
            writer.write(out_file)

        return output_path


