```markdown
# Bab Generator

Bab Generator adalah sebuah alat otomatis untuk menghasilkan dokumen skripsi atau tulisan ilmiah dengan format bab seperti pendahuluan, pembahasan, dan tinjauan pustaka. Alat ini menggunakan beberapa modul Python untuk menghasilkan output dalam bentuk PDF dan HTML.

Berikut adalah contoh Readme.md yang diubah dengan modifikasi terkait penggunaan `weasyprint` dan penggantian beberapa modul:

```markdown
# Bab Generator

Bab Generator adalah alat sederhana untuk menghasilkan berkas PDF dari HTML, Markdown, dan data struktur tertentu.

## Instalasi Dependensi

Sebelum menggunakan alat ini, pastikan untuk menginstal dependensi yang diperlukan. Jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

Pastikan juga Anda memiliki `wkhtmltopdf` terinstal. Jika belum, Anda dapat menginstalnya dengan perintah:

```bash
Download wkhtmltopdf` di link 
```
```
https://wkhtmltopdf.org/downloads.html
```

atau WeasyPrint terinstal. Jika belum, Anda dapat menginstalnya dengan perintah:

```termux
pkg install weasyprint 
```
``` jika pip tidak terinstall
pkg install python-<pip module>

```

## Penggunaan

1. **HTML ke PDF menggunakan WeasyPrint:**

   Untuk mengonversi HTML ke PDF, jalankan perintah berikut:

   ```bash
   python nulis.py
   ```

   Hasilnya akan tersedia di `generate_output.pdf`.

2. **MD ke HTML ke PDF:**

   Untuk mengonversi Markdown ke HTML dan kemudian ke PDF, jalankan perintah berikut:

   ```bash
   python nulis.py
   ```

   Hasilnya akan tersedia di `generate_output.html` dan `generate_output.pdf`.

3. **Penggabungan PDF:**

   Untuk menggabungkan beberapa PDF, jalankan perintah berikut:

   ```bash
   python nulis.py
   ```

   Hasilnya akan tersedia di `final_output.pdf`.

Pastikan untuk menyesuaikan skrip sesuai kebutuhan dan menambahkan data sesuai dengan struktur yang Anda inginkan.

## Struktur Data

Struktur data yang digunakan untuk menghasilkan PDF dapat disesuaikan. Contoh struktur data diberikan di dalam skrip (`data` pada fungsi `beauty_pdf`).

## Catatan

Pastikan untuk mengganti data dan struktur sesuai kebutuhan Anda. Gunakan alat ini sesuai dengan lisensi dan pedoman yang berlaku.

Selamat mencoba!
```

Pastikan untuk menyesuaikan bagian penggunaan, struktur data, dan catatan sesuai dengan kebutuhan proyek Anda.

## Modul yang Diperlukan

Pastikan Anda telah menginstal modul-modul berikut sebelum menggunakan Bab Generator:

- `chardet`
- `fpdf`
- `nltk`
- `numpy`
- `beautifulsoup4`
- `torch`
- `reportlab`
- `PyPDF2`
- `cairosvg`
- `svgwrite`
- `weasyprint`
- `pdfkit`
- `PyMuPDF`
- `python-docx`
- `mpdf`
- `xlsxwriter`
- `openpyxl`
- `pymsgbox`
- `transformers`
- `matplotlib`
- `markdown2pdf`

Anda dapat menginstal modul-modul ini dengan menjalankan perintah berikut:

```bash
pip install chardet fpdf nltk numpy beautifulsoup4 torch reportlab PyPDF2 cairosvg svgwrite weasyprint pdfkit PyMuPDF python-docx mpdf xlsxwriter openpyxl pymsgbox transformers matplotlib markdown2pdf
```

## Penggunaan

1. **input.py**: Jalankan skrip ini untuk memasukkan nilai input seperti BAB, judul, dan isi tulisan skripsi. Hasilnya akan disimpan dalam file Excel, HTML, dan TXT.

```bash
python input.py
```

2. **generate.py**: Skrip ini mengonversi input dari file Excel menjadi HTML dan PDF. Jalankan perintah berikut:

```bash
python generate.py
```

3. **manual.py**: Skrip ini menghasilkan contoh dokumen HTML dan PDF. Jalankan perintah berikut:

```bash
python manual.py
```

4. **generator.py**: Skrip ini menghasilkan dokumen HTML dan PDF dari input yang telah dimasukkan. Jalankan perintah berikut:

```bash
python generator.py
```

5. **nulis.py**: Skrip ini mengonversi HTML ke PDF menggunakan modul `pdfkit`. Pastikan Anda memiliki `wkhtmltopdf` terinstal. Jalankan perintah berikut:

```bash
python nulis.py
```
atau

```bash
python pdf.py
```
## Catatan

- Pastikan Anda telah menginstal semua modul yang diperlukan sebelum menjalankan skrip.
- Jika Anda mengalami masalah terkait `wkhtmltopdf`, pastikan `wkhtmltopdf` terinstal dan ditambahkan ke PATH.

```

Done