class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"


personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")


presentation1 = personne1.SePresenter()
presentation2 = personne2.SePresenter()


print(presentation1)
print(presentation2)
