🇫🇷 [Lire la version française](README_FR.md)

GitHub repository: https://github.com/GerardLeRest/Piveo-v2

# Piveo - Learn first and last names for free

## Project goal

Piveo is a free and open-source application designed to learn and memorize first names, last names, and faces (directory software) for schools, companies, and organizations.  
Typical use cases include teachers learning their students’ names, teams onboarding new employees, or organizations managing large groups of people.

It allows users to learn or retrieve people’s first and last names from an SQLite3 database.

Languages: French, English, Spanish, Breton

Piveo v2 is the current version of the software (v2.5.3).

<p align="center">
<img src="ressources/fichiers/images/accueil.png" alt="Home">
</p>

## How it works

The interface is divided into three areas:

- **Left panel**: displays information about the person
- **Top-right panel**: allows the user to enter answers
- **Bottom-right panel**: contains the settings

<p align="center">
<img src="ressources/fichiers/images/interface.png" alt="Interface">
</p>

### Available modes

1. **Browse**
   - Allows you to navigate between people
   - Navigation is done using the buttons below the image
   - Random mode available
2. **Guess**
   - Encourages the user to think of the name before it is displayed
   - Random mode available
3. **Written**
   - Allows the user to enter the first and last name in the top-right panel
   - Random mode available
4. **Search**
   - Allows you to find one or more people

The program uses:

- Python 3
- PySide6
- CSV initialization files
- SQLite3 database

Three default environments are provided:
- Community
- School
- Company

The environment is selected when the application starts.

## Video

[Piveo presentation video](https://youtu.be/upmGYy93n2w)

## Installation

### 🔗 From source

```bash
git clone https://github.com/GerardLeRest/Piveo
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

- Go to: https://github.com/GerardLeRest/Piveo/releases/
- Download "Piveo_Setup-X.X.X.exe"
- Install and run the software

### 🐧 GNU/Linux

#### 1. Download the AppImage

https://github.com/GerardLeRest/Piveo/releases

#### 2. Download the latest version

Example:
Piveo-X.X.X-x86_64.AppImage (X.X.X: version)

#### 3. Make it executable

```bash
chmod +x ~/Piveo-X.X.X-x86_64.AppImage
```

#### 4. Run the application

```bash
./Piveo-X.X.X-x86_64.AppImage
```

#### 5. Data directory

Directory where user data is stored:  
Linux   : ~/.local/piveo  
Windows : C:\Users\username\.local\piveo

<p align="center">
<img src="ressources/fichiers/images/piveo.png" alt="Icon">
</p>

## (Optional) Menu integration

```bash
sudo apt install alacarte
```

## Why choose Piveo?

* **Full privacy**: Works 100% locally (GDPR compliant). Ideal for schools.
* **Multi-environment**: Modes adapted for Schools, Companies, or Communities.
* **Effective method**: Learning by typing (active memorization), not just multiple-choice questions.
* **Cross-platform**: Available as `.exe` for Windows and `AppImage` for Linux.
* **Multilingual**: Supports French, English, Spanish, and Breton.

## Notes

- Compatible with Python 3.8+
- Tested on Ubuntu and Windows
- Application under development

## Links

- Downloads (Piveo v2): https://github.com/GerardLeRest/piveo-v2/releases
- Official repository (Piveo v2): https://github.com/GerardLeRest/Piveo-v2
- Documentation: https://doc.ubuntu-fr.org/Piveo
- Ubuntu-fr forum: https://forum.ubuntu-fr.org/viewtopic.php?id=2091784
- LinuxFr article: https://linuxfr.org/users/clisam/journaux/piveo-2-4-0-logiciel-d-apprentissage-de-prenoms-et-noms
- Website (Piveo): https://gerardlerest.github.io/piveo-v2

## Data protection

This software runs entirely locally: no data is transmitted or stored remotely.

The user (or the organization using the software) is responsible for how imported data is used. When using personal data (names, photos, etc.), they must ensure compliance with applicable regulations, especially the GDPR.

## License & Images

This project is distributed under the GPL-v3 license.  
© 2026 Gérard Le Rest

The portraits were generated using artificial intelligence and are used for non-commercial educational purposes (https://generated.photos/).

Icons: https://fonts.google.com/icons

## Keywords

directory software, learn names, memorize faces, educational and professional software, onboarding new members
