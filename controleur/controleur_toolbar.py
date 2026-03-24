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
from modele.modele_deviner import ModeleToolbar
from modele.modele_gauche import ModeleGauche


class ControleurToolbar:

    def __init__(self, vue):
        self.vue = vue
        # vue
        self.vue.act_lecture.triggered.connect(self.mode_lire)
        self.vue.act_reponse_cachee.triggered.connect(self.mode_deviner)
        self.vue.act_test_ecrit.triggered.connect(self.mode_ecrit)
        self.vue.act_recherche.triggered.connect(lambda: print("recherche"))
        #modele
        self.modele_toolbar = ModeleToolbar()
        #self.vue.demande_mode_lecture.connect(self.lire)
        # self.vue.act_aleatoire.toggled.connect(self.gerer_aleatoire)
        # self.vue.demande_mode_reponse_cachee.connect(self.deviner)
        # self.modele_toolbar = ModeleToolbar()

    def mode_lire(self) -> None:
        """Mode lecture."""
        liste_personnes = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        self.vue.mettre_a_jour_liste_personnes(liste_personnes)

    def mode_deviner(self) -> None:
        """Mode deviner."""
        #self.vue.act_aleatoire.setChecked(False)
        masquer_prenom = not self.vue.zone_droite_haute.verification_prenom.isChecked()
        masquer_nom = not self.vue.zone_droite_haute.verification_nom.isChecked()
        # insertion des "????"
        liste_affichage = self.modele_toolbar.ajouter_points_interrogations(
            self.vue.zone_droite_basse.liste_personnes_filtree.copy(),
            masquer_prenom,
            masquer_nom
        )
        # Mises à jours
        self.vue.zone_gauche.liste_personnes = liste_affichage
        self.vue.zone_gauche.rang = 0
        self.vue.zone_gauche.nbre_pers = len(liste_affichage)
        # très important
        self.vue.controleur_zone_gauche.modele_gauche = ModeleGauche(liste_affichage)
        self.vue.zone_gauche.maj()

    def mode_ecrit(self)->None:
        """rechercer prenonm/nom """
        liste_personnes = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        self.vue.controleur_zone_droite_haute.valider(liste_personnes)

    def gerer_aleatoire(self) -> None:
        """Gérer le mode aléatoire."""
        if self.vue.act_aleatoire.isChecked():
            self.mode_aleatoire = True
        else:
            self.mode_aleatoire = False
        print (self.mode_aleatoire)