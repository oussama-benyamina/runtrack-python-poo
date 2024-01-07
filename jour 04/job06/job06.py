class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print(f"{self.marque} - {self.modele}: Moteur en marche, prêt à rouler!")

ma_voiture = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)

ma_voiture.informationsVehicule()
ma_voiture.demarrer()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix)
        self.roues = roues

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")

    def demarrer(self):
        print(f"{self.marque} - {self.modele}: Démarrage du moteur de la moto.")



ma_moto = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)



ma_moto.informationsVehicule()
ma_moto.demarrer()
