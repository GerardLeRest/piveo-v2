<p align="center">
  🇬🇧 English | <a href="README-fr.md">🇫🇷 Français</a>
</p>

GitHub repository: https://github.com/GerardLeRest/Piveo-v2

# Piveo

## Project overview

Piveo is a free and open-source application designed to help users learn first names, last names, and faces. It provides a practical alternative to traditional photo directories.

Typical use cases include teachers learning their students' names, teams onboarding new employees, and organizations managing large groups of people.

Each organization relies on an SQL-based database. Piveo simplifies its management through three CSV files located in the working directory (see below).

Available languages: French, English, Spanish, Breton

Piveo v2 is the current version of the software (v2.5.3).

<p align="center">
<img src="ressources/fichiers/images/accueil0.png" alt="Home">
</p>

## How it works

The interface is divided into three sections:

- **Left panel**: displays information about the person
- **Top-right panel**: allows the user to enter answers
- **Bottom-right panel**: contains settings

<p align="center">
<img src="ressources/fichiers/images/interface.png" alt="Interface">
</p>

## Available modes

1. **Browse**
   
   - Navigate through people
   - Use the buttons below the image
   - Random mode available

2. **Guess**
   
   - Encourages users to think of the name before revealing it
   - Random mode available

3. **Written**
   
   - Enter first and last names in the top-right panel
   - Random mode available

4. **Search**
   
   - Find one or multiple people

## Technologies

The application is built with:

- Python 3
- PySide6
- Initialization CSV files
- SQLite3 database
- CSV-based configuration

<p align="center">
<img src="ressources/fichiers/images/tableaux.png" alt="CSV tables">
</p>

## Default environments

Three environments are provided by default:

- Community
- School
- Company

The environment is selected when launching the application.

## Video

[Watch the presentation video](https://youtu.be/upmGYy93n2w)

## Installation

### 🔗 From source

```bash
git clone https://github.com/GerardLeRest/Piveo-v2
cd piveo-v2
```

```bash
python3 -m venv my_env
source my_env/bin/activate
```

```bash
pip install pyside6
```

### 🪟 Windows

- Go to: https://github.com/GerardLeRest/Piveo-v2/releases/
- Download Piveo_Setup-X.X.X.exe
- Install and run the application

### 🐧 GNU/Linux

#### 1. Download the AppImage

https://github.com/GerardLeRest/Piveo-v2/releases

#### 2. Get the latest version

Example:
Piveo-X.X.X-x86_64.AppImage

#### 3. Make it executable

```bash
chmod +x ~/Piveo-X.X.X-x86_64.AppImage
```

#### 4. Run the application

```bash
./Piveo-X.X.X-x86_64.AppImage
```

#### 5. Data directory

- Linux : ~/.local/piveo
- Windows : C:\Users\username\.local\piveo

<p align="center">
<img src="ressources/fichiers/images/piveo.png" alt="Icon">
</p>

## (Optional) Menu integration

```bash
sudo apt install alacarte
```

## Links

- Downloads (Piveo v2): https://github.com/GerardLeRest/piveo-v2/releases
- Official repository: https://github.com/GerardLeRest/Piveo-v2
- Documentation: https://doc.ubuntu-fr.org/Piveo
- Ubuntu-fr forum: https://forum.ubuntu-fr.org/viewtopic.php?id=2091784
- LinuxFr article: https://linuxfr.org/users/clisam/journaux/piveo-2-4-0-logiciel-d-apprentissage-de-prenoms-et-noms
- Website: https://gerardlerest.github.io/piveo

## Data protection

This software runs entirely locally: no data is transmitted or stored remotely.

Users are responsible for how imported data is used and must comply with applicable regulations (especially GDPR).

## License & Images

This project is distributed under the GPL-v3 license.
© 2026 Gérard Le Rest

Portraits were generated using artificial intelligence for non-commercial educational purposes:
https://generated.photos/

Icons: https://fonts.google.com/icons

## Keywords

photo directory, learn names, memorize faces, educational software, onboarding