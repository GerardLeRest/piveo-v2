#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la zone toolbar
"""

from modele.modele_combobox import (
    creer_specialites,
    lister_structures,
    construire_liste_structures
)
from modele.modele_toolbar import ModeleToolbar
from vue.zone_droite_basse import ZoneDroiteBasse


class ControleurToolbar:

    def __init__(self, vue):
        self.vue = vue
        self.vue.demande_mode_lecture.connect(self.lire)
        self.vue.demande_mode_aleatoire.connect(self.gerer_aleatoire)
        self.vue.demande_mode_reponse_cachee.connect(self.deviner)
        self.modele_toolbar = ModeleToolbar()

    def lire(self) -> None:
        """Mode lecture."""
        self.vue.act_aleatoire.setChecked(False) # mode non aléatoire
        self.vue.zone_gauche.liste_personnes = self.vue.liste_personnes_courante.copy()
        self.vue.zone_gauche.rang = 0
        self.vue.zone_gauche.nbre_pers = len(self.vue.zone_gauche.liste_personnes)
        self.vue.zone_gauche.maj()

    def deviner(self) -> None:
        """Mode deviner."""
        self.vue.act_aleatoire.setChecked(False)

        masquer_prenom = not self.vue.zone_droite_haute.verification_prenom.isChecked()
        masquer_nom = not self.vue.zone_droite_haute.verification_nom.isChecked()
        # insertion des "????"
        liste_affichage = self.modele_toolbar.ajouter_points_interrogations(
            self.vue.liste_personnes_courante.copy(),
            masquer_prenom,
            masquer_nom
        )
        # Mises à jours
        self.vue.zone_gauche.liste_personnes = liste_affichage
        self.vue.zone_gauche.rang = 0
        self.vue.zone_gauche.nbre_pers = int (len(liste_affichage) / 2) # /2 à cause de ????
        self.vue.zone_gauche.maj()

    def gerer_aleatoire(self) -> None:
        """Gérer le mode aléatoire."""
        if self.vue.act_aleatoire.isChecked():
            self.vue.zone_gauche.liste_personnes = self.modele_toolbar.melanger(
                self.vue.liste_personnes_courante
            )
        else:
            self.vue.zone_gauche.liste_personnes = self.vue.liste_personnes_courante.copy()
        # MAJ
        self.vue.zone_gauche.rang = 0
        self.vue.zone_gauche.nbre_pers = len(self.vue.zone_gauche.liste_personnes)
        self.vue.zone_gauche.maj()