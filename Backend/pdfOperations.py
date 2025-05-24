from datetime import datetime
from pypdf import PdfReader, PdfWriter
import img2pdf as imgpdf #for images


class pdfOperations:
    def __init__(self,path,fromPage = None, toPage = None):
        self.path = path
        self.fromPage = fromPage
        self.toPage = toPage
    
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

