#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
fichier d'entrée
"""

import sys
import locale
import gettext
from pathlib import Path
from PySide6.QtWidgets import QApplication
from modele.chargement import init_donnees_utilisateurs
from modele.gestion_langue import GestionLangue
from modele.choix_chemin_ressources import chemin_ressources

# répertoires
LOCALE_DIR = chemin_ressources("locales")

# copie de ressources vers ~/.local/piveo
# (uniquement si le dossier n'existe pas)
init_donnees_utilisateurs()

# fichier configuration pour les 4 fichiers json
rep_config = Path.home() / ".local" / "piveo" / "configurations_json"
rep_config.mkdir(parents=True, exist_ok=True)

# fichier de configuration de la langue
fichier_langue = rep_config / "configurationLangue.json"

# lecture de la langue choisie
gestion_langue = GestionLangue(fichier_langue)
langue = gestion_langue.lire()

# configuration locale système
locale.setlocale(locale.LC_ALL, "")

# initialisation de gettext AVANT toute interface
traduction = gettext.translation(
    domain="messages",
    localedir=str(LOCALE_DIR),
    languages=[langue],
    fallback=True
)
traduction.install()

# lancement de la fenêtre "Organisme"
from vue.choix_organisme import ChoixOrganisme

def main():
    app = QApplication(sys.argv)
    # theme sous windows
    app.setStyle("Fusion")
    fenetre = ChoixOrganisme()
    fenetre.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
