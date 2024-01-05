import random

class Personnage:
    def __init__(self, nom, vie, attaque, defense):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque
        self.defense = defense

    def attaquer(self, cible):
        degats = max(0, self.attaque - cible.defense) + random.randint(5, 15)
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts.")
        cible.vie = max(0, cible.vie - degats)
        print(f"{cible.nom} a maintenant {cible.vie} points de vie.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        niveau = input("Choisissez le niveau de difficulté (1, 2, 3) : ")
        try:
            self.niveau = int(niveau)
        except ValueError:
            print("Niveau non valide. Le niveau sera défini comme 1.")

    def lancerJeu(self):
        print("Bienvenue dans le jeu de combat!")
        self.choisirNiveau()

        joueur = Personnage("Joueur", self.niveau * 50, self.niveau * 10, self.niveau * 5)
        ennemi = Personnage("Ennemi", self.niveau * 30, self.niveau * 8, self.niveau * 3)

        while joueur.vie > 0 and ennemi.vie > 0:
            action = input("Que voulez-vous faire? (1: Attaquer, 2: Se défendre) : ")

            if action == "1":
                joueur.attaquer(ennemi)
            elif action == "2":
                print(f"{joueur.nom} se défend et récupère {joueur.defense} points de vie.")
                joueur.vie += joueur.defense
            else:
                print("Action non reconnue. Vous perdez votre tour.")

            ennemi.attaquer(joueur)

            print(f"\nStatut actuel : {joueur.nom} ({joueur.vie} vie) vs {ennemi.nom} ({ennemi.vie} vie)\n")

        if joueur.vie > 0:
            print(f"{ennemi.nom} a été vaincu! Félicitations, vous avez gagné!")
        else:
            print(f"{joueur.nom} a été vaincu! Dommage, vous avez perdu.")


jeu = Jeu()


jeu.lancerJeu()
