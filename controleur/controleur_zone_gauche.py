#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la zone gauche
"""

from modele.modele_gauche import ModeleGauche
from PySide6.QtCore import Slot


class ControleurZoneGauche:
    def __init__(self, vue):
        self.vue = vue # fenêtre principale - zone_gauche:sous-widgets
        self.modele_gauche = ModeleGauche(self.vue.zone_droite_basse.liste_personnes_filtree)
        
        # zone gauche
        self.vue.zone_gauche.demande_avancer.connect(self.avancer)
        self.vue.zone_gauche.demande_reculer.connect(self.reculer)
        self.vue.zone_gauche.demande_debut.connect(self.debut)
        self.vue.zone_gauche.demande_fin.connect(self.fin)

        self.vue.zone_droite_basse.demande_BP_valider_ZD.connect(self.activer_bp)
        
    @Slot()
    def avancer(self) -> None:
        self.modele_gauche.acceder_suivant()
        self.vue.zone_gauche.rang = self.modele_gauche.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def reculer(self) -> None:
        """Reculer vers la gauche."""
        self.modele_gauche.acceder_precedent()
        self.vue.zone_gauche.rang = self.modele_gauche.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def debut(self) -> None:
        """Aller au début."""
        self.modele_gauche.acceder_premier()
        self.vue.zone_gauche.rang = self.modele_gauche.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def fin(self) -> None:
        """Aller à la fin."""
        self.modele_gauche.acceder_dernier()
        self.vue.zone_gauche.rang = self.modele_gauche.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def activer_bp(self):
        """activer ls quatre boutons de la zone"""
        self.vue.zone_gauche.activer_boutons()