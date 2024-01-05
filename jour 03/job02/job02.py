class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, autorise_decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__autorise_decouvert = autorise_decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero_compte}")
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Solde : {self.__solde} EUR")

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde} EUR")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} EUR effectué. Nouveau solde : {self.__solde} EUR")

    def retrait(self, montant):
        if self.__solde >= montant or self.__autorise_decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} EUR effectué. Nouveau solde : {self.__solde} EUR")
        else:
            print("Opération non autorisée. Solde insuffisant.")

    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05  # Supposons un taux d'agios de 5%
            self.__solde -= frais
            print(f"Agios appliqués. Nouveau solde : {self.__solde} EUR")

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} EUR effectué vers le compte {compte_destinataire.__numero_compte}")
        else:
            print("Opération non autorisée. Solde insuffisant.")


compte1 = CompteBancaire(numero_compte="123456", nom="Doe", prenom="John", solde=1000)


compte2 = CompteBancaire(numero_compte="789012", nom="Smith", prenom="Alice", solde=-200, autorise_decouvert=True)


compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)

compte2.afficher()
compte2.afficherSolde()
compte1.virement(compte2, 300)


compte1.afficherSolde()
compte2.afficherSolde()
