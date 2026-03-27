#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
Traitement des noms et des prénoms
"""

class ModeleZoneDroiteHaute:

    def __init__(self, prenom_attendu: str, nom_attendu: str) -> None:
        self.prenom_attendu = prenom_attendu
        self.nom_attendu = nom_attendu

    def comparer_prenom(self, prenom_saisi: str) -> bool:
        """Tester la validité du prénom."""
        print(f"prénom étudié: {prenom_saisi}")
        return prenom_saisi == self.prenom_attendu

    def comparer_nom(self, nom_saisi: str) -> bool:
        """Tester la validité du nom."""
        print(f"nom étudié: {nom_saisi}")
        return nom_saisi == self.nom_attendu