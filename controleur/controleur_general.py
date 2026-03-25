#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur général
"""

from controleur.controleur_zone_gauche import ControleurZoneGauche
from controleur.controleur_zone_droite_haute import ControleurZoneDroiteHaute
from controleur.controleur_zone_droite_basse import ControleurZoneDroiteBasse


class ControleurGeneral:
    def __init__(self, vue, gestionnaire_bdd):
        self.vue = vue
        self.gestionnaire_bdd = gestionnaire_bdd
        # Construction des trois contrôleurs locaux
        self.controleur_zone_gauche = ControleurZoneGauche(self.vue)
        self.controleur_zone_droite_haute = ControleurZoneDroiteHaute(self.vue)
        self.controleur_zone_droite_basse = ControleurZoneDroiteBasse(
            self.gestionnaire_bdd
        )
        self.vue.demande_mode_lecture.connect(self.mode_lecture)

    def mode_lecture(self) -> None:
        """Activer le mode lecture."""
        liste = self.vue.zone_droite_basse.liste_personnes_filtree
        self.controleur_zone_gauche.charger_liste(liste)

    def mettre_a_jour_liste_personnes(self, liste_personnes: list) -> None:
        """Transmettre la liste au contrôleur de zone gauche."""
        self.controleur_zone_gauche.charger_liste(liste_personnes)