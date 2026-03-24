#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
fenêtre contenant les trois zones
ainsi que les icônes et les menus
"""

from pathlib import Path
from builtins import _

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QAction, QActionGroup
from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QToolBar
)

from vue.zone_gauche import ZoneGauche
from vue.zone_droite_haute import ZoneDroiteHaute
from vue.zone_droite_basse import ZoneDroiteBasse

from modele.gestionnaire_bdd_personnes import GestionnaireBDDPersonnes
from modele.modele_gauche import ModeleGauche

from controleur.controleur_zone_gauche import ControleurZoneGauche
from controleur.controleur_zone_droite_haute import ControleurZoneDroiteHaute
from controleur.controleur_zone_droite_basse import ControleurZoneDroiteBasse
from controleur.controleur_toolbar import ControleurToolbar

from PySide6.QtCore import Signal, Qt


class FenetrePrincipale(QMainWindow):
    """Fenêtre principale de l'application."""

    demande_mode_lecture = Signal()
    demande_mode_reponse_cachee = Signal()
    demande_mode_test_ecrit = Signal()
    demande_mode_recherche = Signal()
    demande_mode_aleatoire = Signal()
    demande_verifier = Signal()

    def __init__(self, configuration_json, connecteur_bdd, parent=None):
        super().__init__(parent)

        self.configuration_json = configuration_json
        self.gestionnaire_bdd = GestionnaireBDDPersonnes(connecteur_bdd)
        self.liste_personnes = self.gestionnaire_bdd.liste_personnes
        # zones
        self.zone_gauche = ZoneGauche(self.liste_personnes, configuration_json, self)
        self.zone_droite_haute = ZoneDroiteHaute(configuration_json)
        self.zone_droite_basse = ZoneDroiteBasse(configuration_json, connecteur_bdd)
        # contrôleurs
        self.controleur_zone_gauche = ControleurZoneGauche(self)
        self.controleur_zone_droite_haute = ControleurZoneDroiteHaute(self)
        self.controleur_zone_droite_basse = ControleurZoneDroiteBasse(self.gestionnaire_bdd)
        
        
        # connexion zone droite basse -> mise à jour de la liste
        # self.zone_droite_basse.demande_BP_valider_ZDB.connect(self.mettre_a_jour_liste_personnes)


        # barre de menu
        self.barre = self.menuBar()
        # construction interface
        self.construire_interface()
        # definition des actions
        self.act_lecture = QAction(_("Lecture"), self)
        self.act_reponse_cachee = QAction(_("Deviner puis réponse"), self)
        self.act_test_ecrit = QAction(_("Test écrit"), self)
        self.act_recherche = QAction(_("Recherche"), self)
        self.act_aleatoire = QAction(_("Mode aléatoire"), self)
        self.act_verifier = QAction(_("Verifier"), self)
        # connexions
        self.act_lecture.triggered.connect(self.demande_mode_lecture.emit)
        self.act_reponse_cachee.triggered.connect(self.demande_mode_reponse_cachee.emit)
        self.act_test_ecrit.triggered.connect(self.demande_mode_test_ecrit.emit)
        self.act_recherche.triggered.connect(self.demande_mode_recherche.emit)
        self.act_aleatoire.triggered.connect(self.demande_mode_aleatoire.emit)
        self.act_verifier.triggered.connect(self.demande_verifier.emit)
        self.menu_fichiers()
        self.act_lecture.setEnabled(False)
        # désactiver toutes les actions
        self.act_reponse_cachee.setEnabled(False)
        self.act_test_ecrit.setEnabled(False)
        self.act_recherche.setEnabled(False)
        self.act_aleatoire.setEnabled(False)
        self.act_verifier.setEnabled(False)
        self.barre_outils()
        self.controleur_toolbar = ControleurToolbar(self)

    def construire_interface(self) -> None:
        """Construire l'interface principale."""
        widget_central = QWidget()

        layout_horizontal = QHBoxLayout()
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.zone_droite_haute)
        layout_vertical.addWidget(self.zone_droite_basse)
        layout_horizontal.addWidget(self.zone_gauche)
        layout_horizontal.addLayout(layout_vertical)
        widget_central.setLayout(layout_horizontal)
        self.setCentralWidget(widget_central)

    def barre_outils(self) -> None:
        """Construire la barre d’outils principale."""
        barre_outils = QToolBar("Modes")
        barre_outils.setIconSize(QSize(32, 32))
        barre_outils.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.addToolBar(barre_outils)

        self.dossier_icones = (
            Path(__file__).resolve().parent.parent / "ressources" / "fichiers" / "icones"
        )
        # Rendre les 4 icônes de gauche exclusives comme des boutons radio.
        self.act_lecture.setCheckable(True)
        self.act_reponse_cachee.setCheckable(True)
        self.act_test_ecrit.setCheckable(True)
        self.act_recherche.setCheckable(True)
        # Définir le groupe des 4 éléments de gauche.
        self.groupe_modes = QActionGroup(self)
        self.groupe_modes.setExclusive(True)
        # Ajouter les actions au groupe.
        self.groupe_modes.addAction(self.act_lecture)
        self.groupe_modes.addAction(self.act_reponse_cachee)
        self.groupe_modes.addAction(self.act_test_ecrit)
        self.groupe_modes.addAction(self.act_recherche)
        # Création des icônes.
        self.act_lecture.setIcon(QIcon(str(self.dossier_icones / "oeil.png")))
        self.act_reponse_cachee.setIcon(QIcon(str(self.dossier_icones / "oeil_cache.png")))
        self.act_test_ecrit.setIcon(QIcon(str(self.dossier_icones / "crayon.png")))
        self.act_recherche.setIcon(QIcon(str(self.dossier_icones / "question.png")))
        self.act_aleatoire.setIcon(QIcon(str(self.dossier_icones / "aleatoire.png")))
        self.act_verifier.setIcon(QIcon(str(self.dossier_icones / "verifier.png")))
        # Ajouter les bulles d'information.
        self.act_lecture.setToolTip(_("Lire les noms et prénoms"))
        self.act_reponse_cachee.setToolTip(_("Deviner puis afficher la réponse"))
        self.act_test_ecrit.setToolTip(_("Test écrit"))
        self.act_recherche.setToolTip(_("Rechercher une personne"))
        self.act_aleatoire.setToolTip(_("Mode aléatoire"))
        self.act_verifier.setToolTip(_("Valider les modes"))
        # Ajouter les actions dans la barre d’outils.
        barre_outils.addAction(self.act_lecture)
        barre_outils.addAction(self.act_reponse_cachee)
        barre_outils.addAction(self.act_test_ecrit)
        barre_outils.addAction(self.act_recherche)
        barre_outils.addSeparator()
        barre_outils.addAction(self.act_aleatoire)
        barre_outils.addSeparator()
        barre_outils.addAction(self.act_verifier)
        # Sélectionner l’icône par défaut.
        self.act_lecture.setChecked(True)

    def menu_fichiers(self) -> None:
        """Construire le menu."""
        self.barre.addMenu(_("Fichier"))
        self.barre.addMenu(_("Aide"))

    def mettre_a_jour_liste_personnes(self, liste_personnes: list) -> None:
        """Mettre à jour la liste affichée dans la zone gauche."""
        self.zone_gauche.liste_personnes = liste_personnes
        self.zone_gauche.rang = 0
        self.zone_gauche.nbre_pers = len(liste_personnes)

        self.controleur_zone_gauche.modele_gauche = ModeleGauche(liste_personnes)
        self.zone_gauche.maj()
        self.activer_actions()

    def activer_actions(self) -> None:
        """activer les actions"""
        self.act_lecture.setEnabled(True)
        self.act_reponse_cachee.setEnabled(True)
        self.act_test_ecrit.setEnabled(True)
        self.act_recherche.setEnabled(True)
        self.act_aleatoire.setEnabled(True)
        self.act_verifier.setEnabled(True)
        print("activer_actions appelée")