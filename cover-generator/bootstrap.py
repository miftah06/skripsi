import csv

def bootstrap():
    judul = input("Masukkan judul: ").strip()
    logo = input("Masukkan logo: ").strip()
    teks = input("Masukkan judul tugas (contoh: Skripsi): ").strip()
    nama = input("Masukkan nama: ").strip()
    numerik = input("Masukkan input numerik (contoh: NIM): ").strip()
    input_1 = input("Masukkan input 1 (contoh: Fakultas): ").strip()
    input_2 = input("Masukkan input 2 (contoh: Universitas): ").strip()
    tahun = input("Masukkan tahun (contoh: 2024): ").strip()

    with open('output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'Judul', 'Logo', 'Teks', 'Oleh', 'Input Numerik', 'Input 1', 'Input 2', 'Tahun'
        ])
        writer.writeheader()
        writer.writerow({
            'Judul': judul,
            'Logo': logo,
            'Teks': teks,
            'Oleh': nama,
            'Input Numerik': numerik,
            'Input 1': input_1,
            'Input 2': input_2,
            'Tahun': tahun
        })

if __name__ == "__main__":
    bootstrap()
