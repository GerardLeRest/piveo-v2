#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
Traitement des noms et des prénoms
"""

class ModeleZoneDroiteHaute:

    def __init__(self, prenom_attendu: str, nom_attendu: str) -> None:
        self.prenom_attendu = prenom_attendu.lower()
        self.nom_attendu = nom_attendu.lower()

    def comparer_prenom(self, prenom_saisi: str) -> bool:
        return prenom_saisi.lower() == self.prenom_attendu

    def comparer_nom(self, nom_saisi: str) -> bool:
        return nom_saisi.lower() == self.nom_attendu