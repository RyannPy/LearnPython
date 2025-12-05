class hero:
  def __init__ (self, name, damage, defense, health):
    self.name = name
    self.damage = damage
    self.defense = defense
    self.health = health
    
  def serang(self, lawan):
    print(self.name + " menyerang " + lawan.name)
    lawan.diserang(self, self.damage)
    
      
  def diserang(self, lawan, damage_lawan):
    print(self.name + " diserang " + lawan.name)
    damage_diterima = damage_lawan - self.defense
    print("Total damage: " + str(abs(damage_diterima)))
    self.health -= abs(damage_diterima)
    print("Sisa health " + self.name + " : " + str(self.health))
    
Fanny = hero("Fanny", 80, 30, 100)
Alucard = hero("Alucard", 40, 50, 200)
Belerick = hero("Belerick", 20, 100, 500)

daftarhero = [Fanny, Alucard, Belerick]

Belerick.serang(Alucard)
print("="*20)
Fanny.serang(Alucard)
