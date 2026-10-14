"""
Gestion des données dans le dossier utilisateur
"""
import shutil
import sys
from pathlib import Path
from modele.choix_chemin_ressources import chemin_ressources

APP_NAME = "piveo"
USER_BASE = Path.home() / ".local" / APP_NAME

def init_donnees_utilisateurs() -> None:
    """
    Initialise les données utilisateur uniquement lors de la première utilisation.
    Ensuite, les données appartiennent entièrement à l'utilisateur.
    """
    resources_base = chemin_ressources("ressources")
    marqueur = USER_BASE / ".initialisation_terminee" # fichier témoin (données écrites ou non

    # Initialisation déjà effectuée : ne rien recopier
    if marqueur.exists():
        return

    USER_BASE.mkdir(parents=True, exist_ok=True)

    for source in resources_base.rglob("*"):
        relative_path = source.relative_to(resources_base)
        destination = USER_BASE / relative_path

        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        elif not destination.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    # Mémorise que l'initialisation a été effectuée
    marqueur.touch()