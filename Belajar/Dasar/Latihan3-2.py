def analisisnilai():
  print("======== Program Analisis Nilai ========= ")
  x = int(input("Berapa banyak nilainya?:"))
  nilai = []
  
  for i in range(1, x+1):
    y = float(input(f"Masukkan nilai ke-{i} : "))
    nilai.append(y)
  
      
  print("========= Hasil =========")
  print("Semua nilai: ", nilai)
  print("Rata-rata :", sum(nilai)/len(nilai))
  print("Nilai tertinggi: ", max(nilai))
  print("Nilai terendah: ", min(nilai))
  print("Lulus : ", len([n for n in nilai if n >= 75 ]), "siswa.")
  print("Tidak Lulus : ", len([n for n in nilai if n < 75]), "siswa.")
analisisnilai()



    