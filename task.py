import os
import PyPDF2

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
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            text = extract_text_from_pdf(pdf_path)
            preprocessed_text = preprocess_text(text)
            # Further processing and analysis here
            print(f"Text extracted from {pdf_path}: {preprocessed_text[:100]}...")
            # Call functions for content understanding and resource generation

# Example usage
if __name__ == "__main__":
    pdf_folder = "C:/Users/Kshitij/Desktop/AI Task"
    process_textbook(pdf_folder)
