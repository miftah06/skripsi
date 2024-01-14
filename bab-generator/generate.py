import os
import pandas as pd
from fpdf import FPDF

def generate_opsional_html(subjudul_data):
    opsional_html = ""
    for key, values in subjudul_data.items():
        if key.startswith("Opsional"):
            opsional_html += f"""
                <div class="bold">{values[0]}</div>
                <ul>
            """
            for item in values[1:]:
                opsional_html += f"<li>{item}</li>"
            opsional_html += "</ul>"
    return opsional_html

import pandas as pd

def handle_nan(value, default_value=""):
    """Handles NaN values by replacing them with a default value."""
    return default_value if pd.isna(value) else value

def generate_html(data):
    halaman = handle_nan(data['Logo'][0], "Default Halaman")  # Mengambil nilai dari 'Logo' sebagai 'halaman'
    
    template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{halaman} - {handle_nan(data['Bab'][0], "Default Bab")}</title>
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
            <p class="indent justify">
                {halaman}
            </p>
            <ol>
    """

    # Save HTML
    output_html_path = 'isi-manual.html'
    with open(output_html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(template)

    print("\nProses selesai. File HTML yang indah tersedia di isi-manual.html.")
    return template

def main():
    # Baca data dari file Excel
    input_file_path = 'input_data.xlsx'
    data = pd.read_excel(input_file_path).to_dict(orient='list')

    # Panggil fungsi untuk membuat HTML
    html_content = generate_html(data)

    with open('output.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print("\nProses selesai. File HTML yang dihasilkan tersedia di output.html.")

if __name__ == "__main__":
    main()
