class Animal:
    def __init__(self):
        
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        
    def nommer(self, nom):
        self.prenom = nom


mon_animal = Animal()
mon_animal.nommer("Luna")

print(f"Mon animal se nomme : {mon_animal.prenom}")
print(f"Âge initial de l'animal : {mon_animal.age}")
mon_animal.vieillir()


print(f"Nouvel âge de l'animal : {mon_animal.age}")