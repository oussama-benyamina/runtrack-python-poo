class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def mettre_a_jour_population(self, increment):
        self.__nombre_habitants += increment


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.mettre_a_jour_population(1)

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"Population de la ville de Paris: {paris.get_nombre_habitants()} habitants")

print(f"Population de la ville de Marseille: {marseille.get_nombre_habitants()} habitants")

john = Personne("John", 45, paris)

myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


john.ajouterPopulation()

myrtille.ajouterPopulation()

chloe.ajouterPopulation()

paris.mettre_a_jour_population(0) 

marseille.mettre_a_jour_population(0)  
print(f"Mise à jour de la population de la ville de Paris: {paris.get_nombre_habitants()} habitants")
print(f"Mise à jour de la population de la ville de Marseille: {marseille.get_nombre_habitants()} habitants")
