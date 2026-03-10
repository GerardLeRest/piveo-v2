#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
afficher la photo de l'élève sélecctionné
et ses informations
"""

class DefilementPhotos:
    """Défiler les photos"""

    def __init__(self, liste_personnes: list[list]) -> None:
        self.liste_personnes = liste_personnes
        self.rang = 0

    def acceder_premier(self) -> None:
        """Accéder au premier élève de la liste"""
        if self.liste_personnes:
            self.rang = 0

    def acceder_precedent(self) -> None:
        """Accéder à l'élève précédent"""
        if self.rang > 0:
            self.rang -= 1

    def acceder_suivant(self) -> None:
        """Accéder à l'élève suivant"""
        if self.rang < len(self.liste_personnes) - 1:
            self.rang += 1

    def acceder_dernier(self) -> None:
        """Accéder au dernier élève"""
        if self.liste_personnes:
            self.rang = len(self.liste_personnes) - 1