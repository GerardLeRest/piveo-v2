#!/usr/bin/python3
# -*- coding: utf-8 -*-

from controleur.controleur_zone_gauche import ControleurZoneGauche
from controleur.controleur_zone_droite_haute import ControleurZoneDroiteHaute
from controleur.controleur_zone_droite_basse import ControleurZoneDroiteBasse
from PySide6.QtCore import Slot


class ControleurGeneral:
    def __init__(self, vue, gestionnaire_bdd):
        self.vue = vue
        self.gestionnaire_bdd = gestionnaire_bdd

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

        # connexions des modes (boutons/menus)
        self.vue.demande_mode_lecture.connect(self.mode_lecture)
        self.vue.demande_mode_deviner.connect(self.mode_deviner)
        self.vue.demande_mode_ecrit.connect(self.mode_ecrit)
        self.vue.demande_mode_recherche.connect(self.mode_recherche)

        # bouton valider : rediriger vers écrit ou recherche selon le mode
        self.vue.zone_droite_haute.demande_valider.connect(self.action_valider)

    @Slot()
    def action_valider(self) -> None:
        """Choisir entre validation écrite et recherche."""
        if self.vue.act_ecrit.isChecked():
            self.controleur_zone_droite_haute.valider()

        elif self.vue.act_recherche.isChecked():
            liste = self.vue.zone_droite_basse.liste_personnes.copy()
            liste_personnes = self.controleur_zone_droite_haute.rechercher_personnes(liste)
            self.controleur_zone_gauche.charger_liste(liste_personnes, "recherche")

    def mode_lecture(self) -> None:
        """Activer le mode lecture."""
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        self.controleur_zone_gauche.charger_liste(liste, "mode")

    def mode_deviner(self) -> None:
        """Activer le mode deviner."""
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        liste = self.controleur_zone_gauche.devinner_reponses(liste)
        self.controleur_zone_gauche.charger_liste(liste, "deviner")

    def mode_ecrit(self) -> None:
        """Activer le mode écrit."""
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        self.controleur_zone_gauche.charger_liste(liste, "ecrit")

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
        # nettoyage de la zone de saisie
        self.vue.zone_droite_haute.effacer_reponses()
        self.vue.zone_droite_haute.cacher_image_check()

        # charger la liste de départ
        liste = self.vue.zone_droite_basse.liste_personnes_filtree.copy()
        self.controleur_zone_gauche.charger_liste(liste, "recherche")

    def mettre_a_jour_liste_personnes(self, liste_personnes: list) -> None:
        """Transmettre la liste au contrôleur de zone gauche."""
        self.controleur_zone_gauche.charger_liste(liste_personnes, None)