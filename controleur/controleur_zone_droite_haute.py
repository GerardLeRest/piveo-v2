#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la zone droite haute
"""

from modele.prenom_nom import PrenomNom
from PySide6.QtCore import Slot


class ControleurZoneDroiteHaute:
    def __init__(self, vue):
        self.vue = vue

        # zone droite haute
        self.vue.zone_droite_haute.demande_suite.connect(self.avancer)
        self.vue.zone_droite_haute.demande_effacer.connect(self.effacer)
        self.vue.zone_droite_haute.demande_valider.connect(self.valider)
        
    @Slot()
    def avancer(self) -> None:
        """Passer à la personne suivante."""
        self.vue.controleur_zone_gauche.avancer()

    @Slot()
    def effacer(self)->None:
        """effacer les champs"""
        self.vue.prenom_entree.clear()
        self.vue.nom.entree.clear()

    @Slot()
    def valider(self)->None:
        """valider la réponse"""