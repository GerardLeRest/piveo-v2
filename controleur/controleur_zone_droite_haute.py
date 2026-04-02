from modele.modele_zone_droite_haute import ModeleZoneDroiteHaute
from modele.modele_recherche import ModeleRecherche
from PySide6.QtCore import Slot

class ControleurZoneDroiteHaute:
    """Contrôleur de la zone droite haute."""

    def __init__(self, vue, controleur_zone_gauche) -> None:
        self.vue = vue
        self.controleur_zone_gauche = controleur_zone_gauche

        self.vue.zone_droite_haute.demande_valider.connect(self.action_valider)
        self.vue.zone_droite_haute.demande_effacer.connect(self.effacer)
        self.vue.zone_droite_haute.demande_suite.connect(self.suite)
        self.nbre_bonnes_rep = 0

    @Slot()
    def action_valider(self) -> None:
        """Choisir entre validation ou recherche selon le mode actif."""
        if self.vue.act_ecrit.isChecked():
            self.valider()
        elif self.vue.act_recherche.isChecked():
            liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
            liste_personnes = self.rechercher_personnes(liste)
            self.controleur_zone_gauche.charger_liste(liste_personnes, None)

    @Slot()
    def valider(self) -> None:
        print("valider appelée")
        prenom_saisi, nom_saisi = self.vue.zone_droite_haute.recuperer_saisie()
        personne = self.vue.zone_gauche.liste_personnes[self.vue.zone_gauche.rang+1]
        prenom_attendu = personne[0].lower()
        nom_attendu = personne[1].lower()

        modele = ModeleZoneDroiteHaute(prenom_attendu, nom_attendu)

        resultat_prenom = modele.comparer_prenom(prenom_saisi)
        resultat_nom = modele.comparer_nom(nom_saisi)

        resultat = self.vue.zone_droite_haute.afficher_image_check(resultat_prenom, resultat_nom)
        if resultat:
            self.nbre_bonnes_rep += 1
        print("nbre_bonnes_rep =", self.nbre_bonnes_rep)

    @Slot()
    def effacer(self) -> None:
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.gestion_focus()

    @Slot()
    def suite(self) -> None:
        """Passer à la personne suivante et afficher le score."""
        self.controleur_zone_gauche.avancer()
        # calcul simple - reste dans le controleur
        rang_affiche = (self.vue.zone_gauche.rang // 2) + 1
        self.vue.zone_droite_haute.affichage_score(self.nbre_bonnes_rep, rang_affiche)

    def rechercher_personnes(self, liste: list) -> list:
        """rechercher suivant les prenoms/noms"""
        modele_recherche = ModeleRecherche(self.vue, liste)
        return modele_recherche.trouver()