def italic(text):
    return f"\033[3m{text}\033[0m"

# jenis daftar pustaka
print("Pilih jenis daftar pustaka yang ingin dibuat:")
print("1. Buku")
print("2. Website")
print("3. Jurnal")
pilihan = input("Masukkan pilihan (1/2/3): ").strip()

# jumlah penulis
print("\nJumlah penulis:")
print("1. Satu penulis")
print("2. Dua penulis")
print("3. Lebih dari dua penulis")
jumlah_penulis = input("Masukkan pilihan (1/2/3): ").strip()

# input nama penulis berdasarkan jumlahnya
if jumlah_penulis == "1":  
    lebih_dari_satu = input("Apakah penulis punya nama lebih dari satu kata? (ya/tidak): ").strip().lower()
    
    if lebih_dari_satu == "ya":
        namabelakang = input("Nama Belakang Penulis: ").strip()
        namadepan = input("Nama Depan Penulis: ").strip()
        penulis = f"{namabelakang}, {namadepan}"
    else:
        penulis = input("Nama Penulis (hanya satu kata): ").strip()

elif jumlah_penulis == "2":  
    lebih_dari_satu1 = input("Apakah penulis pertama punya nama lebih dari satu kata? (ya/tidak): ").strip().lower()
    
    if lebih_dari_satu1 == "ya":
        namabelakang1 = input("Nama Belakang Penulis Pertama: ").strip()
        namadepan1 = input("Nama Depan Penulis Pertama: ").strip()
        penulis1 = f"{namabelakang1}, {namadepan1}"
    else:
        penulis1 = input("Nama Penulis Pertama (hanya satu kata): ").strip()

    penulis2 = input("Nama Lengkap Penulis Kedua: ").strip()
    penulis = f"{penulis1} dan {penulis2}"

elif jumlah_penulis == "3":  
    lebih_dari_satu1 = input("Apakah penulis pertama punya nama lebih dari satu kata? (ya/tidak): ").strip().lower()
    
    if lebih_dari_satu1 == "ya":
        namabelakang1 = input("Nama Belakang Penulis Pertama: ").strip()
        namadepan1 = input("Nama Depan Penulis Pertama: ").strip()
        penulis = f"{namabelakang1}, {namadepan1}. dkk."
    else:
        penulis = input("Nama Penulis Pertama (hanya satu kata): ").strip() + ". dkk."

else:
    print("Pilihan jumlah penulis tidak valid.")
    exit()

# proses berdasarkan pilihan jenis referensi
if pilihan == "1":  # Buku
    tahun = input("Tahun Terbit: ").strip()
    judul = input("Judul Buku: ").strip()
    kota = input("Kota Penerbit: ").strip()
    penerbit = input("Penerbit: ").strip()

    daftarpustaka = f"{penulis}. {tahun}. {italic(judul)}. {kota}: {penerbit}."

elif pilihan == "2":  # Website
    tahun = input("Tahun Publikasi: ").strip()
    judul = input("Judul Artikel: ").strip()
    link = input("URL: ").strip()
    tanggalakses = input("Tanggal Akses (format: 12 Januari 2025): ").strip()
    waktuakses = input("Waktu Akses (format: 06.30): ").strip()

    daftarpustaka = f"{penulis}. {tahun}. \"{judul}\". {link} (diakses tanggal {tanggalakses}, pukul {waktuakses})."

elif pilihan == "3":  # Jurnal
    tahun = input("Tahun Publikasi: ").strip()
    judul = input("Judul Artikel: ").strip()
    namajurnal = input("Nama Jurnal: ").strip()
    volume = input("Volume Jurnal: ").strip()
    nomor = input("Nomor Jurnal: ").strip()
    halaman = input("Halaman: ").strip()

    daftarpustaka = f"{penulis}. {tahun}. \"{judul}\". {italic(namajurnal)}, {volume}({nomor}): {halaman}."

else:
    daftarpustaka = "Pilihan tidak valid."

# hasil
print("\nDaftar Pustaka:")
print(daftarpustaka)