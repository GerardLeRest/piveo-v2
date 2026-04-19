#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
gestion du rang de la liste des personnes
et ses informations
"""

class ModeleZoneGauche:
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
        int(self.rang)

    def ajouter_interrogations(self, liste_personnes):
        """ajouter des blancs ou des ??? dans la liste"""
        i = 0
        while i < len(liste_personnes):
            tab = liste_personnes[i].copy()
            tab[0] = "???"
            tab[1] = "???"
            liste_personnes.insert(i, tab)
            i = i + 2
        return liste_personnes
        
    def activer_prenom(self, etat: bool) -> None:
        """sélection/déselection bouton et champs"""
        self.label_prenom.setEnabled(etat)
        self.prenom_entree.setEnabled(etat)
        if not etat:
            self.prenom_entree.clear()

   