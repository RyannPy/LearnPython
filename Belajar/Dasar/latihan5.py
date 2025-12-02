class Burung:
    def suara(self):
        print("Cuit")

class Anjing:
    def suara(self):
        print("Guk guk")

for hewan in [Burung(), Anjing()]:
    hewan.suara()