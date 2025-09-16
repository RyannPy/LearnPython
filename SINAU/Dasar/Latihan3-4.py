def luas_lingkaran(r):
    return 3.14 * r * r

def konversi_suhu(c):
    return (c * 9/5) + 32

def hitung_faktorial(n):
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    return hasil

def menu():
    while True:
        print("\n===== Program Multifungsi =====")
        print("1. Hitung luas lingkaran")
        print("2. Konversi suhu Celcius ke Fahrenheit")
        print("3. Hitung faktorial")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            r = float(input("Masukkan jari-jari: "))
            print("Luas lingkaran:", luas_lingkaran(r))
        elif pilihan == "2":
            c = float(input("Masukkan suhu (C): "))
            print("Hasil konversi:", konversi_suhu(c), "F")
        elif pilihan == "3":
            n = int(input("Masukkan angka: "))
            print("Faktorial:", hitung_faktorial(n))
        elif pilihan == "4":
            print("Terima kasih sudah menggunakan program ini 💖")
            break
        else:
            print("Pilihan tidak valid!")

menu()