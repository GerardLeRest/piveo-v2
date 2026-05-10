#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
afficher la photo de l'élève sélectionné
et ses informations
"""

import sys
from pathlib import Path
# ⚠️ IMPORTANT
# fonctionnement global
from builtins import _
# tester la classe
# python3 -m vue.zone_droite_haute (test de la classe)
#_ = lambda x: x 
# Ajoute la racine du projet au chemin Python
dossier_racine = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(dossier_racine))

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QApplication,
    QLabel, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtGui import QPixmap, QIcon


icones = [
    "Gnome-go-first.png",
    "Gnome-go-previous.png",
    "Gnome-go-next.png",
    "Gnome-go-last.png"
]

class ZoneGauche (QWidget):
    """ Créer la partie gauche de l'interface """

    # signaux
    demande_avancer = Signal()
    demande_reculer = Signal()
    demande_debut = Signal()
    demande_fin = Signal()
        
    def __init__(self, liste_personnes, configuration_json, parent=None):
        """Constructeur de la frame de gauche et de ses éléments"""
        super().__init__(parent)
        self.configuration_json = configuration_json
        self.layout_gauche = QVBoxLayout()
        self.layout_gauche.addSpacing(2)
        self.liste_personnes = liste_personnes
        self.rang = 0
        self.nbre_pers = len(self.liste_personnes)
        self.repertoire_racine = ""
        self.resize(150, 100)
        self.partie_haute()
        self.partie_milieu()
        self.desactiver_boutons()
        self.partie_basse()

    def partie_haute(self) -> None:
        """Partie haute de l'interface."""
        self.layout_grille = QGridLayout()
        # prénom
        self.label_prenom = QLabel(_("Prénom attendu:"))
        self.layout_grille.addWidget(self.label_prenom, 0, 0, alignment=Qt.AlignLeft)
        # Qlabel prenom
        self.prenom = QLabel("-")
        self.prenom.setText(_("Prénom"))
        self.prenom.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        self.layout_grille.addWidget(self.prenom, 0, 1)
        # Qlabel nom
        self.label_nom = QLabel(_("Nom attendu:"))
        self.layout_grille.addWidget(self.label_nom, 1, 0, alignment=Qt.AlignLeft)
        self.nom = QLabel("-")
        self.nom.setText(_("Nom"))
        self.nom.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        self.layout_grille.addWidget(self.nom, 1, 1)
        # ajout de layout_grille dans layout_gauche
        self.layout_gauche.addLayout(self.layout_grille)

    def partie_milieu(self)->None:
        """partie milieu de l'interface"""
        # Layout principal vertical
        layout_milieu = QVBoxLayout()
        # Création du QLabel de l'image
        self.label_image = QLabel()
        self.label_image.setFixedSize(128, 128)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image.setStyleSheet("border: 1px solid #666; background-color: #f0f0f0;")
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Chargement de l'image par défaut
        chemin_defaut = dossier_racine / "ressources" / "fichiers" / "images" / "inconnu.jpg"
        pixmapDefaut = QPixmap(chemin_defaut).scaled(
            128, 128,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.label_image.setPixmap(pixmapDefaut)
        # Puis ajout dans layout vertical principal
        layout_boutons = QHBoxLayout()
        # boutons de défilement
        # bouton début
        bouton_debut = QPushButton()
        bouton_debut.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "Gnome-go-first.png")))
        bouton_debut.setIconSize(QSize(24, 24))
        bouton_debut.clicked.connect(self.demande_debut.emit)
        layout_boutons.addWidget(bouton_debut)
        # bouton précédent
        bouton_reculer = QPushButton()
        bouton_reculer.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "Gnome-go-previous.png")))
        bouton_reculer.setIconSize(QSize(24, 24))
        bouton_reculer.clicked.connect(self.demande_reculer.emit)
        layout_boutons.addWidget(bouton_reculer)
        # bouton suivant
        bouton_avancer = QPushButton()
        bouton_avancer.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "Gnome-go-next.png")))
        bouton_avancer.setIconSize(QSize(24, 24))
        bouton_avancer.clicked.connect(self.demande_avancer.emit)
        layout_boutons.addWidget(bouton_avancer)
        # bouton fin
        bouton_fin = QPushButton()
        bouton_fin.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "Gnome-go-last.png")))
        bouton_fin.setIconSize(QSize(24, 24))
        bouton_fin.clicked.connect(self.demande_fin.emit)
        layout_boutons.addWidget(bouton_fin)
        # permet de traiter les quatre à la fois (activer/desactiver)
        self.boutons = [bouton_debut, bouton_reculer, bouton_avancer, bouton_fin]
        layout_boutons.setSpacing(6)  # espace horizontal entre flèches
        # Bloc vertical (photo + boutons), avec marges
        bloc_photo = QVBoxLayout()
        bloc_photo.setContentsMargins(10, 10, 10, 10)  # marges autour du bloc
        bloc_photo.setSpacing(10)  # espace entre photo et boutons
        bloc_photo.addWidget(self.label_image, alignment=Qt.AlignCenter)
        bloc_photo.addLayout(layout_boutons)
        # Encapsule le tout dans un widget
        photo_milieu = QWidget()
        photo_milieu.setLayout(bloc_photo)
        # Ajoute à layoutMilieu
        layout_milieu.addWidget(photo_milieu)
        # Ajoute à layoutGauche (comme avant)
        self.layout_gauche.addLayout(layout_milieu)

    def partie_basse(self)->None:
        """partie bassse de l'interface"""
		# layout bas
        # affichage des élèves restants
        layout_bas = QVBoxLayout()
        self.num_Ordre_Pers=QLabel() # rang de la Personne
        self.num_Ordre_Pers.setText(_("rang / effectif "))
        layout_bas.addWidget(self.num_Ordre_Pers, alignment=Qt.AlignCenter)
        # affichage de la structure 
        self.structure=QLabel() # label de la structure
        self.structure.setText(_(self.configuration_json["Structure"]))
        self.structure.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 11pt;")
        layout_bas.addWidget(self.structure, alignment=Qt.AlignCenter)
        # affichage des options
        self.specialites = QLabel() # permet de changer le texte du label
        self.specialites.setText(_(self.configuration_json["Specialite"]))
        self.specialites.setStyleSheet("font-size: 10pt;")
        layout_bas.addWidget(self.specialites, alignment=Qt.AlignCenter)
        # attachement au layout gauche
        self.layout_gauche.addLayout(layout_bas)
        # Espace vertical fixe de 10 pixels
        spacer = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout_gauche.addItem(spacer)
        # attachement à la fenêtre principale
        self.setLayout(self.layout_gauche)
        #self.maj()
        self.show()

    def activer_boutons(self) -> None:
        """activer les boutons"""
        for bouton in self.boutons:
            bouton.setEnabled(True)

    def desactiver_boutons(self) -> None:
        """désaciver les bouton"""
        for bouton in self.boutons:
            bouton.setEnabled(False)

    def effacer_affichage(self) -> None:
        """Effacer les informations affichées"""
        self.prenom.setText("-")
        self.nom.setText("-")
        self.structure.setText("-")
        self.specialites.setText("-")
        self.num_Ordre_Pers.setText("-")
        image_par_defaut = dossier_racine / "ressources" / "fichiers" / "images" / "inconnu.jpg"
        self.label_image.setPixmap(QPixmap(image_par_defaut))   

    def maj(self) -> None:
        """Mettre à jour l'affichage de l'élève courant si la liste est valide"""
        if not self.liste_personnes or self.rang >= len(self.liste_personnes):
            return  # on ne fait rien si la liste est vide ou le rang est hors limites
        #self.rang = 0
        self.maj_nom_prenom()
        self.maj_classe_options()
        self.maj_Photo()
        self.maj_num_ordre_Pers()
            
    def maj_Photo(self) -> None:
        """Mise à jour de la photo"""
        nom_image = self.liste_personnes[self.rang][4]
        chemin_image = (
            dossier_racine
            / "ressources"
            / "fichiers"
            / "photos"
            / self.configuration_json["CheminPhotos"]
            / nom_image
        )
        # si l'image existe
        if chemin_image.exists():
            pixmap = QPixmap(str(chemin_image))
        else:
            chemin_defaut = dossier_racine / "ressources" / "fichiers" / "images" / "inconnu.jpg"
            pixmap = QPixmap(str(chemin_defaut))
        # redimesionnemment de l'image
        pixmap = pixmap.scaled(
            128, 128,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
            )
        self.label_image.setPixmap(pixmap)

    def maj_nom_prenom(self):
        """mise à jour du nom et du prenom"""
        self.prenom.setText(self.liste_personnes[self.rang][0])
        self.nom.setText(self.liste_personnes[self.rang][1])
    
    def maj_classe_options(self):
        """mise a jour de la structure et de la spécialité"""
        # Structure (classe / département / parti)
        structure_interne = self.liste_personnes[self.rang][2]
        self.structure.setText(_(structure_interne))
        # Options (liste)
        options = self.liste_personnes[self.rang][3]
        options_ui = [_(opt) for opt in options]
        texteOptions = " - ".join(options_ui)
        self.specialites.setText(texteOptions)

    def maj_num_ordre_Pers(self) -> None:
        """mettre à jour le numéro d'ordre de la personne"""
        if self.nbre_pers==len(self.liste_personnes): # apprentissage
            self.num_Ordre_Pers.setText(str(self.rang+1)+"/"+str(self.nbre_pers))
        else: # test mental
            self.num_Ordre_Pers.setText(str(self.rang//2+1)+"/"+str(self.nbre_pers))  

    def activer_prenom(self, etat: bool) -> None:
        self.label_prenom.setVisible(etat)
        self.prenom.setVisible(etat)

    def activer_nom(self, etat: bool) -> None:
        self.label_nom.setVisible(etat)
        self.nom.setVisible(etat)
                
# ----------------------------------------------------
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    liste_personnes = []

    config = {
        "Organisme": "Entreprise",
        "Structure": "Département",
        "Personne": "Ecole",
        "Specialite": "Option",
        "BaseDonnees": "eleves.db",
        "CheminPhotos": "eleves"
    }

    fenetre = ZoneGauche(liste_personnes, config)
    fenetre.show()

    sys.exit(app.exec())