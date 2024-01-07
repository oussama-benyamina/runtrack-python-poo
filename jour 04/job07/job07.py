import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        if not self.paquet:
            print("Plus de cartes dans le paquet.")
            return None
        return self.paquet.pop()

    def calculer_points(self, main):
        total = sum(self.valeur_carte(carte) for carte in main)
        as_present = any(carte.valeur == 'A' for carte in main)
        if as_present and total <= 11:
            total += 10
        return total

    def valeur_carte(self, carte):
        if carte.valeur in ['J', 'Q', 'K']:
            return 10
        elif carte.valeur == 'A':
            return 1
        else:
            return int(carte.valeur)



jeu = Jeu()
jeu.melanger_paquet()

main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

print("Main du joueur:")
for carte in main_joueur:
    print(f"{carte.valeur} de {carte.couleur}")

print("\nMain du croupier:")
print(f"{main_croupier[0].valeur} de {main_croupier[0].couleur} (Carte cachée)")


points_joueur = jeu.calculer_points(main_joueur)
print(f"\nPoints du joueur: {points_joueur}")


carte_supplementaire = jeu.tirer_carte()
main_joueur.append(carte_supplementaire)

print(f"\nNouvelle carte tirée pour le joueur: {carte_supplementaire.valeur} de {carte_supplementaire.couleur}")


points_joueur = jeu.calculer_points(main_joueur)
print(f"Points du joueur après tirage : {points_joueur}")
