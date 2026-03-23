#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
Choix de la structure et de la spécialité.
"""

from pathlib import Path

from PySide6.QtWidgets import QWidget, QComboBox, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal

from modele.textes_interface import libelle
from modele.gestionnaire_bdd_personnes import GestionnaireBDDPersonnes
from controleur.controleur_zone_droite_basse import ControleurZoneDroiteBasse


DOSSIER_PROJET = Path(__file__).resolve().parent.parent


class ZoneDroiteBasse(QWidget):

    # Signal émis lorsque la liste filtrée de personnes est prête.
    demande_BP_valider_ZD = Signal(list)

    def __init__(self, configuration_json, connecteur_bdd):
        super().__init__()
        self.configuration_json = configuration_json
        self.gestionnaire_bdd_personnes = GestionnaireBDDPersonnes(connecteur_bdd)
        self.layout_principal = QVBoxLayout()
        self.controleur_combo_box = ControleurZoneDroiteBasse(self.gestionnaire_bdd_personnes)
        self.liste_personnes = []
        self.liste_personnes_filtree = []  # liste final de la liste des personnes
        self.liste_specialites = []
        self.specialite_selectionnee = "TOUS"
        self.initialiser()

    def initialiser(self):
        """Initialisation des widgets et des connexions."""
        # Grille principale : structure / spécialité
        layout_grille = QGridLayout()
        layout_grille.setHorizontalSpacing(12)
        layout_grille.setVerticalSpacing(3)
        layout_grille.setContentsMargins(0, 0, 0, 0)
        layout_grille.setAlignment(Qt.AlignTop)
        # Labels
        label_structure = QLabel(_(libelle(self.configuration_json["Structure"])))
        label_specialite = QLabel(_(libelle(self.configuration_json["Specialite"])))
        # Combobox
        self.comboBox_Gauche = QComboBox()
        self.comboBox_droite = QComboBox()
        # Placement dans la grille
        layout_grille.addWidget(label_structure, 0, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout_grille.addWidget(label_specialite, 0, 1, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout_grille.addWidget(self.comboBox_Gauche, 1, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        layout_grille.addWidget(self.comboBox_droite, 1, 1, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.layout_principal.addLayout(layout_grille)
        # Bouton de validation
        valider_style = """
            QPushButton {
                background-color: #76aeba;
                border: 1px solid #558b9e;
                border-radius: 6px;
                padding: 6px 14px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #66a0b0;
            }
            QPushButton:pressed {
                background-color: #5c8c9c;
            }
        """
        self.bouton_valider = QPushButton(_("Valider"))
        self.bouton_valider.setFixedWidth(120)
        self.bouton_valider.setStyleSheet(valider_style)
        self.bouton_valider.setToolTip(_("Valider la liste choisie"))
        layout_bouton = QHBoxLayout()
        layout_bouton.addWidget(self.bouton_valider)
        self.layout_principal.addSpacing(10)
        self.layout_principal.addLayout(layout_bouton)
        self.setLayout(self.layout_principal)
        # Chargement des structures disponibles pour l'interface
        structures_ui = self.controleur_combo_box.recuperer_structures_ui(self.configuration_json)
        self.comboBox_Gauche.addItems(structures_ui)
        # Connexions des signaux
        self.comboBox_Gauche.currentTextChanged.connect(self.choisir_structure_specialites)
        self.comboBox_droite.currentTextChanged.connect(self.choisir_specialite)
        self.bouton_valider.clicked.connect(self.valider_choix)
        # Émission initiale de la liste courante
        #self.demande_BP_valider_ZD.emit(self.liste_personnes)
        # Initialisation de la combobox des spécialités
        self.creer_combo_specialites()

    def choisir_structure_specialites(self) -> None:
        """Met à jour les personnes et les spécialités selon la structure choisie."""
        structure_choisie = self.comboBox_Gauche.currentText()

        self.liste_personnes, self.liste_specialites = (
            self.controleur_combo_box.choisir_structure_specialites(structure_choisie)
        )

        self.creer_combo_specialites()

    def creer_combo_specialites(self) -> None:
        """Remplit la combobox des spécialités."""
        self.comboBox_droite.clear()
        self.comboBox_droite.addItems(self.liste_specialites)
        self.comboBox_droite.setCurrentIndex(0)

    def choisir_specialite(self) -> None:
        """Met à jour la spécialité sélectionnée."""
        self.specialite_selectionnee = self.comboBox_droite.currentText()

    def valider_choix(self) -> None:
        """Filtrer la liste des personnes selon le choix utilisateur."""
        specialite_selectionnee = self.comboBox_droite.currentText().strip()

        if specialite_selectionnee == "TOUS":
            self.liste_personnes_filtree = self.liste_personnes.copy()
        else:
            self.liste_personnes_filtree = [
                personne for personne in self.liste_personnes
                if specialite_selectionnee in personne[3]
            ]

        print("specialite_selectionnee =", specialite_selectionnee)
        print("---------------------------------")
        print("nb personnes filtrées =", len(self.liste_personnes_filtree))
        print("liste_traitée:")
        print(self.liste_personnes_filtree)
        self.demande_BP_valider_ZD.emit(self.liste_personnes_filtree)
        print("nb personnes filtrées =", len(self.liste_personnes_filtree))
        print("-----------------------")