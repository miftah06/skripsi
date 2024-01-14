import pandas as pd
import os
import pdfkit
import random

def handle_nan(value, default):
    return default if pd.isna(value) else value

def generate_opsional_list(data, page_number, katakunci_list):
    opsional_html = ""
    for i in range(1, 10):
        opsional_key = f'Opsional {i}'
        if opsional_key in data and len(data[opsional_key]) > page_number - 1:
            opsional_value = handle_nan(data[opsional_key][page_number - 1], f"Default Opsional {i}")
            opsional_html += f"                <li class='indent justify left'>{opsional_value}</li>\n"

    # Tambahkan kata kunci dari generate_katakunci.txt
    random.shuffle(katakunci_list)
    opsional_html += f"<li class='indent justify left'>{', '.join(katakunci_list)}</li>\n"

    return opsional_html

def generate_html(data, katakunci_list):
    page_number = []
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
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <div class="container">
    """
    for i, bab_key in enumerate(data['Bab']):
        subjudul_key = f'Subjudul {i+1}'
        Halaman_key = f'Halaman'

        template += f"""
            <!-- Page {i+1} -->
            <h1 class="bold left">{handle_nan(data['Bab'][i], "Default Bab")}</h1>
            <p class="indent justify">
                {handle_nan(data[subjudul_key][0], f"Default {subjudul_key}")}
            </p>
            <div class="indent justify">
                <ul class="indent justify left">{generate_opsional_list(katakunci_list, page_number, keyword_list)}</ul>
                <p class="indent justify left">{handle_nan(data[Halaman_key][0], "Default Halaman")}</p>
            </div>
        """
    template += """
        </div>
    </body>
    </html>
    """
    return template

def generate_pdf_from_html(html_content, output_pdf):
    with open('materi.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    # Convert HTML to PDF using pdfkit
    pdfkit.from_file('materi.html', output_pdf)

    # Remove temporary HTML file
    os.remove('materi.html')

    print(f"Dokumen PDF berhasil disimpan di {output_pdf}")

if __name__ == "__main__":
    # Read data from Excel file
    excel_file = 'data.xlsx'
    if os.path.exists(excel_file):
        data = pd.read_excel(excel_file).to_dict(orient='list')
    else:
        print(f"File '{excel_file}' not found.")
        data = {}

    # Read keywords from generate_katakunci.txt
    with open('katakunci.csv', 'r', encoding='utf-8') as katakunci_file:
        katakunci_list = katakunci_file.read().strip().split(',')
        
    with open('katakunci.txt', 'r', encoding='utf-8') as katakunci_file:
        keyword_list = katakunci_file.read().strip().split(',')
    
    html_content = generate_html(data, katakunci_list)
    output_pdf = "materi.pdf"

    generate_pdf_from_html(html_content, output_pdf)
