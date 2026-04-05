#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Rechercher une ou plusieurs personnes dans
l'établissement ou effectuer un test écrit.
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QHBoxLayout,
    QPushButton, QApplication, QFrame, QCheckBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, Qt

# ⚠️ IMPORTANT
# fonctionnement global
from builtins import _
# tester la classe
# python3 -m vue.zone_droite_haute (test de la classe)
# _ = lambda x: x

import os
import sys


REPERTOIRE_RACINE = os.path.dirname(os.path.abspath(__file__))  # répertoire du fichier py


class ZoneDroiteHaute(QWidget):
    """Créer la partie droite haute de l'interface."""

    # Signaux utiles vers le contrôleur
    demande_valider = Signal()
    demande_effacer = Signal ()
    demande_suite = Signal()

    demande_activation_nom = Signal(bool)
    demande_activation_prenom = Signal(bool)

    def __init__(self, configuration_json, fenetre=None) -> None:
        """Constructeur de la zone droite haute."""
        super().__init__(fenetre)
        # configuration générale de l'interface (json)
        self.configuration_json = configuration_json
        # layout principal de la zone droite haute
        self.layout_droit_haut = QVBoxLayout()
        # création des différentes parties
        self.partie_prenom()
        self.partie_nom()
        self.partie_boutons()
        self.partie_icones()
        # état initial des widgets
        self.etat_initial()
        # attacher le layout principal au widget
        self.setLayout(self.layout_droit_haut)
        self.desactiver_boutons_champs()

    def partie_prenom(self) -> None:
        """Créer la zone du prénom."""
        # céation de la grille
        self.layout_grille = QGridLayout()
        # label nom
        self.label_prenom = QLabel(_("Prénom"))
        self.layout_grille.addWidget(self.label_prenom, 0, 0)
        # champs prenom_entree
        self.prenom_entree = QLineEdit()
        self.prenom_entree.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 4px 8px;
            }
        """)
        self.prenom_entree.setPlaceholderText(_("Indiquez votre prénom"))
        self.layout_grille.addWidget(self.prenom_entree, 0, 1)
        self.prenom_entree.returnPressed.connect(self.action_retour_prenom)
        # checkbox prenom
        self.verification_prenom = QCheckBox()
        self.layout_grille.addWidget(self.verification_prenom, 0, 2)
        self.verification_prenom.stateChanged.connect(self.etat_widgets_prenom)
        self.prenom_entree.returnPressed.connect(self.entree_sur_prenom)

    def partie_nom(self) -> None:
        """Créer la zone du nom."""
        # label nom
        self.label_nom = QLabel(_("Nom"))
        self.layout_grille.addWidget(self.label_nom, 1, 0)
        # champs nom_entree
        self.nom_entree = QLineEdit()
        self.nom_entree.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 4px 8px;
            }
        """)
        # champs
        self.nom_entree.setPlaceholderText(_("Indiquez votre nom"))
        self.layout_grille.addWidget(self.nom_entree, 1, 1)
        self.nom_entree.returnPressed.connect(self.demande_valider.emit)
        # checkbox
        self.verification_nom = QCheckBox()
        self.layout_grille.addWidget(self.verification_nom, 1, 2)
        self.verification_nom.stateChanged.connect(self.etat_widgets_nom)
        # ajout du layout self.layout_grille
        self.layout_droit_haut.addLayout(self.layout_grille)
        self.layout_droit_haut.addSpacing(5)


    def action_retour_prenom(self) -> None:
        """Entrée dans prénom : focus sur nom si demandé, sinon validation."""
        if self.verification_nom.isChecked():
            self.nom_entree.setFocus()
        else:
            self.demande_valider.emit()

    def partie_boutons(self) -> None:
        """Créer la zone des boutons."""
        # style du bouton valider
        valider_style = """
            QPushButton {
                background-color: #76aeba;
                border: 1px solid #558b9e;
                border-radius: 12px;
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
        # style du bouton effacer
        effacer_style = """
            QPushButton {
                background-color: #cfd8dc;
                border: 1px solid #b0bec5;
                border-radius: 12px;
                padding: 6px 14px;
                color: #1f2f2f;
            }
            QPushButton:hover {
                background-color: #c0ccd1;
            }
            QPushButton:pressed {
                background-color: #b0bec5;
            }
        """
        # style du bouton suite
        suite_style = """
            QPushButton {
                background-color: #7aaeb1;
                border: 1px solid #5f9ea0;
                border-radius: 12px;
                padding: 6px 14px;
                color: #1f2f2f;
            }
            QPushButton:hover {
                background-color: #6b9da0;
            }
            QPushButton:pressed {
                background-color: #5c8c8f;
            }
        """
        # layout horizontal des boutons
        layout_boutons = QHBoxLayout()
        # bouton valider
        self.bout_valider = QPushButton(_("Valider"), self)
        self.bout_valider.setStyleSheet(valider_style)
        self.bout_valider.clicked.connect(self.demande_valider.emit)
        layout_boutons.addWidget(self.bout_valider)
        # bouton effacer
        self.bout_effacer = QPushButton(_("Effacer"), self)
        self.bout_effacer.setStyleSheet(effacer_style)
        self.bout_effacer.clicked.connect(self.effacer_reponses)
        layout_boutons.addWidget(self.bout_effacer)
        # bouton suite
        self.bout_suite = QPushButton(_("Suite"), self)
        self.bout_suite.setStyleSheet(suite_style)
        self.bout_suite.clicked.connect(self.demande_suite.emit)
        layout_boutons.addWidget(self.bout_suite)
        # liste pratique pour activer/désactiver les boutons en bloc
        self.boutons = [self.bout_valider, self.bout_effacer, self.bout_suite]
        # ajout au layout principal
        self.layout_droit_haut.addSpacing(10)
        self.layout_droit_haut.addLayout(layout_boutons)
   
    def partie_icones(self) -> None:
        """Créer la zone d'affichage de l'icône et du score."""
        # layout horizontal du bas
        layout_images = QHBoxLayout()
        # image de validation (check ou cross)
        self.label_image_gauche = QLabel()
        self.label_image_gauche.setFixedSize(40, 40)
        layout_images.addWidget(self.label_image_gauche)
        # espace flexible entre image et score
        layout_images.addStretch()
        # affichage du nombre de bonnes réponses
        self.nbre_rep = QLabel(_("0/0"))
        self.nbre_rep.setStyleSheet("color: #6c7a80; font-size: 30px;")
        self.nbre_rep_exactes = 0
        layout_images.addWidget(self.nbre_rep)
        # ajout au layout principal
        self.layout_droit_haut.addLayout(layout_images)
        self.layout_droit_haut.addSpacing(10)
        # ligne horizontale de séparation
        ligne = QFrame()
        ligne.setFrameShape(QFrame.HLine)
        ligne.setFrameShadow(QFrame.Plain)
        ligne.setLineWidth(1)
        ligne.setStyleSheet("color: black;")
        self.layout_droit_haut.addWidget(ligne)

    def activer_boutons_champs(self) -> None:
        """Activer les boutons."""
        for bouton in self.boutons:
            bouton.setEnabled(True)
        self.prenom_entree.setEnabled(True)
        self.nom_entree.setEnabled(True)
        self.label_prenom.setEnabled(True)
        self.label_nom.setEnabled(True)
        
    def desactiver_boutons_champs(self) -> None:
        """Désactiver les boutons."""
        for bouton in self.boutons:
            bouton.setEnabled(False)
        self.prenom_entree.setEnabled(False)
        self.nom_entree.setEnabled(False)
        self.label_prenom.setEnabled(False)
        self.label_nom.setEnabled(False)

    def entree_sur_prenom(self) -> None:
        """Entrée dans prénom : focus sur nom si actif, sinon validation."""
        if self.verification_nom.isChecked() and self.nom_entree.isEnabled():
            self.nom_entree.setFocus()
        else:
            self.demande_valider.emit()

    def gestion_focus(self) -> None:
        """Gérer le focus des champs et la touche Entrée."""
        if self.verification_prenom.isChecked():
            self.prenom_entree.setFocus()
        elif self.verification_nom.isChecked():
            self.nom_entree.setFocus()
        
    def etat_widgets_nom(self) -> None:
        """Activer/désactiver les widgets nom."""
        etat: bool = self.verification_nom.isChecked()
        if not etat and self.nom_entree.hasFocus():
            self.nom_entree.clearFocus()
        self.label_nom.setEnabled(etat)
        self.nom_entree.setEnabled(etat)

        if not etat:
            self.nom_entree.clear()

        self.demande_activation_nom.emit(etat)

    def etat_widgets_prenom(self) -> None:
        """Activer/désactiver les widgets relatifs au prénom."""
        etat: bool = self.verification_prenom.isChecked()
        self.label_prenom.setEnabled(etat)
        self.prenom_entree.setEnabled(etat)
        if not etat:
            self.prenom_entree.clear()
        self.demande_activation_prenom.emit(etat)


    def partie_icones(self) -> None:
        """Créer la zone d'affichage de l'icône et du score."""
        # layout horizontal du bas
        layout_images = QHBoxLayout()
        # image de validation (check ou cross)
        self.label_image_gauche = QLabel()
        self.label_image_gauche.setFixedSize(30, 30)
        self.label_image_gauche.setAlignment(Qt.AlignCenter)
        self.label_image_gauche.hide()
        layout_images.addWidget(self.label_image_gauche)
        # espace flexible entre image et score
        layout_images.addStretch()
        # affichage du nombre de bonnes réponses
        self.nbre_rep = QLabel(_("0/0"))
        self.nbre_rep.setStyleSheet("color: #6c7a80; font-size: 30px;")
        self.nbre_rep_exactes = 0
        layout_images.addWidget(self.nbre_rep)
        # ajout au layout principal
        self.layout_droit_haut.addLayout(layout_images)
        self.layout_droit_haut.addSpacing(5)
        # ligne horizontale de séparation
        ligne = QFrame()
        ligne.setFrameShape(QFrame.HLine)
        ligne.setFrameShadow(QFrame.Plain)
        ligne.setLineWidth(1)
        ligne.setStyleSheet("color: black;")
        self.layout_droit_haut.addWidget(ligne)

    def affichage_score(self, nbre_bonnes_reponses: int, rang: int) -> None:
        self.nbre_rep.setText(f"{nbre_bonnes_reponses} / {rang}")

    def afficher_image_check(self, resultat_prenom: bool, resultat_nom: bool) -> bool:
        """affichage de l'icone de validation"""
        self.label_image_gauche.show()
        # validation des deux champs
        if self.verification_prenom.isChecked() and self.verification_nom.isChecked():
            # si le champ "nom" est vide, on fait un focus sur le nom
            if not self.nom_entree.text().strip():
                self.nom_entree.setFocus()
                return False
            resultat = resultat_prenom and resultat_nom
        # validation du prenom
        elif self.verification_prenom.isChecked():
            resultat = resultat_prenom
        # validation du nom
        elif self.verification_nom.isChecked():
            resultat = resultat_nom
        # autres cas
        else:
            return False

        if resultat:
            pixmap = QPixmap("ressources/fichiers/icones/check.png")
        else:
            pixmap = QPixmap("ressources/fichiers/icones/cross.png")

        self.label_image_gauche.setPixmap(
            pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )
        return resultat

    def cacher_image_check(self) -> None:
        """Cacher l'image de résultat."""
        self.label_image_gauche.hide()
        self.label_image_gauche.clear()

    def etat_initial(self) -> None:
        """Initialiser les widgets au démarrage."""
        # cases décochées au départ
        self.verification_prenom.setChecked(False)
        self.verification_nom.setChecked(False)
        # widgets prénom désactivés
        self.label_prenom.setEnabled(False)
        self.prenom_entree.setEnabled(False)
        # widgets nom désactivés
        self.label_nom.setEnabled(False)
        self.nom_entree.setEnabled(False)
        # image cachée au départ
        self.cacher_image_check()

    def effacer_reponses(self) -> None:
        """Effacer les réponses saisies et l'icône de résultat."""
        self.prenom_entree.clear()
        self.nom_entree.clear()
        self.label_image_gauche.clear()
        self.label_image_gauche.hide()
        self.gestion_focus()

    def recuperer_saisie(self) -> tuple[str, str]:
        """Récupérer le prénom et le nom saisis."""
        prenom_saisi = self.prenom_entree.text().strip()
        nom_saisi = self.nom_entree.text().strip()
        return prenom_saisi, nom_saisi

    def champs_actifs(self) -> tuple[bool, bool]:
        """Indiquer si les champs prénom et nom sont demandés."""
        return self.verification_prenom.isChecked(), self.verification_nom.isChecked()


# ----------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ZoneDroiteHaute(None)
    fenetre.show()
    app.exec()