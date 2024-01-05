class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "En cours"

    # méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
        print(f"Plat '{nom_plat}' ajouté à la commande.")

    # méthode pour annuler la commande
    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "Annulée"
        print("La commande a été annulée.")

    # methode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    # methode pour afficher la commande avec son total à payer
    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande}:")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f" - {nom_plat}: {plat['prix']} € ({plat['statut']})")
        total = self.__calculer_total()
        print(f"Total à payer : {total} €")

    # methode pour calculer la TVA de la commande
    def calculer_tva(self, taux_tva=0.2):
        total = self.__calculer_total()
        tva = total * taux_tva
        print(f"La TVA à payer est de : {tva} €")

# Exemple d'utilisation de la classe Commande
commande1 = Commande(1)

# Ajout de plats à la commande
commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Salade", 5)
commande1.ajouter_plat("Pâtes", 8)

# Affichage de la commande
commande1.afficher_commande()

# Calcul de la TVA
commande1.calculer_tva()

# Annulation de la commande
commande1.annuler_commande()

# Affichage de la commande après annulation
commande1.afficher_commande()
