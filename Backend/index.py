import io
import os
import zipfile
from utilites import Utilities
from pdfOperations import pdfOperations
from flask import Flask, jsonify, request,send_file
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  

# Sample route
@app.route('/')
def home():
    return "API Server is running!"

# Example GET API
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# Example POST API


@app.route('/api/split-pdf', methods=['POST'])
def post_data():
    try:
        fromPage = request.form.get('from')
        toPage = request.form.get('to')

        try:
            fromPage = int(fromPage)
            toPage = int(toPage)
        except (TypeError, ValueError):
            return jsonify({'error': 'Invalid page numbers'}), 400

        file = request.files.get('file')

        now = datetime.now()
        file.filename = f'{now}{file.filename}'

        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        UPLOAD_FOLDER = './uploads'
        file.save(os.path.join(UPLOAD_FOLDER, f'{file.filename}'))


        filePath = f'./uploads/{file.filename}'
        splitOperation = pdfOperations(filePath,fromPage,toPage)
    
        filesPath =  splitOperation.splitPDF()

        # Create in-memory ZIP
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            zip_file.write(filesPath[0], arcname='selected.pdf')
            zip_file.write(filesPath[1], arcname='remaining.pdf')

        zip_buffer.seek(0)
        filesPath.append(filePath)
        utlities = Utilities(filesPath)
        utlities.delete_files()

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            download_name='documents.zip',
            as_attachment=True
        )
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/api/merge-pdf', methods=['POST'])
def merge_pdf():
    try:

        files = request.files.getlist('files')

        now = datetime.now()
        filesPath = []
        for file in files:
            file.filename = f'{now}{file.filename}'

            UPLOAD_FOLDER = './uploads'
            file.save(os.path.join(UPLOAD_FOLDER, f'{file.filename}'))
            filePath = f'./uploads/{file.filename}'
            filesPath.append(filePath)
        
        splitOperation = pdfOperations(filesPath)
    
        filePath =  splitOperation.mergePDF()

        # Create in-memory ZIP
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            zip_file.write(filePath, arcname='merged_pdf.pdf')

        zip_buffer.seek(0)
        filesPath.append(filePath)
        utlities = Utilities(filesPath)
        utlities.delete_files()

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            download_name='documents.zip',
            as_attachment=True
        )
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/api/images-to-pdf', methods=['POST'])
def imageToPDF():
    try:

        files = request.files.getlist('files')

        now = datetime.now()
        filesPath = []
        for file in files:
            file.filename = f'{now}{file.filename}'

            UPLOAD_FOLDER = './uploads'
            file.save(os.path.join(UPLOAD_FOLDER, f'{file.filename}'))
            filePath = f'./uploads/{file.filename}'
            filesPath.append(filePath)
        
        splitOperation = pdfOperations(filesPath)
    
        filePath =  splitOperation.convert_images_to_pdf()

        # Create in-memory ZIP
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            zip_file.write(filePath, arcname='images_pdf.pdf')

        zip_buffer.seek(0)
        filesPath.append(filePath)
        utlities = Utilities(filesPath)
        utlities.delete_files()

        return send_file(
            zip_buffer,
            mimetype='application/zip',
            download_name='documents.zip',
            as_attachment=True
        )
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, port=5000)
