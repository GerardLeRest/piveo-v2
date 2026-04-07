"""
G Le Rest - 2026
Gestion des données dans le dossier utilisateur
"""
import shutil
import sys
from pathlib import Path

APP_NAME = "piveo"
USER_BASE = Path.home() / ".local" / APP_NAME

def get_resources_base() -> Path:
    """Retourne le dossier ressources (compatible PyInstaller)"""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "ressources"
    return Path(__file__).resolve().parent.parent / "ressources"

def init_donnees_utiliisateurs() -> None:
    """
    Initialise les données utilisateur.
    """
    resources_base = get_resources_base()

    if USER_BASE.exists():
        shutil.rmtree(USER_BASE)

    shutil.copytree(resources_base, USER_BASE)
   