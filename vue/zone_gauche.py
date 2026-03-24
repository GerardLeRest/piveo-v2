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

from modele.textes_interface import libelle


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
        
    def __init__(self, liste_personnes, configuration_json, fenetre_principale, parent=None):
        """Constructeur de la frame de gauche et de ses éléments"""
        super().__init__(parent)
        self.fenetre_principale = fenetre_principale # pour référencé la fenetre pour les widgets 
        self.configuration_json = configuration_json
        self.layout_gauche = QVBoxLayout()
        self.liste_personnes = liste_personnes
        self.rang = 0
        self.nbre_pers = len(self.liste_personnes)
        self.repertoire_racine = ""
        
        self.resize(150, 100)
        self.partie_haute()
        self.partie_milieu()
        self.partie_basse()


    def partie_haute(self)->None:
        """partie haute de l'interface"""
        # Partie haute du layout
        # QGridLayout
        # prenom
        self.layout_grille = QGridLayout()
        self.prenom = QLabel("-")
        self.prenom.setText(_("Prénom"))
        self.prenom.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        self.layout_grille.addWidget(self.prenom, 0, 1)
        self.layout_grille.addWidget(QLabel(_("Prénom attendu:")), 0, 0, alignment=Qt.AlignLeft)
        # nom
        self.nom = QLabel()
        self.nom.setText(_("Nom"))
        self.nom.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        self.layout_grille.addWidget(self.nom, 1, 1)
        self.layout_grille.addWidget(QLabel(_("Nom attendu :")), 1, 0, alignment=Qt.AlignLeft)
        # attachement à layoutGauche
        self.layout_gauche.addLayout(self.layout_grille)

    def partie_milieu(self)->None:
        """partie milieu de l'interface"""
        # Layout principal vertical
        layout_milieu = QVBoxLayout()
        # Création du QLabel de l'image
        self.label_image = QLabel()
        self.label_image.setFixedSize(128, 128)
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
        # Bouton début
        self.bouton_debut = QPushButton()
        self.bouton_debut.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / icones[0])))
        self.bouton_debut.setIconSize(QSize(24, 24))
        self.bouton_debut.clicked.connect(self.demande_debut.emit)
        layout_boutons.addWidget(self.bouton_debut)
        # Bouton reculer
        self.bouton_reculer = QPushButton()
        self.bouton_reculer.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / icones[1])))
        self.bouton_reculer.setIconSize(QSize(24, 24))
        self.bouton_reculer.clicked.connect(self.demande_reculer.emit)
        layout_boutons.addWidget(self.bouton_reculer)
        # Bouton avancer
        self.bouton_avancer = QPushButton()
        self.bouton_avancer.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / icones[2])))
        self.bouton_avancer.setIconSize(QSize(24, 24))
        self.bouton_avancer.clicked.connect(self.demande_avancer.emit)
        layout_boutons.addWidget(self.bouton_avancer)
        # Bouton fin
        self.bouton_fin = QPushButton()
        self.bouton_fin.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / icones[3])))
        self.bouton_fin.setIconSize(QSize(24, 24))
        self.bouton_fin.clicked.connect(self.demande_fin.emit)
        layout_boutons.addWidget(self.bouton_fin)
        # espaces entre les boutons
        layout_boutons.setSpacing(6)
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
        self.desactiver_boutons()
        
    def desactiver_boutons(self)->None:
        """désactiver les quatre boutons au démarrage"""
        self.bouton_debut.setEnabled(False)
        self.bouton_avancer.setEnabled(False)
        self.bouton_reculer.setEnabled(False)
        self.bouton_fin.setEnabled(False)

    def activer_boutons(self)->None:
        """désactiver les quatre boutons au démarrage"""
        self.bouton_debut.setEnabled(True)
        self.bouton_avancer.setEnabled(True)
        self.bouton_reculer.setEnabled(True)
        self.bouton_fin.setEnabled(True)
        

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
        self.structure.setText(_(libelle(self.configuration_json["Structure"])))
        self.structure.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 11pt;")
        layout_bas.addWidget(self.structure, alignment=Qt.AlignCenter)
        # affichage des options
        self.specialites = QLabel() # permet de changer le texte du label
        self.specialites.setText(_(libelle(self.configuration_json["Specialite"])))
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
        self.structure.setText(libelle(structure_interne))

        # Options (liste)
        options = self.liste_personnes[self.rang][3]
        options_ui = [libelle(opt) for opt in options] # affichage ui
        texteOptions = " - ".join(options_ui)
        self.specialites.setText(texteOptions)


    def maj_num_ordre_Pers(self) -> None:
        """Mettre à jour le numéro d'ordre de la personne."""
        # suivant la position du bouton
        if not self.fenetre_principale.act_reponse_cachee.isChecked():  # mode normal (voir init)
            position = self.rang + 1
            total = self.nbre_pers
        else:  # mode deviner
            print("cachee")
            position = self.rang // 2 + 1
            total = self.nbre_pers // 2
            print(f"position: {position} - total: {total}")
        # mise à jour de position/total
        self.num_Ordre_Pers.setText(f"{position}/{total}") 


    def desactivation_icones(self):
        pass

                
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