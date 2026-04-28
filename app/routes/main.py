"""Main routes for the PDF processing application"""
from flask import Blueprint, render_template, request, jsonify, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
from pathlib import Path
from datetime import datetime
from io import BytesIO
import zipfile

from config import Config
from app.services.pdf_processor import PDFProcessor

bp = Blueprint('main', __name__)
pdf_processor = PDFProcessor()


@bp.route('/')
def index():
    """Homepage with file upload interface"""
    return render_template('index.html')


@bp.route('/upload', methods=['POST'])
def upload_files():
    """
    Handle PDF file uploads and process them
    Returns JSON response with processing results
    """
    # Check if files were uploaded
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
    
    files = request.files.getlist('files[]')
    
    # Validate that files were selected
    if not files or files[0].filename == '':
        return jsonify({'error': 'No files selected'}), 400
    
    uploaded_files = []
    errors = []
    
    # Process each uploaded file
    for file in files:
        if file and Config.allowed_file(file.filename):
            # Secure the filename and save
            filename = secure_filename(file.filename)
            # Add timestamp to avoid filename conflicts
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            unique_filename = f"{timestamp}_{filename}"
            filepath = os.path.join(Config.UPLOAD_FOLDER, unique_filename)
            
            try:
                file.save(filepath)
                uploaded_files.append(filepath)
            except Exception as e:
                errors.append(f"Error saving {filename}: {str(e)}")
        else:
            errors.append(f"Invalid file type: {file.filename}. Only PDF files are allowed.")
    
    # If no valid files were uploaded
    if not uploaded_files:
        return jsonify({'error': 'No valid PDF files uploaded', 'details': errors}), 400
    
    # Process the uploaded PDFs
    try:
        results = pdf_processor.process_multiple_pdfs(uploaded_files)
        summary = pdf_processor.get_summary(results)
        
        response_data = {
            'success': True,
            'summary': summary,
            'results': results,
            'errors': errors if errors else None
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        return jsonify({'error': f'Error processing PDFs: {str(e)}'}), 500
    
    finally:
        # Optional: Clean up uploaded files after processing
        # Uncomment the lines below if you want to delete files after processing
        # for filepath in uploaded_files:
        #     try:
        #         os.remove(filepath)
        #     except:
        #         pass
        pass


@bp.route('/results')
def results():
    """Display results page"""
    return render_template('results.html')


@bp.route('/download-text', methods=['POST'])
def download_text():
    """
    Download extracted text as a .txt file
    Receives text content and filename in POST request
    """
    try:
        data = request.get_json()
        text_content = data.get('text', '')
        filename = data.get('filename', 'extracted_text.txt')
        
        # Remove .pdf extension and add .txt
        if filename.lower().endswith('.pdf'):
            filename = filename[:-4] + '.txt'
        elif not filename.lower().endswith('.txt'):
            filename = filename + '.txt'
        
        # Create a BytesIO object with the text content
        text_io = BytesIO(text_content.encode('utf-8'))
        text_io.seek(0)
        
        return send_file(
            text_io,
            mimetype='text/plain',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': f'Error creating download: {str(e)}'}), 500


@bp.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'PDF Bank Statement Processor'}), 200
