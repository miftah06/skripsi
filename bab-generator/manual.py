# isi-manual.py
# Isi dari manual atau panduan pengguna

isi_manual_content = """
Bab I: Pendahuluan
-------------------
Tulis isi pendahuluan di sini...

Bab II: Pembahasan
-------------------
Tulis isi pembahasan di sini...

Bab III: Tinjauan Pustaka
-------------------------
Tulis tinjauan pustaka di sini...
"""

output_file_path = "isi-manual.md"

with open(output_file_path, "w") as isi_manual_file:
    isi_manual_file.write(isi_manual_content)

print(f"\nProses selesai. File isi-manual.md telah dibuat di lokasi: {output_file_path}")
