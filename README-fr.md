# Piveo

## Fonction du projet

Piveo (anciennement MémoVue) est une application éducative développée en Python avec une interface graphique PySide6, destinée aux écoles, aux entreprises et aux institutions.

Elle permet d’apprendre ou de retrouver les noms et prénoms des personnes à partir d'une base de données SQLite3.

Langues : Français, Anglais, Espagnol, Breton

<p align="center">
  <img src="ressources/fichiers/images/accueil.png" alt="Accueil">
</p>

## Fonctionnement

L'interface comporte trois zones :

- **Zone gauche** : affiche les informations sur la personne.
- **Zone en haut à droite** : permet de répondre aux questions.
- **Zone en bas à droite** : permet d'effectuer les réglages.

<p align="center">
  <img src="ressources/fichiers/images/interface.png" alt="Interface">
</p>

### Modes disponibles

1. **Lecture**
   
   - Permet de parcourir les personnes
   - Navigation via les boutons sous l’image
   - Mode aléatoire disponible

2. **Deviner**
   
   - Permet de réfléchir au nom et au prénom avant affichage

3. **Écrit**
   
   - Permet de saisir le nom et le prénom dans la zone en haut à droite

4. **Rechercher**
   
   - Permet de retrouver une ou plusieurs personnes

Le programme utilise :

- Python 3
- PySide6
- Des fichiers d'initialisation CSV
- Une base de données SQLite3

Trois organismes sont fournis par défaut (Établissement scolaire, Parlement, Entreprise), mais il est possible d’ajouter un organisme personnalisé (ex. : club de sport) en créant sa propre base de données, ses images et ses fichiers CSV.

Le choix de l’organisme se fait au lancement de l'application.

L’application est particulièrement utile pour mémoriser rapidement des visages et des noms dans un contexte professionnel ou scolaire.

## Vidéo

[Vidéo de présentation de Piveo](https://youtu.be/upmGYy93n2w)

## Installation

### 🔗 Depuis les sources

```bash
git clone https://github.com/GerardLeRest/Piveo
cd Fenetre
```

```bash
python3 -m venv mon_env
source mon_env/bin/activate
```

```bash
pip install pyside6
```

### 🪟 Windows

- Aller sur https://github.com/GerardLeRest/Piveo/releases/
- Télécharger "Piveo_Setup-X.X.X.exe"
- Installer et lancer le logiciel

### 🐧 GNU/Linux

#### 1. Télécharger l’archive AppImage

https://github.com/GerardLeRest/Piveo/releases

#### 2. Télécharger la dernière version

Exemple :
Piveo-X.X.X-x86_64.AppImage (X.X.X: version)

#### 3. Rendre l’AppImage exécutable

```bash
chmod +x ~/Piveo-X.X.X-x86_64.AppImage
```

#### 4. Lancer le logiciel

```bash
./Piveo-2.2.1-x86_64.AppImage
```

#### 5. Dossier de données de l’application

Linux :
~/.local/piveo

Windows :
C:\Users\username\.local\piveo

<p align="center">
  <img src="ressources/fichiers/images/piveo.png" alt="Icône">
</p>

## (Optionnel) Intégration au menu

```bash
sudo apt install alacarte
```

## Remarques

- Compatible Python 3.8+
- Testé sous Ubuntu et Windows
- L’application est en cours d’amélioration

## Liens

- https://gerardlerest.github.io/piveo/
- https://github.com/GerardLeRest/Piveo
- https://doc.ubuntu-fr.org/Piveo

## Protection des données

Ce logiciel fonctionne entièrement en local : aucune donnée n’est transmise ni stockée à distance.

L’utilisateur (ou l’organisme utilisant le logiciel) est responsable de l’usage des données qu’il importe. En cas d’utilisation de données personnelles (noms, photos, etc.), il doit s’assurer du respect de la réglementation en vigueur (notamment le RGPD).

## Licence & photos

Ce projet est distribué sous licence GPL-v3.  
© 2026 Gérard Le Rest

Les portraits ont été générés par une intelligence artificielle et sont utilisés dans un cadre pédagogique non commercial (https://generated.photos/)

Icônes : https://fonts.google.com/icons
