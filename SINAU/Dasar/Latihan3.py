#KASUS1
def hitung(a, b):
  return a * (1 - (b/100))

print("Harga akhir :", hitung(100000, 10))

print("=====================================================")

#KASUS2
def ratarata(a, b, c):
  return (a + b + c)/3
  
print("Rata-rata: ", ratarata(80, 90, 100))

def ratarata(nilai):
    return sum(nilai) / len(nilai)

print("Rata-rata:", ratarata([80, 90, 100]))
print("Rata-rata:", ratarata([70, 85, 95, 100]))
print("Rata-rata:", ratarata([60, 75]))

print("=====================================================")

#KASUS 3
def ratarata2(nilai):
  return sum(nilai)/len(nilai)
  
print("Rata-rata:", ratarata2([80, 90, 75, 100, 85, 70]))

#KASUS4
def rataratainput():
  n = int(input("Berapa banyak nilainya?:"))
  nilai = []
  
  for i in range(n):
    y = float(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(y)
    
  return sum(nilai)/len(nilai)
print("Rata-ratanya: ", rataratainput())

