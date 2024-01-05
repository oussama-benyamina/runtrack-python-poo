class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True 
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def get_disponible(self):
        return self.__disponible

    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")

    def verification(self):
        return self.__disponible

    
    def emprunter(self):
        if self.verification():
            print("Emprunt du livre :", self.__titre)
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour emprunt.")

    
    def rendre(self):
        if not self.verification():
            print("Rendu du livre :", self.__titre)
            self.__disponible = True
        else:
            print("Le livre est déjà disponible.")

mon_livre = Livre("Titre du livre", "Auteur du livre", 200)

print("Disponibilité initiale :", mon_livre.verification())

mon_livre.emprunter()
mon_livre.emprunter()
mon_livre.rendre()

mon_livre.rendre()
