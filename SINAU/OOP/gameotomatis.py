import random
import time


class Hero:
  def __init__(self, name, defense, health, basicAttack, skills):
    self.name = name
    self.deff = defense
    self.hp = health
    self.damageBA = basicAttack
    self.skills = skills
    self.exp = 0
    self.level = 1
    
    # PAKAI SKILL
  def pake_skill(self, nomorskill):
    index =  nomorskill - 1
    if 0 <= index < len(self.skills):
      name, damage = self.skills[index]
      print(f'{self.name} menggunakan skill {name} | Total damage: {damage}')
      return damage
      # Jika skill gak valid
    else:
      print("Skill not found")
      
  def serang(self, lawan, jumlahserangan, nomorskill=None):
    print(f'{self.name} menyerang {lawan.name} ({jumlahserangan} kali)')
    # Jika pake skill
    if nomorskill is not None:
        damage = self.pake_skill(nomorskill) * jumlahserangan
    # Jika pake basic attack doang
    else:
        damage = self.damageBA * jumlahserangan
        print(f'Dengan Basic Attack | Total Damage: {damage}')
        
    # itung total damage, dikurangi defense sebelum mengurangi HP
    total_damage = max(0, damage - lawan.deff)
    lawan.hp = max(0, lawan.hp - total_damage)
    print(f'HP {lawan.name} tersisa: {lawan.hp}')
    
    # Lawan mati jika hp 0
    if lawan.hp == 0:
      print(f'{lawan.name} mati.')
    
  # tampilkan info sebelum milih
  def tampilkanInfo(self):
    name = self.name
    hp = self.hp
    deff = self.deff
    BAdamage = self.damageBA
    skill1name, skill1damage = self.skills[0]
    skill2name, skill2damage = self.skills[1]
    skill3name, skill3damage = self.skills[2]
    print("="*30)
    print(f'\n\nNama: {name} \n HP: {hp} \n Def : {deff}')
    print(f'\n\tData damage: \n\t Basic Attack: {BAdamage}\n\t Skill 1 ({skill1name}) : {skill1damage}\n\t Skill 2 ({skill2name}) : {skill2damage}\n\t Skill 3 ({skill3name}) : {skill3damage} ')
    print("="*30)
    
# daftar heronya
Fanny = Hero("Fanny", 30, 100, 5, [("Steel Cable", 10), ("Tornado Strike", 15), ("Cut Throat", 25)])
Alucard = Hero("Alucard", 50, 120, 3, [("Groundsplitter", 5), ("Whirling Smash", 10), ("Fission Waves", 15)])
Claude = Hero("Claude", 10, 80, 8, [("Art of Thievery", 15), ("Battle Mirror Image", 5), ("Blazing Duet", 40)])

daftarHero = [Fanny, Alucard, Claude]
mainHero = None

# pilih hero utama
def pilihHero():
  print("Pilih hero kamu!")
  for i, hero in enumerate(daftarHero, 1):
    print(f'{i}. {hero.name}')
  pilihan = int(input("Masukkan nomor hero: "))
  mainHero = daftarHero[pilihan-1]
  #tampilin hero pilihanmu
  mainHero.tampilkanInfo()
  daftarLawan = [h for h in daftarHero if h != mainHero]
  return mainHero, daftarLawan
  
#pilihLawan
def pilihLawan(mainHero, daftarLawan):
  print("Pilih lawanmu!")
  for i, hero in enumerate(daftarLawan, 1):
    print(f'{i}. {hero.name}')
  pilihan = int(input("Masukkan nomor lawan: "))
  mainLawan = daftarLawan[pilihan-1]
  #tampilin lawan pilihanmu
  mainLawan.tampilkanInfo()
  return mainLawan
  
#battle
def battle(mainHero, mainLawan):
  print("="*30)
  print(f"{mainHero.name} VS {mainLawan.name}")
  jumlahseranganmainHero = random.randint(1, 4)
  jumlahseranganmainLawan = random.randint(1, 4)
  skillmainHero = random.choice([1, 2, 3, None])
  skillmainLawan = random.choice([1, 2, 3, None])
  time.sleep(1)
  mainHero.serang(mainLawan, jumlahseranganmainHero, skillmainHero)
  
  time.sleep(1)
  if mainLawan.hp > 0:
    mainLawan.serang(mainHero, jumlahseranganmainLawan, skillmainLawan)
    if mainHero.hp > 0:
      battle(mainHero, mainLawan)
    elif mainHero.hp == 0:
      time.sleep(1)
      print(f"Kamu kalah, {mainHero.name} telah mati.")
  elif mainLawan.hp == 0:
    time.sleep(1)
    print(f"KAMU MENANG!, {mainLawan.name} telah mati.")



def main():
  mainHero, daftarLawan = pilihHero()
  mainLawan = pilihLawan(mainHero, daftarLawan)
  battle(mainHero, mainLawan)
main()