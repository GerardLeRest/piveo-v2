#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
Gestion des listes pour les combobox
"""

from builtins import _


def creer_specialites(liste_personnes: list) -> list:
    """Créer la liste des spécialités présentes uniquement dans la structure sélectionnée"""
    liste_specialites = []

    for personne in liste_personnes:
        options = personne[3]
        for option in options:
            if option not in liste_specialites:
                liste_specialites.append(option)

    liste_specialites.sort()
    liste_specialites.insert(0, _("TOUS"))

    return liste_specialites


def lister_structures(gestionnaire_bdd_personnes) -> list:
    """Lister les structures"""
    return gestionnaire_bdd_personnes.lister_structures()


def construire_liste_structures(structures: list, configuration_json: dict) -> list:
    """construction de la liste des structures"""
    structure = configuration_json["Structure"]
    if configuration_json["Organisme"] == "Ecole":
        phrase = _("- choisir une %(structure)s -") % {"structure": structure}
    else:
        phrase = _("- choisir un %(structure)s -") % {"structure": structure}

    return [phrase] + structures