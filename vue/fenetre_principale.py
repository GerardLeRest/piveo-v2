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
    QToolBar,
)

from vue.zone_gauche import ZoneGauche
from vue.zone_droite_haute import ZoneDroiteHaute
from vue.zone_droite_basse import ZoneDroiteBasse

from modele.gestionnaire_BDD import GestionnaireBDD
from controleur.controleur_general import ControleurGeneral
from PySide6.QtCore import Signal

class FenetrePrincipale(QMainWindow):
    """Fenêtre principale de l'application."""

    demande_mode_lecture = Signal()

    def __init__(self, configuration_json, connecteur_bdd, parent=None):
        super().__init__(parent)

        self.configuration_json = configuration_json
        self.gestionnaire_bdd = GestionnaireBDD(connecteur_bdd)
        self.liste_personnes = self.gestionnaire_bdd.liste_personnes
        # zones
        self.zone_gauche = ZoneGauche(self.liste_personnes, configuration_json)
        self.zone_droite_haute = ZoneDroiteHaute(configuration_json)
        self.zone_droite_basse = ZoneDroiteBasse(configuration_json, connecteur_bdd)
        # contrôleurs
        self.controleur_general = ControleurGeneral(self, self.gestionnaire_bdd)
        self.controleur_zone_gauche = self.controleur_general.controleur_zone_gauche
        self.controleur_zone_droite_haute = self.controleur_general.controleur_zone_droite_haute
        self.controleur_zone_droite_basse = self.controleur_general.controleur_zone_droite_basse

        # connexion zone droite basse -> mise à jour de la liste
        self.zone_droite_basse.liste_personnes_maj.connect(self.controleur_general.mettre_a_jour_liste_personnes)

        # barre de menu
        self.barre = self.menuBar()
        # construction interface
        self.construire_interface()
        self.menu_fichiers()
        self.barre_outils()

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

    def menu_fichiers(self) -> None:
        """Construire le menu."""
        self.barre.addMenu(_("Fichier"))
        self.barre.addMenu(_("Aide"))

    def barre_outils(self) -> None:
        """Construire la barre d’outils principale."""
        barre_outils = QToolBar("Modes")
        barre_outils.setIconSize(QSize(32, 32))
        self.addToolBar(barre_outils)

        self.dossier_icones = (
            Path(__file__).resolve().parent.parent / "ressources" / "fichiers" / "icones"
        )

        self.act_lecture = QAction(_("Lecture"), self)
        self.act_reponse_cachee = QAction(_("Deviner puis réponse"), self)
        self.act_test_ecrit = QAction(_("Test écrit"), self)
        self.act_recherche = QAction(_("Recherche"), self)
        self.act_aleatoire = QAction(_("Mode aléatoire"), self)

        self.act_lecture.setCheckable(True)
        self.act_reponse_cachee.setCheckable(True)
        self.act_test_ecrit.setCheckable(True)
        self.act_recherche.setCheckable(True)
        self.act_aleatoire.setCheckable(True)

        self.groupe_modes = QActionGroup(self)
        self.groupe_modes.setExclusive(True)
        self.groupe_modes.addAction(self.act_lecture)
        self.groupe_modes.addAction(self.act_reponse_cachee)
        self.groupe_modes.addAction(self.act_test_ecrit)
        self.groupe_modes.addAction(self.act_recherche)

        self.act_lecture.setIcon(QIcon(str(self.dossier_icones / "oeil.svg")))
        self.act_reponse_cachee.setIcon(QIcon(str(self.dossier_icones / "oeil_cache.svg")))
        self.act_test_ecrit.setIcon(QIcon(str(self.dossier_icones / "crayon.svg")))
        self.act_recherche.setIcon(QIcon(str(self.dossier_icones / "question.svg")))
        self.act_aleatoire.setIcon(QIcon(str(self.dossier_icones / "aleatoire.svg")))

        barre_outils.addAction(self.act_lecture)
        barre_outils.addAction(self.act_reponse_cachee)
        barre_outils.addAction(self.act_test_ecrit)
        barre_outils.addAction(self.act_recherche)
        barre_outils.addAction(self.act_aleatoire)

        self.act_lecture.setToolTip(_("Lire les noms et prénoms"))
        self.act_reponse_cachee.setToolTip(_("Deviner puis afficher la réponse"))
        self.act_test_ecrit.setToolTip(_("Test écrit"))
        self.act_recherche.setToolTip(_("Rechercher une personne"))
        self.act_aleatoire.setToolTip(_("Mode aléatoire"))

        # sélectionner l'cone "lecture"
        self.act_lecture.setChecked(True)
        # connexion mode lecture
        self.act_lecture.triggered.connect(self.demande_mode_lecture.emit)