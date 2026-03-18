#!/usr/bin/python3
# -*- coding: utf-8 -*-

from modele.prenom_nom import PrenomNom
from PySide6.QtCore import Slot


class ControleurZoneDroiteHaute:
    def __init__(self, vue):
        self.vue = vue

        # zone droite haute
        self.vue.zone_droite_haute.demande_suite.connect(self.avancer)
        self.vue.zone_droite_haute.demande_etat_prenom.connect(self.widgets_prenom)
        self.vue.zone_droite_haute.demande_etat_nom.connect(self.widgets_nom)
        self.vue.zone_droite_haute.demande_valider.connect(self.recuperation_ecrite)

    @Slot()
    def avancer(self) -> None:
        """Passer à la personne suivante."""
        self.vue.controleur_zone_gauche.avancer()

    @Slot(bool)
    def widgets_prenom(self, etat: bool) -> None:
        """Activer ou désactiver le champ prénom."""
        if etat:
            self.vue.zone_gauche.prenom.setEnabled(True)
            self.vue.zone_gauche.prenom.setText("Prénom")
        else:
            self.vue.zone_gauche.prenom.setText("")
            self.vue.zone_gauche.prenom.setEnabled(False)

    @Slot(bool)
    def widgets_nom(self, etat: bool) -> None:
        """Activer ou désactiver le champ nom."""
        if etat:
            self.vue.zone_gauche.nom.setEnabled(True)
            self.vue.zone_gauche.nom.setText("Nom")
        else:
            self.vue.zone_gauche.nom.setText("")
            self.vue.zone_gauche.nom.setEnabled(False)

    @Slot()
    def recuperation_ecrite(self) -> None:
        """Récupérer le prénom et le nom saisis."""
        print("recuperation_ecrite")

        prenom = self.vue.zone_droite_haute.prenom_entree.text()
        nom = self.vue.zone_droite_haute.nom_entree.text()

        self.prenom_nom = PrenomNom(prenom, nom)

        resultat_prenom = self.prenom_nom.comparer_prenom(prenom)
        resultat_nom = self.prenom_nom.comparer_nom(nom)

        self.vue.zone_droite_haute.afficher_image_check(resultat_prenom, resultat_nom)