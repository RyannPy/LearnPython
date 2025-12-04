import random
import time, sys


class Hero:
  def __init__(self, name, health, defense, skills):
    self.name = name
    self.hp = health
    self.deff = defense
    self.skills = skills
    
    
  #TAMPILKAN INFO
  def tampilkanInfo(self):
    name = self.name
    hp = self.hp
    deff = self.deff
    skill1name, skill1damage = self.skills[0]
    skill2name, skill2damage = self.skills[1]
    skill3name, skill3damage = self.skills[2]
    print("="*30)
    print(f'\n\nNama: {name} \n HP: {hp} \n Def : {deff}')
    print(f'\n\tData damage: \n\t Skill 1 ({skill1name}) : {skill1damage}\n\t Skill 2 ({skill2name}) : {skill2damage}\n\t Skill 3 ({skill3name}) : {skill3damage} ')
    print("="*30)
  
  def pakaiSkill(self, nomorskill):
    index = nomorskill - 1
    if 0 <= index <= len(self.skills):
      skillname, skilldamage = self.skills[index]
      
      print("Menggunakan Skill", end="")
      for i in range(3):   # animasi titik titik
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
        
      print(f'{self.name} menggunakan skill {skillname}')
      print(f'\tTOTAL DAMAGE : {skilldamage}')
      return skilldamage
    else:
      print("Skill not found!")
    
  def serang(self, lawan, nomorskill):
    
    print("Menyerang", end="")
    for i in range(3):   # animasi titik titik
        time.sleep(1)
        print(".", end="")
        sys.stdout.flush()
        
    print(f'{self.name} menyerang {lawan.name}')
    damage = self.pakaiSkill(nomorskill)
    
    if lawan.deff >= 0:
      lawan.deff -= damage
      print(f'HP {lawan.name} tersisa: {lawan.hp}')
      print("="*30)
    elif lawan.deff <= 0:
      lawan.hp = max(0, lawan.hp - damage)
      print(f'HP {lawan.name} tersisa: {lawan.hp}')
      print("="*30)

      
      
Fanny = Hero("Fanny", 100, 30, [("Steel Cable", 10), ("Tornado Strike", 15), ("Cut Throat", 25)])
Alucard = Hero("Alucard", 120, 50, [("Groundsplitter", 5), ("Whirling Smash", 10), ("Fission Waves", 15)])
Claude = Hero("Claude", 80, 10, [("Art of Thievery", 15), ("Battle Mirror Image", 5), ("Blazing Duet", 40)])

daftarHero = [Fanny, Alucard, Claude]

def pilihHero():
  print("\nCHOOSE YOUR HERO!")
  for i, hero in enumerate(daftarHero, 1):
    print(f'\t{i}. {hero.name}')
  pilihan = int(input("\tPilihanmu:"))
  mainHero = daftarHero[pilihan-1]
  mainHero.tampilkanInfo()
  daftarLawan = [h for h in daftarHero if h != mainHero]
  return mainHero, daftarLawan

def pilihLawan(mainHero, daftarLawan):
  
  print("Melanjutkan", end="")
  for i in range(3):   # animasi titik titik
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
    
  print("\nCHOOSE YOUR ENEMY!")
  for i, hero in enumerate(daftarLawan, 1):
    print(f'\t{i}. {hero.name}')
  pilihan = int(input("\tPilihanmu: "))
  mainLawan = daftarLawan[pilihan-1]
  mainLawan.tampilkanInfo()
  return mainLawan
  
def battle(mainHero, mainLawan):
  print("="*30)
  
  print("Bersiap untuk bertarung", end="")
  for i in range(3):   # animasi titik titik
    time.sleep(1)
    print(".", end="")
    sys.stdout.flush()
        
  print(f'\nGiliranmu!{mainHero.name}!')
  pilihanskill = int(input("Skill ke-"))
  mainHero.serang(mainLawan, pilihanskill)
  
  #PILIH ANGKA RANDOM SKILL MUSUH
  skillLawan = random.randint(1, 3)
  
  if mainLawan.hp > 0:
    mainLawan.serang(mainHero, skillLawan)
    if mainHero.hp > 0:
      battle(mainHero, mainLawan)
    elif mainHero.hp == 0:
      print(f'\tYOU LOSE! {mainHero.name} telah MATI')
  elif mainLawan.hp == 0:
    print(f"YOU WIN!, {mainLawan.name} telah mati.")
    
    
def main():
  mainHero, daftarLawan = pilihHero()
  mainLawan = pilihLawan(mainHero, daftarLawan)
  battle(mainHero, mainLawan)
  
main()
  