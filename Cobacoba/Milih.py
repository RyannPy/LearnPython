while True:
    print("Selamat Datang")
    print("Manakah yang ingin anda mainkan?")
    print("1. Minecraft")
    print("2. Mobile Legend")
    print("3. PUBG Mobile")
    print("4. Keluar")

    angka = int(input("Masukkan angka: "))

    if angka == 1:
        print("Minecraft")
    elif angka == 2:
        print("Mobile Legend")
    elif angka == 3:
        print("PUBG Mobile")
    elif angka == 4:
        print("Terima kasih, sampai jumpa!")
        break  # Menghentikan loop
    else:
        print("Pilihan tidak valid, coba lagi.")