 🇫🇷 [Lire la version française](README-fr.md)

# Piveo

## Project Purpose

Piveo (formerly MémoVue) is an educational application developed in
Python with a PySide6 graphical interface, designed for schools,
companies, and institutions.

It allows users to learn or recall people's first and last names from a
SQLite3 database.

Languages: French, English, Spanish, Breton

<p align="center">
<img src="ressources/fichiers/images/accueil.png" alt="Home">
</p>

## How It Works

The interface is divided into three areas:

- **Left panel**: displays information about the person\
- **Top-right panel**: allows the user to answer questions\
- **Bottom-right panel**: contains settings

<p align="center">
<img src="ressources/fichiers/images/interface.png" alt="Interface">
</p>

### Available Modes

1. **Browse**
   - Allows navigation through people\
   - Navigation via buttons below the image\
   - Random mode available
2. **Guess**
   - Encourages thinking about the name before display
3. **Written**
   - Allows entering first and last name in the top-right panel
4. **Search**
   - Allows finding one or more people

The program uses:

- Python 3\
- PySide6\
- CSV initialization files\
- SQLite3 database

Three default environments are provided (School, Parliament, Company),
but it is possible to create a custom one (e.g., sports club) by
building your own database, images, and CSV files.

The environment is selected when launching the application.

The application is particularly useful for quickly memorizing faces and
names in professional or educational contexts.

## Video

[Presentation video of Piveo](https://youtu.be/upmGYy93n2w)

## Installation

### 🔗 From source

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

- Go to: https://github.com/GerardLeRest/Piveo/releases/\
- Download "Piveo_Setup-X.X.X.exe"\
- Install and run the software

### 🐧 GNU/Linux

#### 1. Download the AppImage

https://github.com/GerardLeRest/Piveo/releases

#### 2. Download the latest version

Example:\
Piveo-2.2.1-x86_64.AppImage

#### 3. Make it executable

```bash
chmod +x ~/Piveo-2.2.1-x86_64.AppImage
```

#### 4. Run the application

```bash
./Piveo-2.2.1-x86_64.AppImage
```

<p align="center">
<img src="ressources/fichiers/images/piveo.png" alt="Icon">
</p>

## (Optional) Menu Integration

```bash
sudo apt install alacarte
```

## Notes

- Compatible with Python 3.8+\
- Tested on Ubuntu and Windows\
- Application under active development

## Links

- https://gerardlerest.github.io/piveo/\
- https://github.com/GerardLeRest/Piveo\
- https://doc.ubuntu-fr.org/Piveo

## License & Images

This project is distributed under the GPL-v3 license.\
© 2026 Gérard Le Rest

The portraits were generated using artificial intelligence and are used
for non-commercial educational purposes (https://generated.photos/).

Icons: https://fonts.google.com/icons
