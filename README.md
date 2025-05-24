# 📄 PDF Tool

A powerful web-based PDF utility that enables you to **merge**, **split**, and **convert images to PDFs**, along with other useful PDF operations. This project is built with a **Flask** backend and a lightweight **HTML/CSS/JavaScript** frontend, using **Bootstrap** for styling components.

## 🚀 Features

* ✅ Merge multiple PDFs into a single file
* ✅ Split PDF files by page range
* ✅ Convert images (JPG, PNG) to PDF
* ✅ Perform operations using clean REST APIs
* ✅ Fast, intuitive interface built with HTML, CSS, and Bootstrap
* ✅ Simple and interactive frontend using Vanilla JS

## 🧰 Tech Stack

### Backend

* **Python + Flask** – Handles all API requests
* **mypdf** – Custom library to manipulate PDF files

### Frontend

* **HTML/CSS/Bootstrap** – UI layout and styling
* **Vanilla JavaScript** – Interacts with the Flask API

## 📦 Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/Mohsinullahshah11/pdf_tool
   cd pdf-tool
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**

   ```bash
   python Backend/index.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5000` in your web browser.

## 📂 Folder Structure

```
PDF_TOOL/
├── Backend/
│   ├── __pycache__/
│   ├── uploads/
│   ├── venv/
│   ├── index.py              # Main Flask app entry
│   ├── pdfOperations.py      # PDF logic (merge/split/etc.)
│   ├── utilites.py           # Utility functions
│   └── requirements.txt
├── Frontend/
│   ├── assets/
│   │   ├── script/
│   │   │   ├── mergePDF.js
│   │   │   ├── splitPDF.js
│   │   │   └── script.js
│   │   └── style/
│   └── views/
│       ├── index.html
│       ├── merge_PDF.html
│       └── split_PDF.html
└── README.md
```
