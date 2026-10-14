"""
Gestion des chemins des ressources sous Linux et Windows.
"""

from pathlib import Path
import sys


def dossier_ressources() -> Path:
    """Retourne la racine du projet ou du programme empaqueté."""

    # Programme empaqueté
    if getattr(sys, "frozen", False):

        # Avec PyInstaller
        if hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS)  # type: ignore[attr-defined]

        # Autre exécutable
        return Path(sys.executable).resolve().parent

    # En développement : racine du projet
    return Path(__file__).resolve().parent.parent


def chemin_ressources(chemin: str) -> Path:
    """Retourne le chemin complet d'une ressource."""
    return dossier_ressources() / chemin