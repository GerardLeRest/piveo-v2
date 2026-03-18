from modele.Modele_ComboBox import (
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
        print("controleur - structure_choisie =", structure_choisie)
        liste_personnes = self.gestionnaire_bdd_personnes.personnes_structure(structure_choisie)
        print("controleur - personnes trouvées =", liste_personnes)
        liste_specialites = creer_specialites(liste_personnes)
        print("controleur - specialites =", liste_specialites)
        return liste_personnes, liste_specialites