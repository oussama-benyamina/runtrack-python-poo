class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = credits
        self._level = self._student_eval()

    def add_credits(self, amount):
        if amount > 0:
            self._credits += amount
            self._level = self._student_eval()
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")
            
    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Informations sur l'étudiant:")
        print(f"Nom: {self._nom}")
        print(f"Prénom: {self._prenom}")
        print(f"Identifiant: {self._numero_etudiant}")
        print(f"Niveau: {self._level}")

john_doe = Student("Jhon", "Doe", 145)


john_doe.add_credits(20)
john_doe.add_credits(15)
john_doe.add_credits(5)


john_doe.student_info()