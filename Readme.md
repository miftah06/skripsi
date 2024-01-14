Sure, I'll provide a basic template for your README.md file for the `bab-generator` and `cover-generator` scripts. You may customize and expand it based on your specific needs.

```markdown
# Thesis Document Generator

This project consists of two scripts: `bab-generator` and `cover-generator`, designed to streamline the process of generating thesis documents.

## bab-generator

The `bab-generator` script is used for generating chapters and content for your thesis document. It takes user input for various sections, subheadings, and optional content and generates an HTML file that can be further converted into a PDF document.
# Bab Generator

## Introduction
This tool is a simple Python script to generate chapters (Bab) for academic purposes, such as thesis or research papers. It prompts the user for input including the chapter title, optional content for the page, and subheadings with their respective optional content. The generated output includes an HTML file and a PDF file.

## Getting Started

1. **Run Input Script:**
    ```bash
    python input.py
    ```
atau untuk materi   
   ```bash
    python input-materi.py
    ```
	
nulis materinya
    ```bash
    python nulis-materi.py
    ```

untuk nulis khusus automatis	
    ```bash
    python pdf-generator.py
    ```
	
lalu jalankan
    ```bash
    python pdf.py
    ```

    - Enter the chapter title (BAB), e.g., "BAB II PEMBAHASAN."
    - Provide optional content for the page.
    - Input information for each of the three optional sections.

2. **Run Generator Script:**
    ```bash
    python generator.py
    ```
    - This will generate an HTML file (`materi.html`) and attempt to create a PDF file (`materi_{{timestamp}}_page1.pdf`) using the ReportLab library. If the PDF creation fails, you will receive a message indicating the issue.

    ```bash
    Proses selesai. File HTML yang indah tersedia di materi.html.
    File materi_{{timestamp}}_page1.pdf tidak ditemukan. Pastikan file PDF dari ReportLab sudah terbuat.
    ```

3. **Run Generate Script:**
    ```bash
    python generate.py
    ```
    - This will generate an HTML file (`isi.html`) and a PDF file (`final_output.pdf`) using the provided input.

    ```bash
    Proses selesai. File HTML yang indah tersedia di isi.html.
    Proses selesai. File PDF yang indah tersedia di final_output.pdf.
    ```

## Requirements
- Python 3.x
- pandas
- xlsxwriter
- fpdf
- reportlab

## Troubleshooting
- If you encounter any issues with the PDF generation, make sure the necessary libraries (`fpdf` and `reportlab`) are installed.

### Prerequisites

Make sure you have the required dependencies installed:

- pandas
- fpdf
- nltk
- numpy
- beautifulsoup4
- torch
- reportlab
- Pypdf2
- cairosvg
- svgwrite
- weasyprint
- pdfkit
- PyMuPDF
- python-docx
- mpdf
- xlsxwriter
- openpyxl
- pymsgbox
- transformers
- matplotlib
- markdown2pdf

You can install these dependencies using:

```bash
pip install pandas fpdf nltk numpy beautifulsoup4 torch reportlab Pypdf2 cairosvg svgwrite weasyprint pdfkit PyMuPDF python-docx mpdf xlsxwriter openpyxl pymsgbox transformers matplotlib markdown2pdf
```

### Usage BAB-GENERATOR

```bash
cd bab-generator
```
-- lalu Readme.md

Follow the prompts to input information about each section of your thesis.

## cover-generator

```bash
cd cover-generator
```

The `cover-generator` script is designed to create a cover page for your thesis document.

### Prerequisites

Make sure you have the required dependencies installed:

- pandas
- fpdf

You can install these dependencies using:


-- Contoh install

```bash
pip install pandas
```

atau 

```
pkg install python-pandas
```

### Usage

```bash
python cover.py
python nulis.py
```
lalu

```
python pdf.py
```

Follow the prompts to input information about your thesis cover.

## Tools Conver HTML KE PDF

silahkan lihat di tools.txt

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

by Miftah Izharuddin.