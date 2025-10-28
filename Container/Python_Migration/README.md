# Build de l'image

## 1 : Se positionner dans le dossier où se trouve le dockerfile

## 2 : Build de l'image<br/>
Lancer la commande "docker build -t nomimage:flag ."<br/>
  - -t désigne"<br/>
  - le "." à la fin indique "<br/>

# Run du conteneur

## 1 : Lancer un conteneur<br/>
Lancer la commande "docker run -v folderToCopy:/migration -d -t nomimage"<br/>

# Install de l'environnement python avec Poetry

## 1 : Rentrer dans le conteneur afin de pouvoir interagir en ligne de commande<br/>
Lancer la commande "docker exec -it nomConteneur sh"<br/>

## 2 : Se positionner dans le dossier où se trouve le fichier pyproject.toml afin d'installer l'environnement virtuel python
Lancer les commandes suivantes :<br/>
"cd .."<br/>
"cd migration/csv_mongoDb"<br/>
"poetry install" afin d'installer l'environnement virtuel python<br/>
"eval $(poetry env activate)" afin de rentrer dans l'environnement virtuel python<br/>

# Lancement du script

Lancer les commandes :<br/>
"cd healthCare"<br/>
"python healthcare.py"<br/>
