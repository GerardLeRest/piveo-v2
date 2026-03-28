class ModeleRecherche:
    def __init__(self, vue, liste):
        self.vue = vue
        self.liste = liste
        
        self.liste_finale = []

    def trouver(self) -> list:
        """Rechercher les personnes suivant les données rentrées."""
        nom = self.vue.zone_droite_haute.nom_entree.text().lower().strip()
        prenom = self.vue.zone_droite_haute.prenom_entree.text().lower().strip()
        # sélection des prénoms / noms
        prenom_selectionne = self.vue.zone_droite_haute.verification_prenom.isChecked()
        nom_selectionne = self.vue.zone_droite_haute.verification_nom.isChecked()
        # constitution de la liste finale#
        for eleve in self.liste:
            prenom_eleve = eleve[0].lower().strip()
            nom_eleve = eleve[1].lower().strip()

            if prenom_selectionne and nom_selectionne:
                condition = (prenom == prenom_eleve) and (nom == nom_eleve)
            elif prenom_selectionne and not nom_selectionne:
                condition = prenom == prenom_eleve
            elif not prenom_selectionne and nom_selectionne:
                condition = nom == nom_eleve
            else:
                condition = False

            if condition:
                self.liste_finale.append(eleve)

        return self.liste_finale