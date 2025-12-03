class Siswa:
    def __init__(self, nama, nilai):
        # simpan nama dan nilai ke atribut
        self.nama = nama
        self.nilai = nilai
        pass
    
    def tampilkan_info(self):
        # print nama dan nilai
        print(f'Nama: {self.nama}, Nilai: {self.nilai}')
        pass
    
    def rata_rata(self):
        # hitung rata-rata dari list nilai
        if len(self.nilai) > 0:
          return sum(self.nilai)/len(self.nilai)
        else:
          return 0
        pass


# ==== Main Program ====
# bikin object siswa, misalnya Ryan punya nilai [80, 90, 85]
s1 = Siswa("Ryan", [80, 90, 85])
s2 = Siswa("Dina", [75, 95, 70])
s3 = Siswa("Sora😘", [100, 100, 100])


daftar_siswa = [s1, s2, s3]

for siswa in daftar_siswa:
  siswa.tampilkan_info()
  print("Rata-rata: ", siswa.rata_rata())
  print("========")

tertinggi = 0
siswa_terbaik = None

for siswa in daftar_siswa:
  rata_rata_siswa = siswa.rata_rata()
  if rata_rata_siswa > tertinggi:
    tertinggi = rata_rata_siswa
    siswa_terbaik = siswa
    
print("====")
print("Siswa dengan rata-rata tertinggi adalah: ")
siswa_terbaik.tampilkan_info()
print("Rata-rata tertinggi: ", {tertinggi})

