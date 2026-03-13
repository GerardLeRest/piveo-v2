#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
fenêtre contenant les trois zones
ainsi que les icônes et les menus
"""

from vue.zone_gauche import ZoneGauche
from vue.zone_droite_haute import ZoneDroiteHaute
#from vue.zone_droite_basse import ZoneDroiteBasse
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QHBoxLayout,
                               QApplication)
import sys


class FenetrePrincipale(QWidget):
    """Fenêtre principale de l'application."""

    def __init__(self, liste_personnes, configuration_json, connecteur_bdd, parent=None):
        super().__init__(parent)

        self.zone_gauche = ZoneGauche(None, configuration_json, connecteur_bdd)
        self.zone_droite_haute = ZoneDroiteHaute(configuration_json)
        #self.zone_droite_basse = ZoneDroiteBasse()
        # contruction de l'interface
        self.construire_interface()

    def construire_interface(self):
        """Construire l'interface principale."""
        layout_horizontal = QHBoxLayout()
        #layout vertical
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.zone_droite_haute) 
        self.zone_droite_basse = QLabel("Zone droite basses") # ACHANGER PLUS TARD"
        layout_vertical.addWidget(self.zone_droite_basse)  
        # layout horizontale   
        layout_horizontal.addWidget(self.zone_gauche)
        layout_horizontal.addLayout(layout_vertical)
        self.setLayout(layout_horizontal)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    liste_personnes = [
        ['Sarah', 'Fernandez', '1S1', ['CAM', 'THE'], 'Fernandez_Sarah.jpg'],
        ['Clement', 'Henry', '1S1', ['CAM'], 'Henry_Clement.jpg'],
        ['Emma', 'Petit', 'PSTI2D1', ['ESP'], 'Petit_Emma.jpg']
    ]
    recuperer_bdd = None
    config = {
        "Organisme": "Entreprise",
        "Structure": "Département",
        "Personne": "Ecole",
        "Specialite": "Option",
        "BaseDonnees": "eleves.db",
        "CheminPhotos": "eleves"
    }

if __name__ == "__main__":
    app = QApplication(sys.argv)
    FenetrePrincipale = FenetrePrincipale()    
    sys.exit(app.exec())
