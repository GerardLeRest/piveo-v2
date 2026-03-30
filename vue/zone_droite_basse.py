#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
Choix de la structure et de la spécialité.
"""

from pathlib import Path

from PySide6.QtWidgets import ( QWidget, QComboBox, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout,
                                QPushButton, QSizePolicy, QFrame)
from PySide6.QtCore import Qt, Signal

from modele.textes_interface import libelle
from modele.gestionnaire_BDD import GestionnaireBDD
from controleur.controleur_zone_droite_basse import ControleurZoneDroiteBasse


DOSSIER_PROJET = Path(__file__).resolve().parent.parent


class ZoneDroiteBasse(QWidget):

    # Signal émis lorsque la liste filtrée de personnes est prête.
    demande_envoi_liste_personnes = Signal(list)

    def __init__(self, configuration_json, connecteur_bdd):
        super().__init__()
        self.configuration_json = configuration_json
        self.gestionnaire_bdd_personnes = GestionnaireBDD(connecteur_bdd)
        self.layout_principal = QVBoxLayout()
        self.controleur_combo_box = ControleurZoneDroiteBasse(self.gestionnaire_bdd_personnes)
        self.liste_personnes = []
        self.liste_personnes_filtree = []
        self.liste_specialites = []
        self.specialite_selectionnee = "TOUS"
        self.initialiser()

    def initialiser(self):
        """Initialisation des widgets et des connexions."""
        # Layout principal de la zone droite basse
        layout_bas_droit = QVBoxLayout()
        layout_bas_droit.setContentsMargins(0, 0, 0, 0)
        # Labels
        label_classe = QLabel("Classe")
        label_options = QLabel("Options")
        # Combobox
        self.comboBox_Gauche = QComboBox()
        self.comboBox_droite = QComboBox()
        self.comboBox_Gauche.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.comboBox_droite.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.comboBox_Gauche.setMinimumHeight(32)
        self.comboBox_droite.setMinimumHeight(32)
        # Bouton
        self.bouton_valider = QPushButton("Confirm")
        self.bouton_valider.setFixedWidth(140)
        self.bouton_valider.setMinimumHeight(32)
        self.bouton_valider.setFixedWidth(180)
        self.bouton_valider.setObjectName("bouton_action")
        # Grille
        grille_choix = QGridLayout()
        grille_choix.setContentsMargins(0, 0, 0, 0)
        grille_choix.setHorizontalSpacing(12)
        grille_choix.setVerticalSpacing(13)
        grille_choix.setRowMinimumHeight(2, 35)

        grille_choix.addWidget(label_classe, 0, 0)
        grille_choix.addWidget(label_options, 0, 1)
        grille_choix.addWidget(self.comboBox_Gauche, 1, 0)
        grille_choix.addWidget(self.comboBox_droite, 1, 1)
        grille_choix.addWidget(self.bouton_valider, 2, 0, 1, 2, alignment=Qt.AlignHCenter | Qt.AlignBottom)

        grille_choix.setColumnStretch(0, 1)
        grille_choix.setColumnStretch(1, 1)
        layout_bas_droit.addLayout(grille_choix)
        layout_bas_droit.addStretch()
        self.setLayout(layout_bas_droit)
        # Chargement des structures disponibles pour l'interface
        structures_ui = self.controleur_combo_box.recuperer_structures_ui(self.configuration_json)
        self.comboBox_Gauche.addItems(structures_ui)
        # Connexions des signaux
        self.comboBox_Gauche.currentTextChanged.connect(self.choisir_structure_specialites)
        self.comboBox_droite.currentTextChanged.connect(self.choisir_specialite)
        self.bouton_valider.clicked.connect(self.valider_choix)
        # Émission initiale de la liste courante
        self.demande_envoi_liste_personnes.emit(self.liste_personnes)
        # Initialisation de la combobox des spécialités
        self.creer_combo_specialites()
        # Style du bouton
        self.setStyleSheet("""
        QPushButton#bouton_action {
            background-color: #7daeb8;
            color: white;
            border: 1px solid #6b9aa3;
            border-radius: 12px;
            font-weight: bold;
            padding: 6px 12px;
        }

        QPushButton#bouton_action:hover {
            background-color: #8bbbc4;
        }

        QPushButton#bouton_action:pressed {
            background-color: #6d9ea8;
        }
        """)

    def choisir_structure_specialites(self, texte: str) -> None:
        """Met à jour les personnes et les spécialités selon la structure choisie."""
        structure_choisie = texte
        print("structure choisie =", structure_choisie)

        self.liste_personnes, self.liste_specialites = (
            self.controleur_combo_box.choisir_structure_specialites(structure_choisie)
        )

        print("liste_personnes =", self.liste_personnes)
        print("liste_specialites =", self.liste_specialites)

        self.creer_combo_specialites()

    def creer_combo_specialites(self) -> None:
        """Remplit la combobox des spécialités."""
        self.comboBox_droite.clear()
        self.comboBox_droite.addItems(self.liste_specialites)
        self.comboBox_droite.setCurrentIndex(0)

    def choisir_specialite(self, texte: str) -> None:
        """Met à jour la spécialité sélectionnée."""
        self.specialite_selectionnee = texte

    def valider_choix(self) -> None:
        """Valider la structure et la spécialité choisies."""
        self.specialite_selectionnee = self.comboBox_droite.currentText()

        print("valider_choix lancé")
        print("specialite_selectionnee =", self.specialite_selectionnee)

        if self.specialite_selectionnee == "TOUS":
            self.liste_personnes_filtree = self.liste_personnes
        else:
            self.liste_personnes_filtree = [
                personne for personne in self.liste_personnes
                if self.specialite_selectionnee in personne[3]
            ]

        print("liste envoyée =", self.liste_personnes_filtree)
        self.demande_envoi_liste_personnes.emit(self.liste_personnes_filtree)