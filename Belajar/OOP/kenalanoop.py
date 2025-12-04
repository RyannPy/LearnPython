class hero:
  def __init__ (self, name, damage, health):
    self.name = name
    self.damage = damage
    self.health = health
  def tampilkaninfo(self):
    print(f'Nama: {self.name}, Damage: {self.damage}, Health: {self.health}') 
    
  # method tanpa return, tanpa argumen
  def siapa(self):
    print("Hello, my name is " + self.name)
  
  # method with argumen
  def healthUp(self, up):
    self.health += up
  
  # method with return
  def getHealth(self):
    return self.health
  
hero1 = hero("Fanny", 50, 100)
hero2 = hero("Alucard", 40, 200)
hero3 = hero("Belerick", 20, 500)

daftarhero = [hero1, hero2, hero3]

hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())

