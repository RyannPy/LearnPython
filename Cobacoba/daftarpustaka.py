namadepan = input("Nama Depan Penulis (tuliskan semua nama, kecuali satu kata nama belakang:")
namabelakang = input("Nama Belakang Penulis (hanya satu kata):")
tahun = input("Tahun Publish:")
judul = input("Judul Artikelnya?:")
link = input("Link Webnya:")
tanggalakses = input("Kapan kamu akses? (formatnya tanggal bulan tahun, contoh 12 Januari 2009:")
waktuakses = input("Jam berapa kamu akses? (format angka jam, contoh 06.30):")


daftarpustaka = f'{namabelakang}, {namadepan}. {tahun}. "{judul}". {link} (diakses tanggal {tanggalakses}, pukul {waktuakses}.'

print(daftarpustaka)
