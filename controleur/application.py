#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
lien entre les modèles et les vues
"""

from modele.defilement_photos import DefilementPhotos
from modele.prenom_nom import PrenomNom
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap


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
        self.vue.zone_droite_haute.demande_etat_prenom.connect(self.widgets_prenom) 
        self.vue.zone_droite_haute.demande_etat_nom.connect(self.widgets_nom)
        self.vue.zone_droite_haute.demande_valider.connect(self.recuperation_ecrite)
    
    @Slot()
    def avancer(self)->None:
        print("avancer")
        self.defilement_photos.acceder_suivant()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def reculer(self)->None:
        """reculer vers la gauche"""
        self.defilement_photos.acceder_precedent()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def debut(self)->None:
        """aller au début"""
        self.defilement_photos.acceder_premier()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot()
    def fin(self)->None:
        """aller à la fin"""
        self.defilement_photos.acceder_dernier()
        self.vue.zone_gauche.rang = self.defilement_photos.rang
        self.vue.zone_gauche.maj()

    @Slot(bool)
    def widgets_prenom(self, etat:bool)->None:
        "mettre à jour / désactiner le champs prenom de zone_gauche.prenom"
        if etat:
            self.vue.zone_gauche.prenom.setEnabled(True)
            self.vue.zone_gauche.prenom.setText("Prénom")
        else:
            self.vue.zone_gauche.prenom.setText("")
            self.vue.zone_gauche.prenom.setEnabled(False)

    @Slot(bool)
    def widgets_nom(self, etat:bool)->None:
        "mettre à jour / désactiner le champs prenom de zone_gauche.prenom"
        if etat:
            self.vue.zone_gauche.nom.setEnabled(True)
            self.vue.zone_gauche.nom.setText("Nom")
        else:
            self.vue.zone_gauche.nom.setText("")
            self.vue.zone_gauche.nom.setEnabled(False)

    @Slot()
    def recuperation_ecrite(self)->None:
        """récupération prenom/nom"""
        print("recuperation_ecrite")
        prenom = self.vue.zone_droite_haute.prenom_entree.text()
        nom = self.vue.zone_droite_haute.nom_entree.text()
        self.prenom_nom = PrenomNom(prenom,nom)
        print(f"prenom: {self.prenom_nom.comparer_prenom(prenom)}")
        print(f"nom: {self.prenom_nom.comparer_nom(nom)}")
        resultat_prenom = self.prenom_nom.comparer_prenom(prenom)
        resultat_nom = self.prenom_nom.comparer_nom(nom)
        self.vue.zone_droite_haute.afficher_image_check(resultat_prenom, resultat_nom)






           
            