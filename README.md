# PDF Bank Statement Processor - MVP

A Flask-based web application for uploading and processing bank statement PDFs. The application extracts text content from uploaded PDF files using pdfplumber and displays the results in a user-friendly interface.

## Features

- ✅ Clean and intuitive web interface
- ✅ Single and multiple PDF file upload support
- ✅ Drag-and-drop file upload functionality
- ✅ Text extraction from PDF bank statements using pdfplumber
- ✅ Real-time processing feedback
- ✅ Display extracted text with page-by-page breakdown
- ✅ Processing summary with statistics
- ✅ Copy-to-clipboard functionality for extracted text
- ✅ Modular and scalable architecture

## Project Structure

```
pdfBanks/
│
├── app/
│   ├── __init__.py              # Flask application factory
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py              # Main application routes
│   ├── services/
│   │   ├── __init__.py
│   │   └── pdf_processor.py    # PDF processing service
│   ├── static/
│   │   └── css/
│   │       └── style.css        # Application styles
│   └── templates/
│       └── index.html           # Main homepage template
│
├── uploads/                     # Directory for uploaded files
├── config.py                    # Application configuration
├── run.py                       # Application entry point
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd d:\pdfBanks
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server:**
   ```bash
   python run.py
   ```

2. **Access the application:**
   - Open your web browser and navigate to: `http://localhost:5000`
   - Or use: `http://127.0.0.1:5000`

3. **Upload PDF files:**
   - Click the upload area or drag and drop PDF files
   - Select one or multiple PDF bank statement files
   - Click "Process PDFs" to extract text

## Usage

1. **Upload PDFs:**
   - Navigate to the homepage
   - Click on the upload area or drag and drop your PDF files
   - Multiple files can be selected at once

2. **View Results:**
   - After processing, you'll see a summary showing:
     - Total files processed
     - Number of successful extractions
     - Number of failed extractions
     - Total pages processed
   - Each file's extracted text is displayed with page numbers
   - Use the "Copy Text" button to copy extracted content

3. **Supported Files:**
   - Only PDF files are accepted
   - Maximum file size: 16MB per file
   - Multiple files can be processed simultaneously

## API Endpoints

- `GET /` - Homepage with upload interface
- `POST /upload` - Handle file uploads and process PDFs
- `GET /health` - Health check endpoint

## Configuration

Edit `config.py` to customize:

- `UPLOAD_FOLDER` - Directory for uploaded files
- `MAX_CONTENT_LENGTH` - Maximum file size (default: 16MB)
- `ALLOWED_EXTENSIONS` - Allowed file types (default: PDF only)
- `SECRET_KEY` - Flask secret key (change in production!)

## Future Enhancements

This MVP is designed to be extended with additional features:

- 📊 **Structured data extraction** - Parse tables and extract structured data
- 💾 **CSV export** - Export extracted data to CSV format
- 🗄️ **Database integration** - Store processing history and results
- 🔐 **User authentication** - Add login and user management
- 📈 **Advanced analytics** - Bank statement analysis and insights
- 🔍 **OCR support** - Handle scanned PDFs with image-based text
- 📧 **Email notifications** - Send processing results via email
- ☁️ **Cloud storage** - Integration with cloud storage services

## Technology Stack

- **Backend:** Flask 3.0.0
- **PDF Processing:** pdfplumber 0.10.3
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **File Handling:** Werkzeug 3.0.1

## Development Notes

- The application uses the factory pattern for Flask initialization
- Services are modular and separated from routes for better maintainability
- Uploaded files are stored with timestamps to prevent conflicts
- Error handling is implemented at multiple levels
- The frontend uses modern JavaScript (ES6+) with async/await

## Troubleshooting

**Issue:** Port 5000 already in use
- **Solution:** Change the port in `run.py` or stop the application using port 5000

**Issue:** PDF processing fails
- **Solution:** Ensure the PDF is not password-protected and contains extractable text

**Issue:** Large files not uploading
- **Solution:** Increase `MAX_CONTENT_LENGTH` in `config.py`

## License

This is an MVP project. Add appropriate license as needed.

## Support

For issues or questions, please review the code structure and error logs in the terminal.

---

**Version:** 1.0.0 (MVP)  
**Last Updated:** December 2025
