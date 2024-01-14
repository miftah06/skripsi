import os
import pandas as pd

def validate_length(judul, skripsi):
    while len(judul) != len(skripsi[0]):
        print("Panjang judul tulisan skripsi dan salah satu dari tulisan opsional harus sama.")
        judul = input("Masukkan Bagan judul pada isi ex: \n A. Latar Belakang: ").strip()

    # Menerima input untuk setiap opsional
    opsional = []
    for i in range(3):  # Sesuaikan dengan jumlah opsional
        prompt = f"Opsional berupa isi keterangan misal: ex: \n Berupa isi Rumusan Masalah \n1. Apa yang dixxx...? 1 \n atau materi dst.. {i + 1}: "
        input_opsional = input(prompt).strip()
        opsional.append(input_opsional)

    return judul, opsional

def validate_subjudul(judul, i):
    while not judul:
        print(f"Subjudul {i} tidak boleh kosong.")
        judul = input(f"Masukkan Subjudul {i} misal' A. Latar Belakang : ").strip()
    return judul

def split_title_into_sections(judul):
    # Memecah judul menjadi bagian-bagian
    sections = judul.split('{')

    # Menghapus karakter tidak diinginkan
    sections = [section.replace('}', '') for section in sections]

    return sections

def bootstrap():
    # Meminta input dari pengguna
    bab = input("Masukkan BAB misal' BAB II PEMBAHASAN: ").strip()

    # Membuat DataFrame kosong
    data_dict = {
        'Bab': [],
        'Logo 1': [],
        'Logo 2': [],
        'Logo 3': [],
        'Opsional 1': [],
        'Opsional 2': [],
        'Opsional 3': [],
    }

    i = 1
    while True:
        # Meminta input dari pengguna untuk subjudul dan opsional
        subjudul, opsional = validate_length("", [[] for _ in range(15)])  # Menyesuaikan dengan perubahan dalam validate_length
        subjudul = validate_subjudul(subjudul, i)

        # Memecah judul menjadi bagian-bagian
        subjudul_sections = split_title_into_sections(subjudul)

        # Menambahkan data ke dalam DataFrame
        data_dict['Bab'].append(bab)
        data_dict['Logo 1'].append(input("Masukkan Ket 1: ").strip())
        data_dict['Logo 2'].append(input("Masukkan Ket 2: ").strip())
        data_dict['Logo 3'].append(input("Masukkan Ket 3: ").strip())

        for j in range(3):
            data_dict[f'Opsional {j + 1}'].append(opsional[j])

        data_dict[f'Subjudul {i}'] = subjudul_sections

        i += 1

        # Mengecek apakah pengguna ingin melanjutkan atau tidak
        lanjut = input("Apakah ingin menambahkan subjudul lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    # Print lengths of arrays for debugging
    for key, value in data_dict.items():
        print(f"Length of {key}: {len(value)}")

    # Membuat DataFrame dari input
    df = pd.DataFrame(data_dict)

    # Menyimpan DataFrame ke file Excel
    with pd.ExcelWriter('input_data.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

if __name__ == "__main__":
    bootstrap()
