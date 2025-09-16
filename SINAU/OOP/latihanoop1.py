class hero:
  def __init__ (self, name, damage, health):
    self.name = name
    self.damage = damage
    self.health = health
  def tampilkaninfo(self):
    print(f'Nama: {self.name}, Damage: {self.damage}, Health: {self.health}') 

hero1 = hero("Fanny", 50, 1500)
hero2 = hero("Alucard", 40, 2000)
hero3 = hero("Belerick", 20, 5000)

daftarhero = [hero1, hero2, hero3]
for hero in daftarhero:
  hero.tampilkaninfo()
