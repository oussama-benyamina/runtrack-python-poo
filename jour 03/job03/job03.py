class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} ({self.statut})"
class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{tache.titre}' supprimée de la liste.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "Terminée"
                print(f"Tâche '{tache.titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def afficherListe(self):
        if not self.taches:
            print("La liste de tâches est vide.")
        else:
            print("Liste de tâches:")
            for tache in self.taches:
                print(tache)

    def filterListe(self, statut):
        filtered_taches = [tache for tache in self.taches if tache.statut == statut]
        return filtered_taches

tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser Python", "Préparer pour l'examen")
tache3 = Tache("Faire du sport", "30 minutes de jogging")


liste_taches = ListeDeTaches()


liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)


liste_taches.afficherListe()


liste_taches.marquerCommeFinie("Réviser Python")


liste_taches.afficherListe()


liste_taches.supprimerTache("Faire du sport")


liste_taches.afficherListe()


taches_a_faire = liste_taches.filterListe("À faire")
print("\nTâches à faire:")
for tache in taches_a_faire:
    print(tache)
