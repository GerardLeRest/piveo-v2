from pathlib import Path
import sys

"""
G Le Rest - 2026
Gestion du dossier de fonctionnement suivant l'OS
"""

def dossier_ressources() -> Path:
    """
    Renvoie le dossier racine des ressources :
    - avec PyInstaller : dossier indiqué par _MEIPASS
      (temporaire en --onefile, dossier de ressources en --onedir)
    - pour un exécutable empaqueté sans _MEIPASS :
      dossier contenant l'exécutable
    - en développement : racine du projet, en supposant
      que ce fichier se trouve dans un sous-dossier du projet
    """
    # Vérifie si le programme est empaqueté, quel que soit le système.
    # Si sys.frozen n'existe pas, getattr renvoie False.
    if getattr(sys, "frozen", False):

        # PyInstaller ajoute à sys l'attribut _MEIPASS :
        # il indique le dossier où chercher les ressources.
        if hasattr(sys, "_MEIPASS"):
            # Ignore l'avertissement de typage « attribut inconnu » :
            # _MEIPASS est ajouté par PyInstaller pendant l'exécution.
            return Path(sys._MEIPASS)  # type: ignore[attr-defined]

        # Si _MEIPASS est absent, utilise le dossier de l'exécutable.
        return Path(sys.executable).resolve().parent

    # En développement, __file__ désigne le fichier contenant cette fonction.
    # resolve() donne son chemin absolu et résout les liens symboliques.
    # Le premier parent donne son dossier ; le second donne la racine du projet.
    return Path(__file__).resolve().parent.parent

def chemin_ressources(chemin_ressources: str) -> Path:
    return dossier_ressources() / chemin_ressources
