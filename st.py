import streamlit as st
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
    # Add your preprocessing steps here (if any)
    return text

# Main function to process textbook
def process_textbook(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    preprocessed_text = preprocess_text(text)
    # Further processing and analysis here
    return preprocessed_text

# Streamlit UI
def main():
    st.title("PDF Text Extraction and Preprocessing")

    # File upload
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Create temp_files directory if it doesn't exist
        os.makedirs("temp_files", exist_ok=True)
        
        # Save uploaded file
        with open(os.path.join("temp_files", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Process the uploaded file
        preprocessed_text = process_textbook(os.path.join("temp_files", uploaded_file.name))

        # Display the preprocessed text
        st.header("Preprocessed Text")
        st.text_area("Preprocessed Text", value=preprocessed_text, height=400)

if __name__ == "__main__":
    main()
