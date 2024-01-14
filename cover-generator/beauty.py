from fpdf import FPDF

def beauty_pdf():
    # Membaca data dari file CSV
    with open('output.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {key: [] for key in reader.fieldnames}

        for row in reader:
            for key in reader.fieldnames:
                data[key].append(row[key].strip() if row[key] else '')

    # Membuat file HTML dari data
    html_content = generate_html(data)

    # Menyimpan HTML ke dalam file
    with open('output.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    # Mengonversi HTML menjadi PDF dengan fpdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open('output.html', 'r', encoding='utf-8') as html_file:
        for line in html_file:
            pdf.multi_cell(0, 10, line)
    pdf.output('beautiful_output.pdf')

if __name__ == "__main__":
    beauty_pdf()
    print("File PDF yang indah telah berhasil dibuat dalam file beautiful_output.pdf.")
