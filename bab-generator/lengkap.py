import os
import pandas as pd

def validate_length(judul, skripsi):
    while len(judul) != len(skripsi[0]):
        print("Panjang judul tulisan skripsi dan salah satu dari tulisan Subjudul harus sama.")
        judul = input("Masukkan Bagan judul pada isi ex: \n A. Latar Belakang: ").strip()

    # Menerima input untuk setiap Subjudul
    Subjudul = []
    for i in range(15):  # Sesuaikan dengan jumlah Subjudul
        prompt = f"Subjudul berupa isi keterangan misal: ex: \n Berupa isi Rumusan Masalah \n1. Apa yang dixxx...? 1 \n atau materi dst.. {i + 1}: "
        input_Subjudul = input(prompt).strip()
        Subjudul.append(input_Subjudul)

    # Menerima input untuk setiap Opsional
    Opsional = []
    for i in range(15):  # Sesuaikan dengan jumlah Opsional
        prompt = f"Opsional berupa isi keterangan misal: ex: \n Berupa isi Rumusan Masalah \n1. Apa yang dixxx...? 1 \n atau materi dst.. {i + 1}: "
        input_Opsional = input(prompt).strip()
        Opsional.append(input_Opsional)

    return judul, Subjudul, Opsional

def validate_Subjudul(Subjudul, i):
    while not Subjudul:
        print(f"Subjudul {i} tidak boleh kosong.")
        Subjudul = input(f"Masukkan Subjudul {i} misal' A. Latar Belakang : ").strip()
    return Subjudul

def validate_Opsional(Opsional, i):
    while not Opsional:
        print(f"Opsional {i} tidak boleh kosong.")
        Opsional = input(f"Masukkan Isi Subjudul {i} misal' 1. Apa yang dixxx...? 1 : ").strip()
    return Opsional

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
    data_dict = {'Bab': []}

    num_logos = 15  # Sesuaikan dengan jumlah logo

    for i in range(1, num_logos + 1):
        data_dict[f'Logo {i}'] = []

    for i in range(1, 16):
        data_dict[f'Subjudul {i}'] = []

    for i in range(1, 16):
        data_dict[f'Opsional {i}'] = []

    i = 1
    while True:
        # Meminta input dari pengguna untuk subjudul, Subjudul, dan Opsional
        subjudul, Subjudul, Opsional = validate_length("", [[] for _ in range(15)])  # Menyesuaikan dengan perubahan dalam validate_length
        Subjudul = validate_Subjudul(Subjudul, i)
        Opsional = validate_Opsional(Opsional, i)

        # Memecah judul menjadi bagian-bagian
        subjudul_sections = split_title_into_sections(subjudul)

        # Menambahkan data ke dalam DataFrame
        data_dict['Bab'].append(bab)
        for j in range(1, num_logos + 1):
            logo_input = input(f"Masukkan Keterangan Baris {i} \n untuk Subjudul mulai dari yang ke 2 \n yang ke 1 sebagai Keterangan BAB  {j}: ").strip()
            data_dict[f'Logo {j}'].append(logo_input)

        for j in range(15):
            data_dict[f'Subjudul {j + 1}'].append(Subjudul[j])
            data_dict[f'Opsional {j + 1}'].append(Opsional[j])

        # Mengecek apakah pengguna ingin melanjutkan atau tidak
        lanjut = input("Apakah ingin menambahkan subjudul lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

        i += 1

    # Ensure all lists have the same length
    max_len = max(len(value) for value in data_dict.values())
    for key, value in data_dict.items():
        data_dict[key] += [''] * (max_len - len(value))

    # Membuat DataFrame dari input
    df = pd.DataFrame(data_dict)

    # Menyimpan DataFrame ke file Excel
    with pd.ExcelWriter('input_data.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

if __name__ == "__main__":
    bootstrap()
