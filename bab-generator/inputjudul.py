import os
import pandas as pd

def validate_length(judul, skripsi):
    while len(judul) != len(skripsi[0]):
        print("Panjang judul tulisan skripsi dan salah satu dari tulisan opsional harus sama.")
        judul = input("Masukkan Bagan judul pada isi ex: \n A. Latar Belakang: ").strip()

    # Menerima input untuk setiap opsional
    opsional = []
    for i in range(15):  # Set to 15 inputs for opsional
        prompt = f"Opsional berupa isi keterangan misal: ex: \n Berupa isi Rumusan Masalah \n1. Apa yang dixxx...? 1 \n atau materi dst.. {i + 1}: "
        input_opsional = input(prompt).strip()
        opsional.append(input_opsional)

    return judul, opsional

def validate_subjudul(judul, i):
    while not judul:
        print(f"Subjudul {i} tidak boleh kosong.")
        judul = input(f"Masukkan Subjudul {i} misal' A. Latar Belakang : ").strip()
    return judul

def bootstrap():
    # Meminta input dari pengguna
    bab = input("Masukkan BAB misal' BAB II PEMBAHASAN: ").strip()

    # Membuat DataFrame kosong
    data_dict = {'Bab': [bab]}

    for j in range(15):
        logo_input = input(f"Masukkan Keterangan Baris 1 untuk Logo ke {j+1}: ").strip()
        data_dict[f'Logo {j + 1}'] = [logo_input]  # Set up Logo columns

        # Menerima input untuk setiap opsional
        opsional = []
        for i in range(15):  # Set to 15 inputs for opsional
            prompt = f"Opsional berupa isi keterangan misal: ex: \n Berupa isi Rumusan Masalah \n1. Apa yang dixxx...? 1 \n atau materi dst.. {i + 1}: "
            input_opsional = input(prompt).strip()
            opsional.append(input_opsional)
        
        data_dict[f'Opsional {j + 1}'] = opsional  # Set up 15 Opsional columns

        subjudul = validate_subjudul('', j + 1)
        data_dict[f'Subjudul {j + 1}'] = [subjudul]  # Set up 15 Subjudul columns

    # Membuat DataFrame dari input
    df = pd.DataFrame(data_dict)

    # Menyimpan DataFrame ke file Excel
    with pd.ExcelWriter('input_data.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

if __name__ == "__main__":
    bootstrap()
