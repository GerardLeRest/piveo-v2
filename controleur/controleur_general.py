#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
            self.vue, self.controleur_zone_gauche
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
        self.vue.zone_droite_haute.desactiver_boutons()



        # connexions des modes (boutons/menus)
        self.vue.demande_mode_lecture.connect(self.mode_lecture)
        self.vue.demande_mode_deviner.connect(self.mode_deviner)
        self.vue.demande_mode_ecrit.connect(self.mode_ecrit)
        self.vue.demande_mode_recherche.connect(self.mode_recherche)
        self.vue.demande_mode_aleatoire.connect(self.mode_aleatoire)

        # bouton valider
        self.vue.zone_droite_haute.demande_valider.connect(self.action_valider)

        
    @Slot()
    def action_valider(self) -> None:
        """Traiter le bouton Valider selon le mode courant."""
        if self.mode == "ecrit":
            self.controleur_zone_droite_haute.valider()

        elif self.mode == "recherche":
            liste = self.gestionnaire_bdd.charger_personnes()
            liste_personnes = self.controleur_zone_droite_haute.rechercher_personnes(liste)
            self.controleur_zone_gauche.charger_liste(liste_personnes, "recherche")

    def mode_lecture(self) -> None:
        """Activer le mode lecture."""
        # activer/désactiver bouton
        self.mode = "lecture"
        print("mode_lecture")
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        # act/désac des boutons
        self.vue.zone_gauche.activer_boutons()
        self.vue.zone_droite_haute.desactiver_boutons()
        if self.aleatoire:
            random.shuffle(liste)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

    def mode_deviner(self) -> None:
        """Activer le mode deviner."""
        self.mode = "deviner"
        # act/désac des boutons
        self.vue.zone_gauche.activer_boutons()
        self.vue.zone_droite_haute.desactiver_boutons()
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        if self.aleatoire:
            random.shuffle(liste)
        liste = self.controleur_zone_gauche.deviner_reponses(liste)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

    def mode_ecrit(self) -> None:
        """Activer le mode écrit."""
        self.mode = "ecrit"
        # act/désac des boutons
        self.vue.zone_gauche.desactiver_boutons()
        self.vue.zone_droite_haute.activer_boutons()
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        if self.aleatoire:
            random.shuffle(liste)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

        # activer les cases de vérification
        self.vue.zone_droite_haute.verification_prenom.setEnabled(True)
        self.vue.zone_droite_haute.verification_nom.setEnabled(True)

        # cocher les cases
        self.vue.zone_droite_haute.verification_prenom.setChecked(True)
        self.vue.zone_droite_haute.verification_nom.setChecked(True)

        # remettre la zone propre
        self.vue.zone_droite_haute.activer_boutons()
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.cacher_image_check()

    def mode_recherche(self) -> None:
        """Activer le mode recherche."""
        self.mode = "recherche"
        # act/désac des boutons
        self.vue.zone_gauche.desactiver_boutons()
        self.vue.zone_droite_haute.bout_valider.setEnabled(True)
        self.vue.zone_droite_haute.bout_effacer.setEnabled(False) 
        self.vue.zone_droite_haute.bout_suite.setEnabled(False)
        # champs et image
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.cacher_image_check()

        liste = self.gestionnaire_bdd.charger_personnes() # récupération de toutes les pesrsonnes (BDD)
        self.controleur_zone_gauche.charger_liste(liste, self.mode)

    def mettre_a_jour_liste_personnes(self, liste_personnes: list) -> None:
        """Réception de la liste filtrée."""
        # on met à jour la liste dans la vue (important)
        self.vue.zone_droite_basse.liste_personnes_filtree = liste_personnes
        # on lance le mode lecture seulement maintenant
        self.mode_lecture()

    def mode_aleatoire(self, etat: bool) -> None:
        """indiquer l'état aléatoire"""
        self.aleatoire = etat
        if self.mode == "lecture":
            self.mode_lecture()
        elif self.mode =="deviner":
            self.mode_deviner()
        elif self.mode == "ecrit":
            self.mode_ecrit()