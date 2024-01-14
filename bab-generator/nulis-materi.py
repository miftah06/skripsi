import os
import pandas as pd
from datetime import datetime

def handle_nan(value, default_value=""):
    """Handles NaN values by replacing them with a default value."""
    return default_value if pd.isna(value) else value

def generate_html(data):
    halaman = handle_nan(data['Logo'][0], "Default Halaman")

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
            </p class="left"> <!-- Ubah ke left agar opsional di rata kiri -->
            <p class="indent justify ul-spacing first-line-indent">
                {halaman}
            </p>
            <p class="indent justify left">
                {', '.join([handle_nan(data[f'Opsional {i}'][0], "") for i in range(1, 16) if data[f'Opsional {i}'][0] != 0])}
            </p>
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

def main():
    # Baca data dari file Excel
    input_file_path = 'input_data.xlsx'
    data = pd.read_excel(input_file_path).to_dict(orient='list')

    # Panggil fungsi untuk membuat HTML
    output_html_path = generate_html(data)

if __name__ == "__main__":
    main()
