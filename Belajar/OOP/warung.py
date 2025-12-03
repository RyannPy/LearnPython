menuMakan = {"Mie Ayam" : 15000, "Sate Ayam" : 10000, "Ayam Goreng" : 7000, "Ayam Bakar" : 9000, "Bakso" : 13000, "Mie Bakso" : 17000}
menuMinum = {
  "Es Teh" : 3000, "Es Jeruk" : 4000, "Es Teler" : 6000, "Es Sirup" : 3000, "Teh Hangat" : 3000
}

def tampilkanMenu():
  i = 1
  print(" === MAKANAN ===")
  for makanan, harga in menuMakan.items():
    print(i, ". ", makanan, " = ", harga)
    i += 1
  i = 1
  print(" === MINUMAN ===")
  for minuman, harga in menuMinum.items():
    print(i, ". ", minuman, " = ", harga)
    i += 1
    
class Transaksi:
  def __init__ (self, namamenu, harga, jumlah):
    self.namamenu = namamenu
    self.harga = harga
    self.jumlah = jumlah
    
pesanan1 = Transaksi("Ayam Goreng", 15000, 1)