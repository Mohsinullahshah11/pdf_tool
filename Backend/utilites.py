from datetime import datetime
import os
import io

import zipfile
from pdfOperations import pdfOperations
from flask import jsonify

class Utilities():

    def __init__(self,path=None,formData = None):
        self.filesPath = path
        self.formData = formData
    def delete_files(self):
        for path in self.filesPath:
            try:
                if os.path.exists(path):
                    os.remove(path)
                    print(f"Deleted: {path}")
                else:
                    print(f"File not found: {path}")
            except Exception as e:
                print(f"Error deleting {path}: {e}")
    
    def handleSplitRequest(self):
        fromPage = self.formData.get('from')
        toPage = self.formData.get('to')

        try:
            fromPage = int(fromPage)
            toPage = int(toPage)
        except (TypeError, ValueError):
            return jsonify({'error': 'Invalid page numbers'}), 400

        file = self.formData.get('file')

        now = datetime.now()
        file.filename = f'{now}{file.filename}'

        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        UPLOAD_FOLDER = './uploads'
        file.save(os.path.join(UPLOAD_FOLDER, f'{file.filename}'))


        filePath = f'./uploads/{file.filename}'
        splitOperation = pdfOperations(filePath,fromPage,toPage)
    
        filessPath =  splitOperation.splitPDF()
        self.delete_files(path=[filePath])

        return filessPath