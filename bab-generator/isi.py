import os
import chardet
from fpdf import FPDF
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def read_text_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    return content

def preprocess_text(content):
    # Use nltk to process text, such as tokenization, removing stop words, and counting word frequencies
    nltk.download('punkt')
    nltk.download('stopwords')
    
    # Tokenization
    tokens = word_tokenize(content)

    # Remove stop words
    stop_words = set(stopwords.words('indonesian'))
    filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

    # Count word frequencies
    fdist = FreqDist(filtered_tokens)

    # Only take the top 100 words as an example
    top_words = [word for word, freq in fdist.most_common(100)]
    
    return top_words

def create_html_from_content(content):
    # Use BeautifulSoup to generate HTML from text
    soup = BeautifulSoup(content, 'html.parser')
    html_content = soup.prettify()
    return html_content

def create_pdf_from_html(html_content, output_file):
    # Use FPDF to print HTML to PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add HTML content to PDF
    pdf.write_html(html_content)

    # Save PDF
    pdf.output(output_file)

def main():
    input_file_path = "input_data.xlsx"
    output_pdf_path = "isi.pdf"

    # Read content from text file
    text_content = read_text_file(input_file_path)

    # Process text (e.g., tokenization, removing stop words, etc.)
    preprocessed_content = preprocess_text(text_content)

    # Create HTML from content
    html_content = create_html_from_content(preprocessed_content)

    # Create PDF from HTML
    create_pdf_from_html(html_content, output_pdf_path)

if __name__ == "__main__":
    main()
