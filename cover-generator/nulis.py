import pandas as pd
from fpdf import FPDF
import pdfkit
import os

def handle_nan(value, default):
    return default if pd.isna(value) else value

def generate_html(data):
    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{handle_nan(data['Logo'][0], "Default Logo")}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <style>
            body {{
                margin: 4%;
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
                text-align: left;  /* Ubah ke left agar teks opsional di rata kiri */
            }}
            .center {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="bold center">{handle_nan(data['Bab'][0], "Default Bab")}</h1>
            <p class="indent justify">
                {handle_nan(data['Subjudul 1'][0], "Default Subjudul")}
            </p class="left"> <!-- Ubah ke left agar opsional di rata kiri -->
            <ol>
    """

    # Generate list items for opsional data
    for i in range(1, 16):  # Assuming opsional data is up to 15
        opsional_key = f'Opsional {i}'
        if opsional_key in data:
            opsional_value = handle_nan(data[opsional_key][0], f"Default Opsional {i}")
            template += f"                <li class='indent justify left'>{opsional_value}</li>\n"

    template += """
            </ol>
        </div>
    </body>
    </html>
    """
    return template

def generate_pdf_from_html(html_content, output_pdf):
    with open('cover.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    # Konversi HTML ke PDF menggunakan modul pdfkit
    pdfkit.from_file('cover.html', output_pdf)

    # Hapus file HTML sementara
    os.remove('cover.html')

    print(f"Dokumen PDF berhasil disimpan di {output_pdf}")

if __name__ == "__main__":
    # Contoh data, gantilah dengan cara sesuai kebutuhan
    data = {
        'Logo': ['Logo Perusahaan'],
        'Bab': ['Bab I Pendahuluan'],
        'Subjudul 1': ['Latar Belakang'],
        'Opsional 1': ['Opsional 1'],
        'Opsional 2': ['Opsional 2'],
        # ... tambahkan opsional lainnya sesuai kebutuhan
    }

    html_content = generate_html(data)
    output_pdf = "output.pdf"
    
    generate_pdf_from_html(html_content, output_pdf)
