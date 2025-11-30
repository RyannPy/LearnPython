def analisisangka():
  print("========== Program Analisis Angka ===========")
  x = int(input("Berapa banyak angkanya?:"))
  angka = []
  
  for i in range(1, x+1):
    y = int(input(f"Masukkan angka ke-{i}: "))
    angka.append(y)
  
  print("============ Hasil =============")
  print("Semua angka : ", angka)
  print("Jumlah angka ganjil : ", len([a for a in angka if a % 2 != 0]))
  print("Jumlah angka genap : ", len([a for a in angka if a % 2 == 0]))
  print("Total semua angka : ", sum(angka))
  if len(angka) > 0:
    print("Rata-rata : ", (sum(angka)/len(angka)))
  else:
      print("Input kosong!")
analisisangka()
  