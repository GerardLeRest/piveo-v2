import random


class ModeleToolbar:

    def melanger(self, liste_de_personnes: list) -> list:
        """Retourner une liste mélangée."""
        liste_aleatoire = liste_de_personnes.copy()
        random.shuffle(liste_aleatoire)
        return liste_aleatoire
    
    def ajouter_points_interrogations(self, liste_personnes, masquer_prenom, masquer_nom):
        """ajouter des blancs ou des ??? dans la liste"""
        i = 0
        while i < len(liste_personnes):
            tab = liste_personnes[i].copy()
            if masquer_prenom and masquer_nom:
                tab[0] = "???"
                tab[1] = "???"
            elif masquer_nom:
                tab[0] = "???"
                tab[1] = ""
            else:
                tab[0] = ""
                tab[1] = "???"
            liste_personnes.insert(i, tab)
            i = i + 2
        print("liste: ", liste_personnes)
        return liste_personnes