#KASUS 1
angka = [80, 75, 90, 85, 70]
average = sum(angka)/len(angka)
print(f"Rata ratanya : {average}")

print("===================================================")
#KASUS 2
kata = "Saya suka belajar Python"
jumlahKata = len(kata.split())
print(f"Jumlah katanya: {jumlahKata}")

print("===================================================")

#KASUS 3
nilai = int(input("Masukkan nilai kamu :"))

if nilai >= 90:
  grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "D"
    
print(f"Grade kamu : {grade}")

print("===================================================")


#KASUS 4
angka2 = [2, 5, 8, 11, 14, 17]

for x in angka2:
  if x % 2 == 0:
   print(x)
   
print("===================================================")


#KASUS 5
nilai_siswa = [80, 65, 90, 75, 88, 92, 70, 60]
jumlah_lulus = 0
for y in nilai_siswa:
  if y >= 75 :
    print(f"yang lebih dari 75 : {y}")
    jumlah_lulus += 1

print(f"siswa yang lulus sebanyak : {jumlah_lulus} siswa")

average2 = sum(nilai_siswa)/len(nilai_siswa)
print (f"Rata rata nilai siswa = {average2}")

print("===================================================")


#KASUS 6
harga_barang = [12000, 5000, 30000, 15000, 8000, 20000, 4500]

for harga in harga_barang:
  if harga > 10000:
    print(f"lebih dari 10k: {harga}")
    
totalharga = sum(harga_barang)
print (f"Total harga: {totalharga}")

dibawah10k = 0
for harga2 in harga_barang:
  if harga2 < 10000:
    dibawah10k += 1
print(f"Banyak barang harganya dibawah 10k : {dibawah10k}")

harga_barang = [12000, 5000, 30000, 15000, 8000, 20000, 4500]

# 1. Cetak harga > 10k
lebih_10k = [h for h in harga_barang if h > 10000]
print("Lebih dari 10k:", lebih_10k)

# 2. Total harga
print("Total harga:", sum(harga_barang))

# 3. Barang < 10k
dibawah_10k = len([h for h in harga_barang if h < 10000])
print("Jumlah barang di bawah 10k:", dibawah_10k)