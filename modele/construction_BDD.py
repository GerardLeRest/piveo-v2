import sqlite3, csv

class ConstructionBDD:

    def __init__(self,chemin_bdd, chemin_CSV):
        self.chemin_bdd = chemin_bdd
        self.chemin_CSV = chemin_CSV
        if chemin_bdd.exists():
            chemin_bdd.unlink() # suppression et recréation de la base
        self.connexion = sqlite3.connect(self.chemin_bdd)
        self.curseur = self.connexion.cursor()
        self.creation_tables()
        self.remplissage_tables()

    def creation_tables(self)->None:
        """création des tables"""
        self.curseur.execute("""
            PRAGMA foreign_keys = ON;
        """)
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS personnes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prenom TEXT,
            nom TEXT,
            structure TEXT,
            photo TEXT                                      
        )
        """)
        self.connexion.commit()
        """création des tables"""
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS specialites(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            specialite TEXT                            
        )
        """)
        self.connexion.commit()
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS personnes_specialites (
        id_personne  INTEGER NOT NULL,
        id_specialite INTEGER NOT NULL,
        PRIMARY KEY (id_personne, id_specialite),
        FOREIGN KEY (id_personne)  REFERENCES personnes(id)  ON DELETE CASCADE,
        FOREIGN KEY (id_specialite) REFERENCES specialites(id) ON DELETE CASCADE
        )
        """)
        self.connexion.commit()
        self.curseur.execute("""
        CREATE INDEX IF NOT EXISTS idx_ps_personne  ON personnes_specialites(id_personne);
        """)
        self.curseur.execute("""
        CREATE INDEX IF NOT EXISTS idx_ps_specialite ON personnes_specialites(id_specialite);
        """)
    
    def remplissage_tables(self)->None:
        """remplissage des tables avec les fichiers CSV"""
        # table "personnes"
        chemin_personnes = self.chemin_CSV / "personnes.csv"
        with open(chemin_personnes, newline='', encoding="utf-8") as f:
            lecteur =csv.reader(f)
            next(lecteur) # on saute la première ligne
            for ligne in lecteur:
                nom, prenom, photo, structure = ligne
                self.curseur.execute("""
                INSERT INTO personnes(nom, prenom, photo, structure)
                VALUES(?, ?, ?, ?)
                """, (nom, prenom, photo, structure))                
        self.connexion.commit()
         # table "specialites"
        chemin_specialites = self.chemin_CSV / "specialites.csv"
        with open(chemin_specialites, newline='', encoding="utf-8") as f:
            lecteur =csv.reader(f)
            next(lecteur) # on saute la première ligne
            for ligne in lecteur:
                specialite = ligne[0]
                self.curseur.execute("""
                INSERT INTO specialites(specialite)
                VALUES(?)
                """, (specialite,))
        self.connexion.commit()
        # table "petsonnes_specialites
        chemin_personnes_specialites = self.chemin_CSV / "personnes_specialites.csv"
        with open(chemin_personnes_specialites, newline='', encoding="utf-8") as f:
            lecteur =csv.reader(f)
            next(lecteur) # on saute la première ligne
            for ligne in lecteur:
                id_personne, id_specialite = ligne
                self.curseur.execute("""
                INSERT INTO personnes_specialites(id_personne, id_specialite)
                VALUES(?, ?)
                """, (id_personne, id_specialite))
        self.connexion.commit()
