#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
G Le Rest - 2026
contrôleur de la zone droite basse
"""

from modele.modele_combobox import (
    creer_specialites,
    lister_structures,
    construire_liste_structures
)


class ControleurZoneDroiteBasse:
    def __init__(self, gestionnaire_bdd_personnes):
        self.gestionnaire_bdd_personnes = gestionnaire_bdd_personnes

    def recuperer_structures_ui(self, configuration_json: dict) -> list:
        structures = lister_structures(self.gestionnaire_bdd_personnes)
        return construire_liste_structures(structures, configuration_json)

    def choisir_structure_specialites(self, structure_choisie: str) -> tuple[list, list]:
        liste_personnes = self.gestionnaire_bdd_personnes.personnes_structure(structure_choisie)
        liste_specialites = creer_specialites(liste_personnes)
        return liste_personnes, liste_specialites