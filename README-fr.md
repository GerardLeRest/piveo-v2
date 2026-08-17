<p align="center">
  Français | <a href="README.md">🇬🇧 English</a>
</p>

# Piveo – Logiciel libre et gratuit pour apprendre les prénoms, les noms et les visages

## Objectif du projet

Piveo est une **application libre et gratuite** qui aide les utilisateurs à apprendre les prénoms, les noms et les visages. Elle peut être considérée comme une alternative au trombinoscope traditionnel.

Les cas d'utilisation typiques incluent les enseignants souhaitant apprendre les noms de leurs élèves, les équipes accueillant de nouveaux employés ou les organisations gérant de grands groupes de personnes.

Chaque environnement repose sur une base de données SQL. Piveo simplifie l'administration grâce à trois fichiers de configuration CSV situés dans le répertoire de travail (voir ci-dessous).

**Langues disponibles :** français, anglais, espagnol, breton

**Systèmes d'exploitation :** GNU/Linux (testé sous Ubuntu 24.04 LTS), Windows

Piveo v2 est la version actuelle du logiciel (v2.5.3).

<p align="center">
<img src="ressources/fichiers/images/accueil0.png" alt="Écran d'accueil de Piveo">
</p>

## Fonctionnement

L'interface est divisée en trois parties :

* **Partie gauche :** affiche les informations concernant la personne
* **Partie supérieure droite :** permet à l'utilisateur de saisir ses réponses
* **Partie inférieure droite :** contient les paramètres

<p align="center">
<img src="ressources/fichiers/images/interface.png" alt="Interface utilisateur de Piveo">
</p>

### Modes disponibles

1. **Parcourir**
   
   * Permet de parcourir les personnes
   * Boutons de navigation situés sous l'image
   * Mode aléatoire disponible

2. **Deviner**
   
   * Encourage l'utilisateur à retrouver le nom avant de l'afficher
   * Mode aléatoire disponible

3. **Écrit**
   
   * Permet à l'utilisateur de saisir le prénom et le nom dans la partie supérieure droite
   * Mode aléatoire disponible

4. **Rechercher**
   
   * Permet de rechercher une ou plusieurs personnes

L'application repose sur les technologies suivantes :

* Python 3
* PySide6
* SQLite
* Initialisation et configuration à l'aide de fichiers CSV

<p align="center">
<img src="ressources/fichiers/images/tableaux.png" alt="Structure des fichiers de configuration CSV de Piveo">
</p>

Trois environnements sont fournis par défaut :

* **Communauté**
* **École**
* **Entreprise**

L'environnement est sélectionné au lancement de l'application.

## Vidéo

Vidéo de présentation de Piveo :

https://youtu.be/upmGYy93n2w

## Installation

### 🔗 Depuis les sources

```bash
git clone https://github.com/GerardLeRest/Piveo-v2
cd Piveo-v2
```

```bash
python3 -m venv my_env
source my_env/bin/activate
```

```bash
pip install pyside6
```

### 🪟 Windows

Rendez-vous sur :

https://github.com/GerardLeRest/Piveo-v2/releases

Téléchargez :

`Piveo_Setup-X.X.X.exe`

Installez puis lancez le logiciel.

### 🐧 GNU/Linux

#### 1. Télécharger le paquet .deb

Rendez-vous sur :

https://github.com/GerardLeRest/Piveo-v2/releases

Téléchargez la dernière version.

Exemple :

`piveo_X.X.X-Y_amd64.deb`

* `X.X.X` = version de Piveo
* `Y` = révision du paquet Debian

#### 2. Installer le paquet

```bash
sudo apt install ./piveo_X.X.X-Y_amd64.deb
```

#### 3. Lancer l'application

In a terminal:

```bash
piveo
```

ou cliquez sur l'icône Piveo dans le menu des applications.

#### 4. Répertoire des données

Les données de l'utilisateur sont stockées dans :

* GNU/Linux : `~/.local/piveo`
* Windows : `C:\Users\username\.local\piveo`

<p align="center">
<img src="ressources/fichiers/images/piveo.png" alt="Icône de Piveo">
</p>

## Intégration facultative au menu

Sous GNU/Linux, le menu des applications peut être personnalisé à l'aide d'Alacarte :

```bash
sudo apt install alacarte
```

## Liens

* Téléchargements (Piveo v2) :
  https://github.com/GerardLeRest/Piveo-v2/releases
* Documentation :
  https://doc.ubuntu-fr.org/Piveo
* Forum Ubuntu-fr :
  https://forum.ubuntu-fr.org/viewtopic.php?id=2091784
* Article LinuxFr :
  https://linuxfr.org/users/clisam/journaux/piveo-2-4-0-logiciel-d-apprentissage-de-prenoms-et-noms
* Site web :
  https://gerardlerest.github.io/piveo

## Protection des données

Ce logiciel fonctionne entièrement hors ligne : aucune donnée n'est transmise ni stockée à distance.

L'utilisateur (ou l'organisation utilisant le logiciel) est responsable de l'utilisation des données importées. En cas d'utilisation de données personnelles (noms, photos, etc.), l'utilisateur doit veiller au respect de la réglementation applicable, notamment du RGPD.

## Licence et images

Ce projet est distribué sous licence GPL-v3.
© 2026 Gérard Le Rest

Les portraits ont été générés à l'aide de l'intelligence artificielle et sont utilisés à des fins éducatives non commerciales :

https://generated.photos/

Icônes :

https://fonts.google.com/icons
