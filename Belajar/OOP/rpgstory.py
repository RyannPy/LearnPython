import time, sys
import random


class Makhluk:
  def __init__ (self, name, health, defense, skills):
    self.name = name
    self.health = health
    self.defense = defense
    self.skills = skills
    self.cooldowns = {}

Player = Makhluk(
  "Player", 
  100, 
  10, 
  [
    ("Sword Dash", 10, 1), 
    ("God Aiming", 15, 2), 
    ("End of World", 20, 3)]
  )


# Enemy 1: Goblin
Goblin = Makhluk(
    "Goblin",
    60,
    5,
    [
        ("Tusukan Karat", 8, 1),
        ("Teriakan Liar", 12, 2),
        ("Lempar Batu", 18, 3),
    ]
)

# Enemy 2: Serigala Buas
Serigala = Makhluk(
    "Serigala Buas",
    80,
    8,
    [
        ("Gigit", 10, 1),
        ("Cakar Mematikan", 15, 2),
        ("Howl Darah", 20, 3),
    ]
)

# Enemy 3: Ogre
Ogre = Makhluk(
    "Ogre",
    120,
    15,
    [
        ("Tinju Raksasa", 12, 1),
        ("Hantaman Tanah", 18, 2),
        ("Teriakan Mengerikan", 25, 3),
    ]
)

# Enemy 4: Naga Api (Boss)
NagaApi = Makhluk(
    "Naga Api",
    200,
    20,
    [
        ("Cakar Api", 20, 1),
        ("Napas Api", 30, 2),
        ("Meteor Flame", 40, 3),
    ]
)


# Daftar enemy bisa kamu taruh di list
daftarEnemy = [Goblin, Serigala, Ogre, NagaApi]

def pakaiSkill(self, nomorskill):
  index = nomorskill - 1
  skillname, skilldamage, skillcd = self.skills[index]
  print("="*30)
  print(f'{self.name} menggunakan skill {skillname}')
  print(f'Damage diberikan: {skilldamage}')
  print("="*30)
  #damage dilanjutkan ke fungsi serang
  totaldamage = skilldamage
  return totaldamage

  
def serang(self, lawan, nomorskill):
  print(f'{self.name} menyerang {lawan.name}')
  self.pakaiSkill(nomorskill)
  #total damage diambil, dilanjutkan untuk mengurangi def dan health
  lawan.health = lawan.health + lawan.defense - totaldamage
  print(f'HP {lawan.name} tersisa {lawan.health}')
  
  
  
  
  