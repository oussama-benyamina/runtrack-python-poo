class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        print(f"Produit : {self.nom}")
        print(f"Prix HT : {self.prixHT} euros")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.CalculerPrixTTC()} euros")

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Laptop", 800, 20)
produit2 = Produit("Smartphone", 500, 15)


produit1.afficher()
print("\n")
produit2.afficher()
print("\n")

produit1.modifierNom("Ordinateur Portable")
produit1.modifierPrixHT(900)

produit2.modifierNom("Téléphone Intelligent")
produit2.modifierPrixHT(550)
produit1.afficher()
print("\n")
produit2.afficher()
