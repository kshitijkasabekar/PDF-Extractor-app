import os
import PyPDF2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Function for text preprocessing
def preprocess_text(text):
    # Add your preprocessing steps here
    return text

# Main function to process textbook
def process_textbook(pdf_folder):
    processed_textbooks = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            preprocessed_text = preprocess_text(text)
            processed_textbooks.append({'filename': filename, 'text': preprocessed_text})
            # Further processing and analysis here
            print(f"Text extracted from {pdf_path}: {preprocessed_text[:100]}...")
            # Call functions for content understanding and resource generation
    return processed_textbooks

# API endpoint to upload textbook PDF
@app.route('/', methods=['GET', 'POST'])
def upload_textbook():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and file.filename.endswith('.pdf'):
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(uploaded_file_path)
        processed_textbooks = process_textbook(uploaded_file_path)
        # Process the uploaded textbook and generate resources
        return jsonify({'message': 'Textbook uploaded and processed', 'processed_textbooks': processed_textbooks})
    else:
        return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = "C:/Users/Kshitij/Desktop/AI Task"
    app.run(debug=True)
