import os
from PyPDF2 import PdfMerger

def merge_html_to_pdf(html_files, output_pdf):
    merger = PdfMerger()

    for html_file in html_files:
        pdf_file = f"{os.path.splitext(html_file)[0]}.pdf"
        cmd = f'wkhtmltopdf {html_file} {pdf_file}'
        os.system(cmd)
        merger.append(pdf_file)

    merger.write(output_pdf)
    merger.close()

    for html_file in html_files:
        pdf_file = f"{os.path.splitext(html_file)[0]}.pdf"
        os.remove(pdf_file)

    print(f"\nProses selesai. File PDF yang indah tersedia di {output_pdf}.")

def main():
    # Input HTML files to be merged
    html_files_to_merge = []
    while True:
        html_file = input("Masukkan nama file HTML (tekan Kosongkan untuk mengakhiri): ")
        if not html_file:
            break
        html_files_to_merge.append(html_file)

    # Output PDF file
    output_pdf_file = input("Masukkan nama file PDF hasil merge: ")

    # Merge HTML to PDF using wkhtmltopdf
    merge_html_to_pdf(html_files_to_merge, output_pdf_file)

    # Log the process
    with open("merge_log.txt", "a") as log_file:
        log_file.write(f"{', '.join(html_files_to_merge)} merged into {output_pdf_file}\n")

    print(f"\nProses selesai. File PDF hasil merge tersedia.")

if __name__ == "__main__":
    main()
