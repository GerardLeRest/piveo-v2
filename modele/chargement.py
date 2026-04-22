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
    """Retourne le dossier ressources (compatible PyInstaller)."""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / "ressources"
    return Path(__file__).resolve().parent.parent / "ressources"

def init_donnees_utilisateurs() -> None:
    """
    Initialise les données utilisateur sans écraser les fichiers déjà modifiés.
    """
    resources_base = get_resources_base()
    USER_BASE.mkdir(parents=True, exist_ok=True)
    for source in resources_base.rglob("*"):
        relative_path = source.relative_to(resources_base)
        destination = USER_BASE / relative_path
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
        else:
            if not destination.exists():
                shutil.copy2(source, destination)