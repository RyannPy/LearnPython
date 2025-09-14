import sqlite3

# Hubungkan ke database
conn = sqlite3.connect("keuangan.db")
cursor = conn.cursor()

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS keuangan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kategori TEXT,
    nominal REAL,
    jenis TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS saldo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nominal REAL
)
""")
conn.commit()

# Variabel global untuk saldo dan catatan pemasukan/pengeluaran
saldo_awal = 0
total_pemasukan = 0
total_pengeluaran = 0

def ambil_saldo():
    global saldo_awal
    # Ambil saldo dari database jika ada
    cursor.execute("SELECT nominal FROM saldo ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        saldo_awal = result[0]
    else:
        saldo_awal = 0  # Jika belum ada saldo, set saldo awal menjadi 0

def tampilkan_menu():
    print("MENGHITUNG DAN MENCATAT KEUANGANMU!")
    print("=====================================")
    print("Pilih menu:")
    print("1. Edit saldo awal")
    print("2. Input pemasukan")
    print("3. Input pengeluaran")
    print("4. Info saldo dan rekap")
    print("5. Keluar")
    print("6. Reset database")

def edit_saldo_awal():
    global saldo_awal
    print("\nKuy masukkin nominal saldo awal kalian (hanya angka):")
    try:
        saldo_awal = float(input("> "))
        # Simpan saldo ke database
        cursor.execute("DELETE FROM saldo")  # Hapus saldo lama (jika ada)
        cursor.execute("INSERT INTO saldo (nominal) VALUES (?)", (saldo_awal,))
        conn.commit()
        print(f"Saldo awal berhasil diinput: {saldo_awal}")
    except ValueError:
        print("Input tidak valid, masukkan angka saja ya!")
    print("\n=====================================")

def input_pemasukan():
    global saldo_awal, total_pemasukan
    print("Pilih kategori pemasukan:")
    print("1. Uang saku")
    print("2. Pendapatan lain")
    while True:
        kategori = input("Masukkan nomor kategori (1/2): ")
        if kategori in ["1", "2"]:
            kategori_nama = "Uang saku" if kategori == "1" else "Pendapatan lain"
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
    
    while True:
        try:
            nominal = float(input("Berapa jumlahnya gan? : "))
            saldo_awal += nominal
            total_pemasukan += nominal
            # Simpan pemasukan ke database
            cursor.execute("INSERT INTO keuangan (kategori, nominal, jenis) VALUES (?, ?, ?)", 
                           (kategori_nama, nominal, 'Pemasukan'))
            cursor.execute("UPDATE saldo SET nominal = ? WHERE id = (SELECT MAX(id) FROM saldo)", (saldo_awal,))
            conn.commit()
            print(f"Pemasukan kategori '{kategori_nama}' sebesar {nominal} berhasil dicatat.")
            print(f"Total Saldo Saat Ini: {saldo_awal}")
            break
        except ValueError:
            print("Masukkan hanya angka, ya! Coba lagi...")
    
    print("=====================================")

def input_pengeluaran():
    global saldo_awal, total_pengeluaran
    print("Pilih kategori pengeluaran:")
    print("1. Kendaraan")
    print("2. Sekolah")
    print("3. Komunikasi")
    print("4. Pengeluaran lain")
    while True:
        kategori = input("Masukkan nomor kategori (1/2/3/4): ")
        if kategori in ["1", "2", "3", "4"]:
            kategori_nama = (
                "Kendaraan" if kategori == "1" else
                "Sekolah" if kategori == "2" else
                "Komunikasi" if kategori == "3" else
                "Pengeluaran lain"
            )
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")
    
    while True:
        try:
            nominal = float(input("Berapa jumlahnya gan? : "))
            saldo_awal -= nominal
            total_pengeluaran += nominal
            # Simpan pengeluaran ke database
            cursor.execute("INSERT INTO keuangan (kategori, nominal, jenis) VALUES (?, ?, ?)", 
                           (kategori_nama, nominal, 'Pengeluaran'))
            cursor.execute("UPDATE saldo SET nominal = ? WHERE id = (SELECT MAX(id) FROM saldo)", (saldo_awal,))
            conn.commit()
            print(f"Pengeluaran kategori '{kategori_nama}' sebesar {nominal} berhasil dicatat.")
            print(f"Total Saldo Saat Ini: {saldo_awal}")
            break
        except ValueError:
            print("Masukkan hanya angka, ya! Coba lagi...")
    
    print("=====================================")

def info_saldo_rekap():
    global total_pemasukan, total_pengeluaran
    print("Pilih informasi yang ingin dilihat:")
    print("1. Info saldo saat ini")
    print("2. Total pemasukan")
    print("3. Total pengeluaran")
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == "1":
        print(f"Saldo kamu saat ini: {saldo_awal}")
    elif pilihan == "2":
        print(f"Pemasukan kamu: {total_pemasukan}")
    elif pilihan == "3":
        print(f"Pengeluaran kamu: {total_pengeluaran}")
    else:
        print("Pilihan tidak valid.")
    
    print("=====================================")

def keluar():
    print("Udah kelar gan? Oke makasih!")
    print("=====================================")

def reset_database():
    cursor.execute("DELETE FROM saldo")  # Hapus data di tabel saldo
    cursor.execute("DELETE FROM keuangan")  # Hapus data di tabel keuangan
    conn.commit()
    print("Database telah direset.")
    print("=====================================")

# Memanggil menu
ambil_saldo()  # Ambil saldo dari database ketika program dijalankan

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        edit_saldo_awal()
    elif pilihan == "2":
        input_pemasukan()
    elif pilihan == "3":
        input_pengeluaran()
    elif pilihan == "4":
        info_saldo_rekap()
    elif pilihan == "5":
        keluar()
        break
    elif pilihan == "6":
        reset_database()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")