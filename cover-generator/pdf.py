import fitz  # PyMuPDF
import numpy as np
import chardet
from bs4 import BeautifulSoup
from fpdf import FPDF

def html_to_pdf(input_html, output_pdf):
    # Membaca isi HTML dari file
    with open(input_html, 'rb') as file:
        # Deteksi encoding
        rawdata = file.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']

        # Dekode isi HTML
        html_content = rawdata.decode(encoding)

    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = [p.get_text() for p in soup.find_all('p')]

    # Membuat PDF dengan PyMuPDF
    pdf = fitz.open()
    page = pdf.new_page()

    # Menyusun teks ke dalam PDF
    y_offset = 20
    for paragraph in paragraphs:
        page.insert_text((20, y_offset), paragraph, fontname="helv", fontsize=12)
        y_offset += 14

    # Simpan hasil ke file PDF
    pdf.save(output_pdf)

    # Jika ingin menyimpan juga sebagai teks
    with open('output_cover.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write('\n'.join(paragraphs))

    print(f"File PDF ({output_pdf}) dan teks (output_cover.txt) telah berhasil dibuat.")

if __name__ == "__main__":
    html_to_pdf('cover.html', 'output_cover.pdf')
