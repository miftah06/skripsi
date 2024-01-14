import os
import pandas as pd
from fpdf import FPDF
from bs4 import BeautifulSoup

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


    # Save HTML
    output_html_path = 'isi.html'
    with open(output_html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(template)

    print("\nProses selesai. File HTML yang indah tersedia di isi.html.")
    return template

def beauty_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Set up some styles
    bold_style = 'B'
    newline_style = 'Ln'
    
    for key, values in data.items():
        if key.startswith("Subjudul"):
            # Add subjudul to PDF
            pdf.set_font("Arial", size=12)
            
            # Convert values[0] to string
            pdf.cell(0, 10, str(values[0]), ln=True, align='C')
            
            for value in values[1:]:
                pdf.set_font("Arial", size=12)
                
                # Convert value to string
                pdf.multi_cell(0, 10, str(value), align='L')
                
            pdf.ln(5)  # Add some space after each subjudul

    pdf.output("final_output.pdf")

    print("\nProses selesai. File PDF yang indah tersedia di final_output.pdf.")

def main():
    # Baca data dari file Excel
    input_file_path = 'input_data.xlsx'
    data = pd.read_excel(input_file_path).to_dict(orient='list')

    # Panggil fungsi untuk membuat HTML
    generate_html(data)

    # Panggil fungsi untuk membuat PDF
    beauty_pdf(data)

if __name__ == "__main__":
    main()
