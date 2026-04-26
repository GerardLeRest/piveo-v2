#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fenêtre d'accueil – choix de l'organisme :
École, Entreprise, Parlement
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QScrollArea, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from pathlib import Path
import json, sqlite3
from vue.fenetre_principale import FenetrePrincipale
from modele.choix_chemin_ressources import chemin_ressources
from modele.construction_BDD import ConstructionBDD
from builtins import _
from controleur.controleur_zone_gauche import ControleurZoneGauche

class ChoixOrganisme(QWidget):
    """Fenêtre de choix de l'organisme"""

    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self) -> None:
        """Création de l'interface graphique"""
        # Fenêtre
        self.resize(320,600)
        self.setWindowTitle(_("Piveo"))
        self.setStyleSheet("background-color: white;")
        # Layout principal
        layout=QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(8)
        # Titre
        label=QLabel(_("Mode de fonctionnement"))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color:#2F4F4F;font-weight:bold;font-size:20px;")
        layout.addWidget(label)
        # Boutons radio
        self.radio_collectivite=QRadioButton(_("Collectivité"))
        self.radio_ecole=QRadioButton(_("École"))
        self.radio_entreprise=QRadioButton(_("Entreprise"))
        self.radio_ecole.setChecked(True)
        for radio in (self.radio_collectivite, self.radio_ecole,self.radio_entreprise):
            radio.setStyleSheet("font-size:18px;margin:2px 0;color:black;")
            layout.addWidget(radio)
        # Zone RGPD (scrollable simple)
        scroll_rgpd=QScrollArea()
        scroll_rgpd.setWidgetResizable(True)
        scroll_rgpd.setFixedHeight(220)
        scroll_rgpd.setStyleSheet("""
            QScrollArea {
                background-color: #f9f9f9;
                border: 1px solid #999;
                margin-top: 15px;
            }
        """)
        label_rgpd=QLabel("<b>Protection des données</b><br><br>"
                        "Ce logiciel traite des données personnelles (prénoms, noms, photos) dans le cadre de la gestion interne des personnes.<br><br>"
                        "Les données sont stockées localement sur un nombre limité d’ordinateurs fixes sécurisés, qui doivent rester sur place dans une zone définie. "
                        "L’accès à ces ordinateurs est strictement réservé aux personnes autorisées. Aucune copie des données n’est autorisée en dehors de cet environnement.<br><br>"
                        "La consultation, la modification et l’ajout de données sont réservés aux personnes désignées et habilitées par le responsable du traitement.<br><br>"
                        "Conformément au RGPD, chaque personne dispose d’un droit d’accès, de rectification et de suppression de ses données.<br><br>"
                        "Les données sont conservées uniquement pendant la durée nécessaire à leur utilisation.<br><br>"
                        "Le responsable du traitement est l’organisme au sein duquel ce logiciel est utilisé.")
        label_rgpd.setWordWrap(True)
        label_rgpd.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        label_rgpd.setMargin(8)
        label_rgpd.setStyleSheet("QLabel{background-color:#f9f9f9;color:black;font-size:12px;}")
        scroll_rgpd.setWidget(label_rgpd)
        layout.addWidget(scroll_rgpd)
        # Bouton OK
        bouton=QPushButton(_("OK"))
        bouton.setFixedWidth(80)
        bouton.setStyleSheet("QPushButton{background-color:#76aeba;color:white;border-radius:12px;padding:5px 10px;font-weight:bold;}QPushButton:hover{background-color:#66a0b0;}")
        bouton.clicked.connect(self.lancer_piveo)
        layout.addWidget(bouton,alignment=Qt.AlignCenter)
        # Logo
        label_logo=QLabel()
        chemin_logo=chemin_ressources("ressources/fichiers/logos/logoPiveo.png")
        pixmap=QPixmap(str(chemin_logo))
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaledToWidth(90,Qt.SmoothTransformation))
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo)
        # Application du layout
        self.setLayout(layout)

    def lancer_piveo(self) -> None:
        """Lancé après le clic utilisateur"""
        # chemin des ~/.loval/piveo
        APP_NAME = "piveo"
        USER_BASE = Path.home() / ".local" / APP_NAME
        # récupération du fichier json de configuration
        if self.radio_ecole.isChecked():
            fichier_config = "ConfigEcole.json"
            chemin_CSV = USER_BASE / "fichiers" / "eleves"
        elif self.radio_entreprise.isChecked():
            fichier_config = "ConfigCollectivite.json"
            chemin_CSV = USER_BASE / "fichiers" / "salaries"
        else:
            fichier_config = "ConfigCollectivite.json"
            chemin_CSV = USER_BASE / "fichiers" / "agents"
        # charger la configuration choisie
        try:
            chemin_config = USER_BASE / "configurations_json" / fichier_config
            with open(chemin_config, "r", encoding="utf-8") as f:
                configuration_json = json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de la configuration : {e}")
            return
        # Chemin COMPLET vers la base de données
        chemin_bdd = USER_BASE / "BaseDonnees" / configuration_json["BaseDonnees"]
        construction_BDD = ConstructionBDD(chemin_bdd, chemin_CSV)
        # on utilise la connexion de contruction_BDD
        conn = construction_BDD.connexion  
        # Lancement de la fenêtre principale
        self.fenetre_principale = FenetrePrincipale(configuration_json, conn, None)
        self.fenetre_principale.show()
        self.close()