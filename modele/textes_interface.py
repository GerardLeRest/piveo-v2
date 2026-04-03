#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
G Le Rest - 2026
Libelles interface
"""

# ⚠️ IMPORTANT
import gettext
# ligne ci-dessous -> fonctionnement NORMAL
from gettext import gettext as _
# ligne ci-dessous décommmentée -> test if __name__ == "__name__":
# _ = gettext.gettext

LIBELLES_INTERFACE = {
    "parlement": "Parlement",
    "parti": "Parti",
    "depute": "Député",
    "commissions": "Commissions",
    "entreprise": "Entreprise",
    "departement": "Département",
    "salarie": "Salarié",
}

def libelle(value: str) -> str:
    return _(LIBELLES_INTERFACE.get(value, value))
