class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur

    @longueur.setter
    def longueur(self, value):
        self.__longueur = value

    @property
    def largeur(self):
        return self.__largeur

    @largeur.setter
    def largeur(self, value):
        self.__largeur = value

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    @property
    def hauteur(self):
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, value):
        self.__hauteur = value

    def volume(self):
        return self.longueur * self.largeur * self.__hauteur



mon_rectangle = Rectangle(longueur=5, largeur=3)


print("Périmètre du rectangle :", mon_rectangle.perimetre())
print("Surface du rectangle :", mon_rectangle.surface())


mon_rectangle.longueur = 7
mon_rectangle.largeur = 4


print("Nouvelle longueur du rectangle :", mon_rectangle.longueur)
print("Nouvelle largeur du rectangle :", mon_rectangle.largeur)
print("Nouveau périmètre du rectangle :", mon_rectangle.perimetre())
print("Nouvelle surface du rectangle :", mon_rectangle.surface())

mon_parallelepipede = Parallelepipede(longueur=5, largeur=3, hauteur=2)

print("Volume du parallélépipède :", mon_parallelepipede.volume())
