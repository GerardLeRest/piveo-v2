#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la zone droite haute
"""

from modele.modele_zone_droite_haute import ModeleZoneDroiteHaute
from modele.modele_recherche import ModeleRecherche
from PySide6.QtCore import Slot

class ControleurZoneDroiteHaute:
    """Contrôleur de la zone droite haute."""

    def __init__(self, vue, controleur_zone_gauche, gestionnaire_bdd) -> None:
        self.vue = vue
        self.controleur_zone_gauche = controleur_zone_gauche
        self.gestionnaire_bdd = gestionnaire_bdd
        self.vue.zone_droite_haute.demande_valider.connect(self.action_valider)
        self.vue.zone_droite_haute.demande_effacer.connect(self.effacer)
        self.vue.zone_droite_haute.demande_suite.connect(self.suite)
        self.nbre_bonnes_rep = 0
        self.vue.zone_droite_haute.demande_effacer.connect(self.effacer)
        self.vue.zone_droite_haute.demande_suite.connect(self.suite)

    @Slot()
    def action_valider(self) -> None:
        """Choisir entre validation ou recherche selon le mode actif."""
        if self.vue.act_ecrit.isChecked():
            self.valider()
        elif self.vue.act_recherche.isChecked():
            self.rechercher()

    @Slot()
    def valider(self) -> None:
        """Valider la réponse en mode écrit."""
        prenom_saisi, nom_saisi = self.vue.zone_droite_haute.recuperer_saisie()
        personne = self.vue.zone_gauche.liste_personnes[self.vue.zone_gauche.rang + 1]
        prenom_attendu = personne[0].lower()
        nom_attendu = personne[1].lower()
        #création du modèle ModeleZoneDroiteHaute
        modele = ModeleZoneDroiteHaute(prenom_attendu, nom_attendu)
        resultat_prenom = modele.comparer_prenom(prenom_saisi)
        resultat_nom = modele.comparer_nom(nom_saisi)
        # récupération du résultat
        resultat = self.vue.zone_droite_haute.afficher_image_check(resultat_prenom, resultat_nom)
        if resultat:
            self.nbre_bonnes_rep += 1
        if self.vue.zone_gauche.rang < len(self.vue.zone_gauche.liste_personnes) - 1:
            self.vue.zone_gauche.rang += 1
        else:
            self.vue.zone_gauche.rang = 0
        self.vue.zone_gauche.maj()
        

    @Slot()
    def rechercher(self) -> None:
        """Lancer la recherche des personnes."""
        liste = self.gestionnaire_bdd.liste_personnes
        liste_personnes = self.rechercher_personnes(liste)
        self.controleur_zone_gauche.charger_liste(liste_personnes, "recherche")

    @Slot()
    def effacer(self) -> None:
        """préparer les champs"""
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.gestion_focus()

    @Slot()
    def suite(self) -> None:
        """Passer à la personne suivante et afficher le score."""
        rang_affiche = (self.vue.zone_gauche.rang // 2) + 1
        self.vue.zone_droite_haute.affichage_score(self.nbre_bonnes_rep, rang_affiche)
        self.controleur_zone_gauche.avancer()
        self.vue.zone_droite_haute.cacher_image_check()

    def rechercher_personnes(self, liste: list) -> list:
        """rechercher suivant les prenoms/noms"""
        modele_recherche = ModeleRecherche(self.vue, liste)
        return modele_recherche.trouver()
