from datetime import datetime
import os
import io

import zipfile
from pdfOperations import pdfOperations
from flask import jsonify

class Utilities():

    def __init__(self,path=None):
        self.filesPath = path
        
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

