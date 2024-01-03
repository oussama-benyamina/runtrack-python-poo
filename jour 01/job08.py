import math
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")
    def volume(self):
        return 2 * math.pi * self.rayon
    def aire(self):
        return math.pi * self.rayon**2
    def diametre(self):
        return 2 * self.rayon

cercle1 = Cercle(4)
cercle2 = Cercle(7)

for cercle in [cercle1, cercle2]:
    print(f"Cercle avec un rayon de {cercle.rayon}:")
    cercle.afficherInfos()
    print(f"Volume : {cercle.volume()}")
    print(f"Diamètre : {cercle.diametre()}")
    print(f"Aire : {cercle.aire()}")