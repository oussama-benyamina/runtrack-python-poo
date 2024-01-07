class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")


class Professeur(Personne):
    def __init__(self, age=30, matiereEnseignee="Mathématiques"):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


 
eleve1 = Eleve()


eleve1.bonjour()       
eleve1.allerEnCours()  

eleve1.modifierAge(15)

eleve1.afficherAge()    
professeur1 = Professeur(age=40)
professeur1.bonjour()    
professeur1.enseigner()  
