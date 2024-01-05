class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    
    def demarrer(self):
        if self.__verifier_plein():
            print("La voiture démarre.")
            self.__en_marche = True
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    
    def arreter(self):
        print("La voiture s'arrête.")
        self.__en_marche = False

    
    def __verifier_plein(self):
        return self.__reservoir > 5


ma_voiture = Voiture("Toyota", "Camry", 2022, 10000)


print("Marque :", ma_voiture.get_marque())
print("Modèle :", ma_voiture.get_modele())
print("Année :", ma_voiture.get_annee())
print("Kilométrage :", ma_voiture.get_kilometrage())
print("En marche :", ma_voiture.get_en_marche())
print("Réservoir :", ma_voiture.get_reservoir())


ma_voiture.demarrer()


ma_voiture.arreter()
