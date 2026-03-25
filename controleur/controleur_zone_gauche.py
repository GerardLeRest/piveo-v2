#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la zone gauche
"""

from modele.modele_zone_gauche import ModeleZoneGauche
from PySide6.QtCore import Slot


class ControleurZoneGauche:
    def __init__(self, vue):
        print("controleur zone gauche")
        self.vue = vue
        self.defilement_photos = ModeleZoneGauche(self.vue.zone_gauche.liste_personnes)

        # zone gauche
        self.vue.zone_gauche.demande_avancer.connect(self.avancer)
        self.vue.zone_gauche.demande_reculer.connect(self.reculer)
        self.vue.zone_gauche.demande_debut.connect(self.debut)
        self.vue.zone_gauche.demande_fin.connect(self.fin)

    @Slot()
    def avancer(self) -> None:
        print("avancer")
        self.defilement_photos.acceder_suivant()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def reculer(self) -> None:
        """Reculer vers la gauche."""
        self.defilement_photos.acceder_precedent()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def debut(self) -> None:
        """Aller au début."""
        self.defilement_photos.acceder_premier()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def fin(self) -> None:
        """Aller à la fin."""
        self.defilement_photos.acceder_dernier()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    def charger_liste_personnes(self, liste_personnes) -> None:
        """"""
        self.defilement_photos = ModeleZoneGauche(liste_personnes)
        self.vue.zone_gauche.rang = 0
        self.vue.zone_gauche.liste_personnes = liste_personnes
        self.vue.zone_gauche.maj()