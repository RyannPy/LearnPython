from datetime import date

# Tanggal hari ini
hari_ini = date(2025, 1, 13)

while True:
    # Input tanggal lahir
    try:
        tgl_lahir = int(input("Masukkan tanggal lahir Anda (1-31): "))
        bln_lahir = int(input("Masukkan bulan lahir Anda (1-12): "))
        thn_lahir = int(input("Masukkan tahun lahir Anda: "))
        
        # Buat objek tanggal lahir
        tanggal_lahir = date(thn_lahir, bln_lahir, tgl_lahir)
        
        # Hitung perbedaan
        delta = hari_ini - tanggal_lahir
        tahun = delta.days // 365  # Perkirakan jumlah tahun
        sisa_hari = delta.days % 365
        
        # Hitung bulan dan hari
        bulan = sisa_hari // 30  # Perkiraan bulan
        hari = sisa_hari % 30
        
        # Output usia
        print(f"Usia Anda adalah {tahun} tahun, {bulan} bulan, dan {hari} hari.")
        
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan tanggal dengan format yang benar.")
    
    # Opsi untuk keluar dari loop
    lanjut = input("Apakah Anda ingin mengulang? (y/n): ").lower()
    if lanjut != 'y':
        print("Terima kasih!")
        break