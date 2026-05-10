#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur général
"""

from controleur.controleur_zone_gauche import ControleurZoneGauche
from controleur.controleur_zone_droite_haute import ControleurZoneDroiteHaute
from controleur.controleur_zone_droite_basse import ControleurZoneDroiteBasse
from PySide6.QtCore import Slot
import random

class ControleurGeneral:
    def __init__(self, vue, gestionnaire_bdd):
        self.vue = vue
        self.gestionnaire_bdd = gestionnaire_bdd
        self.mode = ""
        self.aleatoire : bool=False

        # Construction des trois contrôleurs locaux
        self.controleur_zone_gauche = ControleurZoneGauche(self.vue)
        self.controleur_zone_droite_haute = ControleurZoneDroiteHaute(
            self.vue,
            self.controleur_zone_gauche,
            self.gestionnaire_bdd
        )
        self.controleur_zone_droite_basse = ControleurZoneDroiteBasse(
            self.gestionnaire_bdd
        )

        # initialisation des checkbox
        self.vue.zone_droite_haute.verification_prenom.setEnabled(True)
        self.vue.zone_droite_haute.verification_nom.setEnabled(True)

        self.vue.zone_droite_haute.verification_prenom.setChecked(True)
        self.vue.zone_droite_haute.verification_nom.setChecked(True)

        # act/désac des boutons
        self.vue.zone_gauche.activer_boutons()
        self.vue.zone_droite_haute.desactiver_boutons_champs()

        
        # connexions des modes (boutons/menus)
        self.vue.demande_mode_lecture.connect(self.mode_lecture)
        self.vue.demande_mode_deviner.connect(self.mode_deviner)
        self.vue.demande_mode_ecrit.connect(self.mode_ecrit)
        self.vue.demande_mode_recherche.connect(self.mode_recherche)
        self.vue.demande_mode_aleatoire.connect(self.mode_aleatoire)

        self.mode_lecture() # bug à la mise sous tension

        
    def mode_lecture(self) -> None:
        """Activer le mode lecture."""
        # activer/désactiver bouton
        self.mode = "lecture"
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        # act/désac des boutons
        self.vue.zone_gauche.activer_boutons()
        self.vue.zone_droite_haute.desactiver_boutons_champs()
        if self.aleatoire:
            random.shuffle(liste)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

    def mode_deviner(self) -> None:
        """Activer le mode deviner."""
        self.mode = "deviner"
        # act/désac des boutons
        self.vue.zone_gauche.activer_boutons()
        self.vue.zone_droite_haute.desactiver_boutons_champs()
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        if self.aleatoire:
            random.shuffle(liste)
        liste = self.controleur_zone_gauche.deviner_reponses(liste)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

    def mode_ecrit(self) -> None:
        """Activer le mode écrit."""
        self.mode = "ecrit"
        self.controleur_zone_droite_haute.nbre_bonnes_rep = 0
        # act/désac des boutons
        self.vue.zone_gauche.desactiver_boutons()
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        if self.aleatoire:
            random.shuffle(liste)
        # voir mode deviner
        liste = self.controleur_zone_gauche.deviner_reponses(liste)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)
        # activer les cases de vérification
        self.vue.zone_droite_haute.verification_prenom.setEnabled(True)
        self.vue.zone_droite_haute.verification_nom.setEnabled(True)
        # cocher les cases
        self.vue.zone_droite_haute.verification_prenom.setChecked(True)
        self.vue.zone_droite_haute.verification_nom.setChecked(True)
        # remettre la zone propre
        if liste:
            self.vue.zone_droite_haute.activer_boutons_champs()
        else:
            self.vue.zone_droite_haute.desactiver_boutons_champs()
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.cacher_image_check()

    def mode_recherche(self) -> None:
        """Activer le mode recherche."""
        self.mode = "recherche"
        # act/désac des boutons
        self.vue.zone_droite_haute.activer_boutons_champs()
        self.vue.zone_gauche.activer_boutons()
        self.vue.zone_droite_haute.bout_effacer.setEnabled(True) 
        self.vue.zone_droite_haute.bout_suite.setEnabled(False)
        # champs et image
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.cacher_image_check()
        self.vue.zone_droite_haute.gestion_focus()
        liste = self.gestionnaire_bdd.charger_personnes() # récupération de toutes les personnes (BDD)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

    def mettre_a_jour_liste_personnes(self, liste_personnes: list) -> None:
        """Réception de la liste filtrée."""
        self.vue.zone_droite_basse.liste_personnes_filtree = liste_personnes
        if self.mode == "lecture":
            self.mode_lecture()
        elif self.mode == "deviner":
            self.mode_deviner()
        elif self.mode == "ecrit":
            self.mode_ecrit()
        elif self.mode == "rechercher":
            self.mode_rechercher()

    def mode_aleatoire(self, etat: bool) -> None:
        """indiquer l'état aléatoire"""
        self.aleatoire = etat
        if self.mode == "lecture":
            self.mode_lecture()
        elif self.mode =="deviner":
            self.mode_deviner()
        elif self.mode == "ecrit":
            self.mode_ecrit()

    @Slot()
    def suite(self) -> None:
        """Traiter le bouton Suite."""
        self.controleur_zone_droite_haute.suite()