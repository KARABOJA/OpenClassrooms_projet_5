# Build de l'image

##1 : Se positionner dans le dossier où se trouve le dockerfile

##2 : Build de l'image
Lancer la commande "docker build -t nomimage:flag ."
  - -t désigne
  - le "." à la fin indique 

# Run du conteneur

##1 : Lancer un conteneur
Lancer la commande "docker run -d -t nomimage"

# Install de l'environnement python avec Poetry

##1 : Rentrer dans le conteneur afin de pouvoir interagir en ligne de commande
Lancer la commande "docker exec -it nomConteneur sh"

##2 : Se positionner dans le dossier où se trouve le fichier pyproject.toml afin d'installer l'environnement virtuel python
Lancer les commandes suivantes :
"cd .." 
"cd migration/csv_mongoDb"
"poetry install" afin d'installer l'environnement virtuel python
"eval $(poetry env activate)" afin de rentrer dans l'environnement virtuel python

# Lancement du script
Lancer les commandes : 
"cd healthCare"
"python healthcare.py"
