#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
Traitement des noms et des prenoms
"""
PRENOM = "Gérard"
NOM = "Le Rest"


class PrenomNom:

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        self.comparer_prenom(prenom)
        self.comparer_nom(nom)

    def comparer_prenom(self, prenom)->bool:
        "tester la validité du prénom"
        print(f"prénom étudié: {prenom}")
        if PRENOM == prenom:
            return True
        else:
            return False
        
    def comparer_nom(self, nom)->bool:
        "tester la validité du nom"
        print(f"nom étudié: {nom}")
        if NOM == nom:
            return True
        else:
            return False