#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la toolbar
"""

class ControleurToolbar:

    def __init__(self, vue):
        self.vue = vue
        print("init")
        self.vue.fenetre_principale.demande_mode_lecture.connect(self.lire)

    def lire(self)->None:
        """mode lecture"""
        self.vue.fenetre_principale.mettre_a_jour_liste_personne(self.vue.zone_droite_basse.liste_personnes)
        print("lire")