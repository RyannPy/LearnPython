print ("Konversi Suhu!")
suhuHasil = None
suhuInput = int(input("Masukkan suhu pertama:"))
print ("Pilih jenis suhu:")
print ("1. Celcius")
print ("2. Fahrenheit")
print ("3. Kelvin")
print ("4. Reamur")
jenisSuhuInput = int(input("Pilihan (1/2/3/4) : "))

print ("Mau diubah jadi apa?")
print ("1. Celcius")
print ("2. Fahrenheit")
print ("3. Kelvin")
print ("4. Reamur")
jenisSuhuHasil = int(input("Pilihan (1/2/3/4): "))

suhuHasil = None
if jenisSuhuInput == "1" and jenisSuhuHasil == "2" :
  suhuHasil = (suhuInput * 1.8) + 32
elif jenisSuhuInput == "1" and jenisSuhuHasil == "3" :
  suhuHasil = suhuInput + 273
elif jenisSuhuInput == "1" and jenisSuhuHasil == "4" :
  suhuHasil = suhuInput * 0.8
elif jenisSuhuInput == "2" and jenisSuhuHasil == "1" :
  suhuHasil = 5 / 9 * (suhuInput - 32)
elif jenisSuhuInput == "2" and jenisSuhuHasil == "3" :
  suhuHasil = None
elif jenisSuhuInput == "2" and jenisSuhuHasil == "4" :
  suhuHasil = 4 / 9 * (suhuInput - 32)
elif jenisSuhuInput == "3" and jenisSuhuHasil == "1" :
  suhuHasil = suhuInput - 273
elif jenisSuhuInput == "3" and jenisSuhuHasil == "2" :
  suhuHasil = None
elif jenisSuhuInput == "3" and jenisSuhuHasil == "4" :
  suhuHasil = 0.8 * (suhuInput - 273)
elif jenisSuhuInput == "4" and jenisSuhuHasil == "1" :
  suhuHasil = 1.25 * suhuInput
elif jenisSuhuInput == "4" and jenisSuhuHasil == "2" :
  suhuHasil = (2.25 * suhuInput) + 32
elif jenisSuhuInput == "4" and jenisSuhuHasil == "3" :
  suhuHasil = (1.25 * suhuInput) + 273
else :
  suhuHasil = suhuInput
  
print (f"Jadi, hasil konversinya = {suhuHasil}")