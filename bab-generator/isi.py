import os
import pandas as pd
from fpdf import FPDF
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfWriter, PdfReader

def handle_nan(value, default_value=""):
    """Handles NaN values by replacing them with a default value."""
    return default_value if pd.isna(value) else value

def generate_html(data):
    halaman = handle_nan(data['Opsional 1'][0], "Default Halaman")
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{halaman} - {handle_nan(data['Bab'][0], "Default Bab")}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {{
                margin: 4%;
                font-family: 'Times New Roman', Times, serif;
            }}
            .container {{
                margin: auto;
                width: 70%;
                text-align: justify;
            }}
            .bold {{
                font-weight: bold;
                font-size: 16px;
            }}
            .indent {{
                text-indent: 20px;
            }}
            .justify {{
                text-align: justify;
            }}
            .left {{
                text-align: left;
                margin-bottom: 2em;
            }}
            .center {{
                text-align: center;
            }}
            .ul-spacing {{
                margin-left: 1em;
            }}
            .first-line-indent {{
                text-indent: 3em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="bold center">{handle_nan(data['Bab'][0], "")}</h1>
            <p class="indent justify bold ">
                {handle_nan(data['Subjudul 1'][0], "Default Subjudul")}
            </p> <!-- Remove class="left" here -->
            <p class="indent justify ul-spacing first-line-indent">
                {halaman}
            </p>
            <p class="indent justify ul-spacing first-line-indent">
                {handle_nan(data['Logo 1'][0], "Default Keterangan")}
            </p>
            <ol>
        <div class="container">
            <h1 class="bold center">{handle_nan(data['Bab'][0], "")}</h1>
            <p class="indent justify bold ">
                {handle_nan(data['Subjudul 2'][0], "Default Subjudul")}
            </p> <!-- Remove class="left" here -->
            <p class="indent justify ul-spacing first-line-indent">
                {halaman}
            </p>
            <p class="indent justify ul-spacing first-line-indent">
                {handle_nan(data['Logo 2'][0], "Default Keterangan")}
            </p>
            <ol>
        <div class="container">
            <h1 class="bold center">{handle_nan(data['Bab'][0], "")}</h1>
            <p class="indent justify bold ">
                {handle_nan(data['Subjudul 3'][0], "Default Subjudul")}
            </p> <!-- Remove class="left" here -->
            <p class="indent justify ul-spacing first-line-indent">
                {halaman}
            </p>
            <p class="indent justify ul-spacing first-line-indent">
                {handle_nan(data['Logo 3'][0], "Default Keterangan")}
            </p>
            <ol>
    """

    # Generate list items for optional data
    for i in range(1, 16):  # Assuming optional data is up to 15
        optional_key = f'Opsional {i}'
        if optional_key in data and not pd.isna(data[optional_key][0]):
            optional_value = handle_nan(data[optional_key][0], f"")
            template += f"                <li class='indent justify left'>{optional_value}</li>\n"

    template += """
            </ol>
        </div>
    </body>
    </html>
    """

    # Save HTML
    output_html_path = f'materi_{timestamp}.html'
    with open(output_html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(template)

    print("\nProses selesai. File HTML yang indah tersedia di materi.html.")
    return output_html_path

def beauty_pdf(data, output_html_path):
    pdf_output_path = "final_output.pdf"

    # Convert HTML to PDF using ReportLab
    c = canvas.Canvas(pdf_output_path, pagesize=letter)
    with open(output_html_path, 'r', encoding='utf-8') as html_file:
        for line in html_file:
            c.drawString(100, 800, line.strip())
            c.showPage()
    c.save()

    # Check if the PDF file from ReportLab is created
    pdf_from_reportlab_path = output_html_path.replace('.html', '_page1.pdf')
    if os.path.exists(pdf_from_reportlab_path):
        # Merge PDFs using PyPDF2
        pdf_writer = PdfWriter()
        pdf_reader = PdfReader(pdf_output_path)
        pdf_writer.add_page(pdf_reader.pages[0])
        
        pdf_reader = PdfReader(pdf_from_reportlab_path)
        pdf_writer.add_page(pdf_reader.pages[0])
        
        with open(pdf_output_path, 'wb') as pdf_out:
            pdf_writer.write(pdf_out)

        print("\nProses selesai. File PDF yang indah tersedia di final_output.pdf.")
    else:
        print(f"File {pdf_from_reportlab_path} tidak ditemukan. Pastikan file PDF dari ReportLab sudah terbuat.")

def main():
    # Baca data dari file Excel
    input_file_path = 'input_data.xlsx'
    data = pd.read_excel(input_file_path).to_dict(orient='list')

    # Panggil fungsi untuk membuat HTML
    output_html_path = generate_html(data)

    # Panggil fungsi untuk membuat PDF
    beauty_pdf(data, output_html_path)

if __name__ == "__main__":
    main()
