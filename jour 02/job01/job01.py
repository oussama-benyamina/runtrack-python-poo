class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    # Assesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle avec les valeurs initiales
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Longueur initiale :", mon_rectangle.get_longueur())
print("Largeur initiale :", mon_rectangle.get_largeur())

# Modification des valeurs
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(7)

# Affichage des valeurs modifiées
print("Nouvelle longueur :", mon_rectangle.get_longueur())
print("Nouvelle largeur :", mon_rectangle.get_largeur())
