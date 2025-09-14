import random
min_val = 0
max_val = 20
while True: 
  print("Prediksi Skor?")
  tim1 = input("Siapa tim Kandang?:")
  rankingtim1 = input("Berapa peringkatnya? (angka):")
  tim2 = input("Siapa tim Tandang?:")
  rangkingtim2 = input("Berapa peringkatnya? (angka):")
  
  probabilitas_tim1_menang = 0.6
  probabilitas_tim2_menang = 1 - probabilitas_tim1_menang

  selisih_peringkat = abs(int(rankingtim1) - int(rangkingtim2))
  probabilitas_tim1_menang += selisih_peringkat * 0.01
  probabilitas_tim1_menang = min(probabilitas_tim1_menang, 0.95)
  probabilitas_tim2_menang = 1 - probabilitas_tim1_menang

  if random.random() < probabilitas_tim1_menang:
     skortim1 = random.randint(selisih_peringkat, max_val)
     skortim2 = random.randint(min_val, max_val - selisih_peringkat)
  else:
     skortim1 = random.randint(min_val, max_val - selisih_peringkat)
     skortim2 = random.randint(selisih_peringkat, max_val)

  hasil = f"{tim1} {skortim1} - {skortim2} {tim2}"

  print(hasil)

  ulang = input("Mau ulang? (y/n):")
  if ulang != "y" :
    print("Selesai!")
    break
