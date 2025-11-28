#KASUS1
daftarminuman = [
  {"nama": "teh", "harga": 4000},
  {"nama": "kopi", "harga": 6000},
  {"nama": "jus", "harga": 10000},
  {"nama": "soda", "harga": 8000},
  {"nama": "air", "harga": 3000}
]

#1. 1 Teh 1 Kopi 3 Jus 1 Soda 4 Air Mineral
harga_total = daftarminuman[0]['harga']*2 + daftarminuman[1]['harga'] + daftarminuman[2]['harga']*3 + daftarminuman[3]['harga'] + daftarminuman[4]['harga']*4
print(f"Harga total adalah: {harga_total}")

#2. Harga termahal dan termurah
mahal = max(daftarminuman, key=lambda x: x['harga'])
murah = min(daftarminuman, key=lambda x: x['harga'])
print(f"harga termahal : {mahal['nama']} dengan harga {mahal['harga']}")
print(f"harga termurah : {murah['nama']} dengan harga {murah['harga']}")

#3. Berapa jenis minuman harganya >5000
diatas5k = 0
for minuman in daftarminuman :
  if minuman['harga'] > 5000:
    diatas5k += 1
    
print(f"Produk diatas 5k : {diatas5k}")

print("=====================================================")

#KASUS2

perpustakaan = [
    {"judul": "Matematika Dasar", "halaman": 120},
    {"judul": "Astronomi", "halaman": 200},
    {"judul": "Pemrograman Python", "halaman": 150},
    {"judul": "Sejarah Indonesia", "halaman": 180}
]

#1. Buku dgn jumlah halaman paling sedikit
tipis = min(perpustakaan, key=lambda x: x['halaman'])
print(f"Buku paling tipis : {tipis['judul']} dengan {tipis['halaman']} halaman")
#2. Buku dgn jumlah halaman paling banyak
tebal = max(perpustakaan, key=lambda x: x['halaman'])
print(f"Buku paling tebal : {tebal['judul']} dengan {tebal['halaman']} halaman")
#3. Urutkan buku dari tipis ke tebal
tipisketebal = sorted(perpustakaan, key=lambda x: x['halaman'])
print(f"Urutannya dari tipis ke tebal : ")
for buku in tipisketebal:
  print(f"- {buku['judul']} ({buku['halaman']} halaman)")


print("=====================================================")

daftarmahasiswa = [
    {"nama": "Andi", "nilai": 85},
    {"nama": "Budi", "nilai": 72},
    {"nama": "Citra", "nilai": 90},
    {"nama": "Dewi", "nilai": 65},
    {"nama": "Eka", "nilai": 78}
]

# 1. Cari mahasiswa dengan nilai tertinggi
tertinggi = max(daftarmahasiswa, key=lambda x: x['nilai'])
print(f"Nilai tertinggi : {tertinggi['nama']} dengan nilai {tertinggi['nilai']}")
# 2. Cari mahasiswa dengan nilai terendah
terendah = min(daftarmahasiswa, key=lambda x: x['nilai'])
print(f"Nilai terendah : {terendah['nama']} dengan nilai {terendah['nilai']}")
# 3. Urutkan mahasiswa berdasarkan nilai (dari terendah ke tertinggi)
urutan = sorted(daftarmahasiswa, key=lambda x: x['nilai'])
print("Urutan nilai dari terendah ke tertinggi:")
for mahasiswa in urutan:
  print(f"- {mahasiswa['nama']} ({mahasiswa['nilai']})")
# 4. Tampilkan semua mahasiswa yang lulus (nilai >= 75)
print("Mahasiswa yang lulus :")
for mahasiswa in daftarmahasiswa:
  if mahasiswa['nilai'] >= 75:
    print(f"- {mahasiswa['nama']} ({mahasiswa['nilai']})")
# 5. Hitung rata-rata nilai seluruh mahasiswa
nilaiMahasiswa = [mahasiswa['nilai'] for mahasiswa in daftarmahasiswa]
print("Rata-rata nilai Mahasiswa :", sum(nilaiMahasiswa)/len(nilaiMahasiswa))