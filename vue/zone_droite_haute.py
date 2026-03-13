#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
rechercher une ou plusieurs personnes dans 
l'établissement
"""


from PySide6.QtWidgets import (QWidget, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QHBoxLayout,
                               QPushButton, QApplication, QSpacerItem, QSizePolicy, QFrame, QCheckBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal
import os, sys

# ⚠️ IMPORTANT
import gettext
# ligne ci-dessous -> fonctionnement NORMAL
from gettext import gettext as _
# ligne ci-dessous décommmentée -> test if __name__ == "__name__":
# _ = gettext.gettext

REPERTOIRE_RACINE=os.path.dirname(os.path.abspath(__file__)) # répetoire du fichier pyw

class ZoneDroiteHaute(QWidget):
    """ Créer la partie droite haute de l'interface """

    demande_suite = Signal()
        
    def __init__(self, configuration_json, fenetre = None):
        """Constructeur de la frame de droite et de ses éléments"""
        super().__init__(fenetre)  # ← Important 
        self.configuration_json = configuration_json # configuration de l'interface - json
        self.layout_droit_haut = QVBoxLayout() 
        self.partie_prenom()
        self.partie_nom()
        self.partie_boutons()
        self.partie_icones()
        self.etat_initial()


    def partie_prenom(self)->None:
        """zone du prenom"""
        # prenom
        self.layout_grille = QGridLayout()
        self.label_prenom = QLabel(_("Prénom"))
        self.layout_grille.addWidget(self.label_prenom,0,0)
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
        self.layout_grille.addWidget(self.prenom_entree,0, 1)
        # checkBox "prenom"
        self.verification_prenom = QCheckBox()
        self.layout_grille.addWidget(self.verification_prenom,0, 2)
        self.verification_prenom.stateChanged.connect(self.etat_widgets_prenom)

    def partie_nom(self)->None:
        "zone du nom"
        # nom
        self.label_nom = QLabel(_("Nom"))
        self.layout_grille.addWidget(self.label_nom,1,0)
        self.nom_entree = QLineEdit()  
        self.nom_entree.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 4px 8px;
            }
        """)
        self.nom_entree.setPlaceholderText(_("Indiquez votre nom"))
        self.layout_grille.addWidget(self.nom_entree,1, 1)
        # checkBox "prenom"
        self.verification_nom = QCheckBox()
        self.layout_grille.addWidget(self.verification_nom,1, 2)
        self.verification_nom.stateChanged.connect(self.etat_widgets_nom)
        self.layout_droit_haut.addLayout(self.layout_grille)
        self.layout_droit_haut.addSpacing(5)

    def partie_boutons(self)->None:
        """zone boutons - QHBoxLayout"""
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
        suite_bouton_style = """
            QPushButton {
                background-color: #a6d0c0;
                border: 1px solid #7fb09b;
                border-radius: 6px;
                padding: 6px 14px;
                color: black;
            }
            QPushButton:hover {
                background-color: #95c0b0;
            }
            QPushButton:pressed {
                background-color: #84b0a0;
            }
        """
        efface_bouton_style =   """
            QPushButton {
                background-color: #9aaab8;
                border: 1px solid #7a8a98;
                border-radius: 6px;
                padding: 6px 14px;
                color: black;
            }
            QPushButton:hover {
                background-color: #8b9ba9;
            }
            QPushButton:pressed {
                background-color: #7c8c99;
            }
        """
        # boutons
        layout_boutons = QHBoxLayout()
        # bouton valider
        self.bout_valider = QPushButton (_("Valider"), self)
        self.bout_valider.setStyleSheet(valider_style)
        layout_boutons.addWidget(self.bout_valider)
        # bouton effacer
        self.bout_effacer = QPushButton (_("Effacer"), self)
        self.bout_effacer.setStyleSheet(efface_bouton_style)
        layout_boutons.addWidget(self.bout_effacer)
        self.bout_effacer.clicked.connect(self.effacer_reponses)
        # bouton Suite
        self.bout_suite = QPushButton (_("Suite"), self)
        self.bout_suite.setStyleSheet(suite_bouton_style)
        self.bout_suite.clicked.connect(self.demande_suite.emit)
        layout_boutons.addWidget(self.bout_suite)
        # espacement au dessus des boutons
        espaceur = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout_droit_haut.addItem(espaceur)
        self.layout_droit_haut.addLayout(layout_boutons)
        # désativer les boutons
        # self.bout_valider.setEnabled(False)
        # self.bout_effacer.setEnabled(False)
        # self.bout_suite.setEnabled(False)

    def partie_icones(self)->None:
        """deux icones ok et nok"""
        # partie du bas - 2 images (réusssite à gauhe et score à droite)
        layout_images = QHBoxLayout()
        # image de validation check ou cross) -Image vide au départ
        self.label_image_gauche = QLabel()
        self.label_image_gauche.setFixedSize(32, 32)
        layout_images.addWidget(self.label_image_gauche)
        # espace entre l'image et le compteur de bonnes réponses
        layout_images.addStretch()  # ← ajoute un espace flexible
        # affichage des bonnes réponses
        self.nbre_rep = QLabel(_("0/0")) 
        self.nbre_rep.setStyleSheet("color: grey;font-size: 30px;")
        self.nbre_rep_exactes=0 
        layout_images.addWidget(self.nbre_rep)
        self.layout_droit_haut.addLayout(layout_images)
        self.layout_droit_haut.addSpacing(10)
        # Ligne horizontale continue
        ligne = QFrame()
        ligne.setFrameShape(QFrame.HLine)
        ligne.setFrameShadow(QFrame.Plain)
        ligne.setLineWidth(1)
        ligne.setStyleSheet("color: black;")
        self.layout_droit_haut.addWidget(ligne)
        self.setLayout(self.layout_droit_haut)
        self.show()

    def etat_initial(self)->None:
        """initialiser les widgets au démarrage"""
        self.label_prenom.setEnabled(False)
        self.prenom_entree.setEnabled(False)
        self.label_nom.setEnabled(False)
        self.nom_entree.setEnabled(False)

    def etat_widgets_prenom(self)->None:
        """activer/désactiver widgets relatif au prénom"""
        if self.verification_prenom.isChecked():
            self.label_prenom.setEnabled(True)
            self.prenom_entree.setEnabled(True)
        else:
            self.label_prenom.setEnabled(False)
            self.prenom_entree.setEnabled(False)

    def etat_widgets_nom(self)->None:
        """activer/désactiver les widgets relatif à nom"""
        if self.verification_nom.isChecked():
            self.label_nom.setEnabled(True)
            self.nom_entree.setEnabled(True)
        else:
            self.label_nom.setEnabled(False)
            self.nom_entree.setEnabled(False)

    def effacer_reponses(self) -> None:
        """effacer réponses"""
        # effacer champs des noms et prénom
        self.prenom_entree.setEnabled(True)
        self.prenom_entree.clear()
        self.nom_entree.setEnabled(True)
        self.nom_entree.clear()
        # effacer icone
        self.label_image_gauche.clear() 
        # désactiver - Nbres bonne réponse  
        self.nbre_rep.setEnabled(False) 
    
    # -------------------------------------------    
                
    def config_rechercher(self) -> None:
        """configurer - mode Rechercher"""
        # changer couleur label
        self.label_prenom.setStyleSheet("color: black;")
        self.label_nom.setStyleSheet("color: black;")
        # Désactiver l'affichage des bonnes réponses
        self.Des_Affich_Rep()
        # activer/désactiver boutons 
        self.bout_valider.setEnabled(True)
        self.bout_effacer.setEnabled(True)
        self.bout_suite.setEnabled(False)
    
    def Des_Affich_Rep(self) -> None:
        """ désactiver l'affichage des bonnes réponses"""
        self.nbre_rep.setStyleSheet("color: grey;font-size: 30px") #nbre bonnes reponses en gris
        self.nbre_rep_exactes=0  # nbre de réponses exactes
        # maj nbrebonnes réponses
        self.nbre_rep.setText(f"{self.nbre_rep_exactes}/0")   
    
    def des_cadre_Dr_Ha(self) -> None:
        """désactiver des boutons et les entry de la frameDB"""     
        self.prenom_entree.setEnabled(False)
        self.nom_entree.setEnabled(False)
        self.bout_valider.setEnabled(False)
        self.bout_effacer.setEnabled(False)
        self.bout_suite.setEnabled(False)
        self.nbre_rep.setStyleSheet("color: grey;font-size: 30px")
        
        
    def config_test_ecrit(self) -> None:
        """ configurer - Test écrit """
        # changer couleur label
        self.label_prenom.setStyleSheet("color: black;")
        self.label_nom.setStyleSheet("color: black;")
        self.nom_entree.setStyleSheet("color: black") 
        self.nbre_rep.setStyleSheet("color: back; font-size:30px;") 
        # effacer réponses
        self.effacer_reponses()        
        # activer boutons 
        self.bout_valider.setEnabled(True)
        self.bout_effacer.setEnabled(True)
        self.bout_suite.setEnabled(True)   
        
# ----------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ZoneDroiteHaute(None)
    fenetre.show()
    app.exec()