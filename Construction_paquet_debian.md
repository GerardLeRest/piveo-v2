# 1 - Récupération des sources et création de l’archive

- On récupère le dépôt Git complet de Piveo depuis GitHub. `git clone` crée le dossier
`~/construction-piveo/piveo-v2` s’il n’existe pas. On se déplace dans ce dossier :

```bash
git clone --branch base_propre https://github.com/GerardLeRest/piveo-v2.git ~/construction-piveo/piveo-v2
cd ~/construction-piveo/piveo-v2
```

**Remarque :** pour la première construction (voir ci-dessus), si le dépôt n'est pas encore présent dans `~/construction-piveo`, on le clone avec `git clone`.
Pour une nouvelle version, le dépôt existe déjà. Il ne faut pas le cloner à nouveau : on se place dans `piveo-v2` et on le met à jour avec `git pull` :

```bash
cd ~/construction-piveo/piveo-v2
git pull
```

- On crée l’archive `piveo_2.5.7.orig.tar.gz` à partir des fichiers
enregistrés dans le dernier commit de la branche (`HEAD`) :

```bash
git archive --format=tar.gz --prefix=piveo-2.5.7/ HEAD > ../piveo_2.5.7.orig.tar.gz
```

**Attention :** `../` place l’archive dans `~/construction-piveo`, à côté du dépôt (`~/construction-piveo/piveo-v2`).

# 2 - Dossier piveo-2.5.7

* On décompresse l'archive source amont `piveo_2.5.7.orig.tar.gz` avec la commande :
  
  ```bash
  cd ~/construction-piveo
  tar -xzf piveo_2.5.7.orig.tar.gz
  ```

* Cela crée automatiquement le dossier :
  
  `piveo-2.5.7/`

* Ce dossier devient le **répertoire de travail** pour construire le paquet Debian.

Il y a donc dans ~/construction-piveo :

* `piveo-v2/` → dépôt Git contenant les sources de développement
* `piveo_2.5.7.orig.tar.gz` → archive des sources amont 2.5.7
* `piveo-2.5.7/` → répertoire dans lequel sera réalisé le paquetage Debian

# 3 - étape 3 : Création de la structure Debian

On construit le dossier debian qui contiendra des fichiers de construction

```bash
cd piveo-2.5.7
mkdir debian
```

## Préparer `sbuild` sur Debian 13

`sbuild` construit le paquet dans un environnement Debian minimal et propre. La préparation de cet environnement se fait une seule fois sur la VM (Debian a été testé sur une machine virtuelle); on peut ensuite le réutiliser pour les versions suivantes de Piveo. Les commandes ci-dessous correspondent à Debian 13 (« trixie ») sur une machine `amd64`, avec le mode `schroot`.

### Installer les outils et autoriser l’utilisateur

Ces commandes sont à lancer dans une session root (`su -`). Si le compte Gérard n’a pas accès à `sudo`, il faut utiliser le mot de passe root défini pour cette VM.

```bash
apt update
apt install sbuild schroot debootstrap
sbuild-adduser gerard
```

La dernière commande ajoute `gerard` au groupe `sbuild`. Il faut **fermer la session puis se reconnecter** pour que cette appartenance soit prise en compte. Vérification après reconnexion :

```bash
id -nG
```

Le groupe `sbuild` doit apparaître dans la liste. 

### Créer l’environnement de construction

Cette opération télécharge un système Debian trixie minimal. Elle demande une connexion Internet et peut prendre quelques minutes.

```bash
sbuild-createchroot --include=eatmydata,ccache trixie /srv/chroot/trixie-amd64-sbuild https://deb.debian.org/debian
```

- `trixie` : version de Debian dans laquelle le paquet sera construit ;
- `/srv/chroot/trixie-amd64-sbuild` : dossier de cet environnement ;
- `--include=eatmydata,ccache` : outils facultatifs inclus dans l’environnement.

Vérifier que `schroot` voit l’environnement :

```bash
schroot -l
```

La liste doit contenir un environnement pour `trixie` et `amd64`. **Ne pas recréer l’environnement à chaque construction.** Une fois les fichiers `debian/` préparés (sections 3.1 à 3.10), on pourra lancer la construction avec `sbuild` depuis le dossier des sources du paquet.

## 3.1 debian/control

dans debian/control:

```bash
Source: piveo
Section: education
Priority: optional
Maintainer: Gérard Le Rest <gerard.lerest@orange.fr>
Build-Depends: debhelper-compat (= 13)
Standards-Version: 4.7.2
Rules-Requires-Root: no

Package: piveo
Architecture: all
Depends: ${misc:Depends},
         python3,
         python3-pyside6.qtwidgets
Description: application éducative d'association de prénoms et de visages
 Piveo est une application éducative permettant de travailler
 l'association entre des prénoms et des visages.
```

- optional: priorité normale pour ce logiciel. Cela ne concerne pas le fonctionnement de Debian.
- Build-Depends: debhelper-compat (= 13) : indique la version de debhelper utilisée pour construire le paquet
- Standards-Version: version des règles Debian prises comme référence
- Rules-Requires-Root: no: la construction ne nécessite pas les privilèges de root.
- Depends : dépendances nécessaires pour utiliser le paquet installé. L'installation de `python3-pyside6.qtwidgets` entraîne automatiquement celle de ses propres dépendances.
- ${misc:Depends}: permet à `debhelper` d’ajouter certaines dépendances automatiquement.

## 3.2 debian/changelog

La commande ci-dessous crée le fichier et ouvre un éditeur

```bash
dch --create --package piveo --newversion 2.5.7-1 --distribution trixie
```

Voici le fichier modifié:

```text
piveo (2.5.7-1) trixie; urgency=medium

  * Paquet Debian de Piveo 2.5.7.

 -- Maintainer: Prénom Nom <adresse@example.org>  Sat, 26 Sep 2026 13:02:21 +0200
```

## 3.3 debian/rules

```bash
#!/usr/bin/make -f

%:
        dh $@

override_dh_auto_build:
        # Rien à compiler

override_dh_auto_install:
        dh_auto_install
        install -D -m 0755 debian/piveo-launcher debian/piveo/usr/bin/piveo
```

- #!/usr/bin/make -f: interpréter par make
- %:...dh $@: règle make (pour les différentes étapes de construction du paquet, on laisse `dh` (debhelper) s'en charger.)
- override_dh_auto_build indique que Piveo est une application Python, il n'y a donc rien à compiler.
- override_dh_auto_install indique à debhelper quoi faire à cette étape. La première ligne lance dh_auto_install, qui tente l’installation automatique prévue par le projet. La seconde copie debian/piveo-launcher dans debian/piveo/usr/bin/piveo : c’est le dossier provisoire qui représente le contenu du futur paquet. L’option -D crée les dossiers nécessaires et -m 0755 donne au lanceur les droits d’exécution. Quand le .deb sera installé, ce fichier se trouvera dans /usr/bin/piveo.

Rendre le fichier exécutable:

```bash
chmod +x debian/rules
```

## 3.4 debian/piveo-launcher

Piveo-launcher debian sera le lanceur de l'application. Il permettra de taper simplement piveo dans le terminal pour lancer Piveo

```bash
#!/bin/bash

export PYTHONPATH="/usr/share/piveo"
exec python3 /usr/share/piveo/piveo.py "$@"
```

PYTHONPATH permet à Python de trouver les modules de Piveo dans /usr/share/piveo.
La deuxième ligne lance l'application.

Rendre le fichier piveo-launcher exécutable:

```bash
chmod +x debian/piveo-launcher
```

## 3.5 debian/install

- liste des fichiers à installer dans le futur paquet :

```bash
piveo.py usr/share/piveo/
controleur usr/share/piveo/
modele usr/share/piveo/
vue usr/share/piveo/
locales usr/share/piveo/
ressources usr/share/piveo/

debian/piveo.desktop usr/share/applications/
piveo.png usr/share/icons/hicolor/256x256/apps/
```

## 3.6 debian/piveo.desktop

```bash
[Desktop Entry]
Type=Application
Name=Piveo
Comment=Apprentissage des visages, prénoms et noms
Exec=piveo
Icon=piveo
Terminal=false
Categories=Education;
```

- Exec=piveo: le menu des applications exécutera /usr/bin/piveo.
- Icon=piveo: Debian recherchera une icône appelée piveo dans les emplacements standards.
- Terminal=false: aucun terminal ne s’ouvre quand Piveo est lancé depuis le menu.
- Categories=Education;: classe Piveo parmi les applications éducatives.

## 3.7 debian/source et debian/source/format

- debian/source:
  
  ```bash
  mkdir -p debian/source
  ```

- ligne de code:
  
  ```bash
  printf '3.0 (quilt)\n' > debian/source/format
  ```
  
  debian/source/format:
  
  ```text
  3.0 (quilt)
  ```

Ce fichier indique à Debian le format utilisé pour le paquet source.

## 3.8 Page de manuel

- debian/piveo.1:
  
  ```bash
  .TH PIVEO 1 "September 2026" "Piveo 2.5.7" "User Commands"
  .SH NAME
  piveo \- application for learning faces, first names and names
  .SH SYNOPSIS
  .B piveo
  .SH DESCRIPTION
  .B Piveo
  is an educational graphical application for learning and memorizing
  faces, first names and names of people.
  .SH OPTIONS
  Piveo does not currently provide command-line options.
  .SH AUTHOR
  Piveo was written by Gerard Le Rest.
  ```

- ligne de commande:
  
  ```bash
  printf 'debian/piveo.1\n' > debian/piveo.manpages
  ```
  
  debian/piveo.manpages:
  
  ```text
  debian/piveo.1
  ```

## 3.9 debian/copyright

debian/copyright:

```text
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: Pivéo

Files: *
Copyright: 2026 Gérard Le Rest
License: GPL-3

Files: ressources/fichiers/photos/*
Copyright: 2026 Gérard Le Rest
Comment: Portraits générés avec ChatGPT.
License: CC0-1.0

Files: ressources/fichiers/images/*
Copyright: 2026 Gérard Le Rest
Comment: Images créées pour Piveo, dont des captures d’écran
 et le portrait inconnu.jpg généré avec ChatGPT.
License: CC0-1.0

Files: piveo.ico
 piveo.png
 ressources/fichiers/images/piveo.png
 ressources/fichiers/logos/logoPiveo.png
Copyright: 2026 Gérard Le Rest
Comment: Icônes générées avec ChatGPT.
License: CC0-1.0
```

Le fichier complet contient aussi les paragraphes pour les icônes Google,
les icônes GNOME et les textes des licences.

# 4 - Construction et installation du paquet

Après la version 2.5.7, le dépôt local a été mis à jour avec git pull depuis la branche base_propre,
qui contenait la nouvelle image inconnu.jpg et l’adresse e-mail corrigée.
Une archive `piveo_2.5.8.orig.tar.gz` a été créée à partir de ce nouveau `HEAD`, puis
extraite dans `~/construction-piveo/piveo-2.5.8`. Les fichiers Debian
préparés pour la 2.5.7 ont été repris et adaptés : `debian/changelog`
indique `2.5.8-1`, la page de manuel indique 2.5.8 et
`debian/copyright` couvre les images et les autres fichiers.

Depuis `~/construction-piveo/piveo-2.5.8`, la commande de construction est :

```bash
sbuild --dist=trixie --arch=amd64
```

Pour cette version, la construction a réussi (`Status: successful` et
`Lintian: pass`). Le paquet se trouve dans
`~/construction-piveo/piveo_2.5.8-1_all.deb`. Sa page de manuel
`/usr/share/man/man1/piveo.1.gz` est présente.

Pour installer le paquet, depuis une session root (`su -`) :

```bash
apt install /home/gerard/construction-piveo/piveo_2.5.8-1_all.deb
```

Piveo 2.5.8 a été lancé dans la VM. L’ajout d’un élève et la suppression de
deux élèves ont fonctionné.
