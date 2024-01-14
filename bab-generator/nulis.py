import os
from fpdf import FPDF
from PyPDF2 import PdfMerger
import markdown2

def html_to_pdf_wkhtmltopdf(input_html, output_pdf):
    cmd = f'wkhtmltopdf {input_html} {output_pdf}'
    os.system(cmd)
    print(f"\nProses selesai. File PDF yang indah tersedia di {output_pdf}.")

def md_to_pdf(input_md, output_pdf):
    with open(input_md, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = markdown2.markdown(md_content)

    with open('temp.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    html_to_pdf_wkhtmltopdf('temp.html', output_pdf)
    os.remove('temp.html')

def beauty_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, values in data.items():
        if key.startswith("Subjudul"):
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, str(values[0]), ln=True, align='C')

            for value in values[1:]:
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, str(value), align='L')

            pdf.ln(5)

    pdf.output("isi-manual-fpdf.pdf")
    print("\nProses selesai. File PDF yang indah tersedia di isi-manual-fpdf.pdf.")

def main():
    # Render generate.py output HTML to PDF using wkhtmltopdf
    html_to_pdf_wkhtmltopdf('anu.html', 'isi-manual.pdf')

    # Render generate.py output MD to HTML
    md_to_pdf('isi-manual.md', 'isi-manual.html')

    # Generate data untuk beauty_pdf (sesuaikan sesuai kebutuhan)
    data = {"Subjudul1": ["Isi subjudul 1.1", "Isi subjudul 1.2"],
            "Subjudul2": ["Isi subjudul 2.1", "Isi subjudul 2.2"]}

    # Generate PDF using fpdf
    beauty_pdf(data)

    print("\nProses selesai. File PDF, MD, dan HTML yang dihasilkan tersedia.")

if __name__ == "__main__":
    main()
