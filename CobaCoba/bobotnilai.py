jumlah_bobot = int(input("Berapa banyak jenis pembobotan? "))

bobot = []
jumlahPerJenis = {}  
skorAkhir = 0

for jenis in range(jumlah_bobot):
    namaJenis = input(f"Jenis ke-{jenis+1}: ")
    bobotJenis = float(input(f"{namaJenis} bobotnya berapa? (desimal): "))
    skornya = int(input(f"{namaJenis} skornya berapa?: "))
    
    skorPerJenis = skornya * bobotJenis
    jumlahPerJenis[namaJenis] = skorPerJenis
    skorAkhir += skorPerJenis
    bobot.append(namaJenis)

print(f"\nSkor Akhirnya adalah: {skorAkhir}")
print("\nRincian nilai per jenis:")
for nama, skor in jumlahPerJenis.items():
    print(f"- {nama}: {skor}")