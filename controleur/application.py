#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
lien entre les modèles et les vues
"""

from modele.defilement_photos import DefilementPhotos

class Application:

    def __init__(self, vue):
        print("application")
        self.vue = vue
        self.defilement_photos = DefilementPhotos(self.vue.zone_gauche.liste_personnes)
        # zone gauche
        self.vue.zone_gauche.demande_avancer.connect(self.avancer)
        self.vue.zone_gauche.demande_reculer.connect(self.reculer)
        self.vue.zone_gauche.demande_debut.connect(self.debut)
        self.vue.zone_gauche.demande_fin.connect(self.fin)
        # zone droite haute
        self.vue.zone_droite_haute.demande_suite.connect(self.avancer)

    def avancer(self):
        print("avancer")
        self.defilement_photos.acceder_suivant()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    def reculer(self):
        """reculer vers la gauche"""
        self.defilement_photos.acceder_precedent()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    def debut(self):
        """aller au début"""
        self.defilement_photos.acceder_premier()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    def fin(self):
        """aller à la fin"""
        self.defilement_photos.acceder_dernier()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()
