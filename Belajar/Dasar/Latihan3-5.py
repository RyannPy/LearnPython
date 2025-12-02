import statistics

def ratarata(a):
  return sum(a)/len(a)
  
def terbesar(x):
  return max(x)

def terkecil(n):
  return min(n)

def median(data):
  return statistics.median(data)
  
def modus(data):
  return statistics.modus(data)
  
def stdev(data):
  return statistics.stdev(data)
  
def menu():
  while True:
    print(" ======= Program Analisis Angka ======= ")
    print(" 1. Hitung rata-rata ")
    print(" 2. Angka terbesar ")
    print(" 3. Angka terkecil ")
    print(" 4. Median  ")
    print(" 5. Modus ")
    print(" 6. Standar Deviasi ")
    print(" 7. Udah ")
    pilihan = input("Pilih menu: ")
    try:
      if pilihan in ["1", "2", "3", "4", "5", "6"]:
        data = [float(x) for x in input("Masukkan angka, pisahkan dengan spasi: ").split()]
        if pilihan == "1":
          print("Rata-rata", ratarata(data))
        elif pilihan == "2":
          print("Angka terbesar: ", terbesar(data))
        elif pilihan == "3":
          print("Angka terkecil: ", terkecil(data))
        elif pilihan == "4":
          print("Median: ", median(data))
        elif pilihan == "5":
          print("Modus: ", modus(data))
        elif pilihan == "6":
          print("Standar Deviasi: ", stdev(data))
      
      elif pilihan == "4":
        print("Thanks bro")
        break
      else:
        print("Pilihan gak valid!")
    except Exception as e:
      print("Error: ", e)
    
      
menu()