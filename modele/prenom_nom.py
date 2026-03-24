#!/usr/bin/python3
# -*- coding: utf-8 -
"""
G Le Rest - 2026
Traitement des noms et des prenoms
"""

class PrenomNom:

    def __init__(self, liste_personnes, vue):
        self.vue = vue
        self.vue.zone_droite_haute.activer_boutons() # activer les trois bouton
        self.prenom = liste_personnes[0]
        self.nom = liste_personnes[1]
        self.acquisitions_champs()
        self.comparer_prenom(self.prenom)
        self.comparer_nom(self.nom)

    def acquisitions_champs(self)->None:
        """acquisition des deux champs"""
        self.prenom_saisie = self.vue.prenom_nom.prenom_entree.text() 
        self.nom_saisie = self.vue.prenom_nom.prenom_entree.text() 

    def comparer_prenom(self)->bool:
        "tester la validité du prénom"
        if self.prenom_saisie == self.prenom:
            return True
        else:
            return False
        
    def comparer_nom(self)->bool:
        "tester la validité du nom"
        if self.nom_saisie == self.nom:
            return True
        else:
            return False