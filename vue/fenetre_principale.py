#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
fenêtre contenant les trois zones
ainsi que les icônes et les menus
"""

from vue.zone_gauche import ZoneGauche
from vue.zone_droite_haute import ZoneDroiteHaute
from vue.zone_droite_basse import ZoneDroiteBasse
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QHBoxLayout,
                               QToolBar)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QAction
from modele.gestionnaire_BDD_personnes import GestionnaireBDDPersonnes
from pathlib import Path
from builtins import _

class FenetrePrincipale(QMainWindow):
    """Fenêtre principale de l'application."""

    def __init__(self, configuration_json, connecteur_bdd, parent=None):
        super().__init__(parent)
        self.gestionnaire_bdd = GestionnaireBDDPersonnes(connecteur_bdd)
        self.liste_personnes = self.gestionnaire_bdd.liste_personnes
        self.zone_gauche = ZoneGauche(self.liste_personnes, configuration_json)
        self.zone_droite_haute = ZoneDroiteHaute(configuration_json)
        self.zone_droite_basse = ZoneDroiteBasse(configuration_json, connecteur_bdd)
        # connecteur (zone gauche - fenêtre principale)
        self.zone_droite_basse.liste_personnes_maj.connect(self.mettre_a_jour_liste_personnes)
        self.barre = self.menuBar() # barre de menu
        # contruction de l'interface
        self.construire_interface()
        self.menu_fichiers()
        self.barre_outils()

    def construire_interface(self):
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
        """Construit le menu fichiers."""
        menu_fichiers = self.barre.addMenu(_("Fichier"))  # self.barre: barre de menu
        menu_fichiers = self.barre.addMenu(_("Aide"))


    def barre_outils(self) -> None:
        """Construit la barre d’outils principale avec ses icônes et ses actions."""
        barre_outils = QToolBar("Modes")
        barre_outils.setIconSize(QSize(32, 32))
        self.addToolBar(barre_outils)

        self.dossier_icones = Path(__file__).resolve().parent.parent / "ressources" / "fichiers" / "icones"

        
        self.act_lecture = QAction(_("Lecture"), self)
        self.act_reponse_cachee = QAction(_("Deviner puis réponse"), self)
        self.act_test_ecrit = QAction(_("Test écrit"), self)
        self.act_recherche = QAction(_("Recherche"), self)
        self.act_aleatoire = QAction(_("Mode aléatoire"), self)

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
        

    def mettre_a_jour_liste_personnes(self, liste_personnes: list) -> None:
        print("signal reçu dans FenetrePrincipale")
        print("liste reçue =", liste_personnes)

        self.liste_personnes = liste_personnes
        self.zone_gauche.liste_personnes = liste_personnes
        self.zone_gauche.index_personne = 0
        self.zone_gauche.maj()