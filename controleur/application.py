#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
lien entre les modèles et les vues
"""

from modeles.defilement_photos import DefilementPhotos

class Application:

    def __init__(self, vue):
        self.vues = vue
        self.defilement_photos = DefilementPhotos(self.vues.liste_personnes)
        self.vues.demande_avancer.connect(self.avancer)
        self.vues.demande_reculer.connect(self.reculer)
        self.vues.demande_debut.connect(self.debut)
        self.vues.demande_fin.connect(self.fin)
    
    def avancer(self):
        """avancer vers la droite"""
        self.defilement_photos.acceder_suivant()
        self.vues.rang = self.defilement_photos.rang
        self.vues.maj()

    def reculer(self):
        """avancer vers la gauche"""
        self.defilement_photos.acceder_precedent()
        self.vues.rang = self.defilement_photos.rang
        self.vues.maj()

    def debut(self):
        """avancer vers le début"""
        self.defilement_photos.acceder_premier()
        self.vues.rang = self.defilement_photos.rang
        self.vues.maj()
    
    def fin(self):
        """avancer vers la fin"""
        self.defilement_photos.acceder_dernier()
        self.vues.rang = self.defilement_photos.rang
        self.vues.maj()

    