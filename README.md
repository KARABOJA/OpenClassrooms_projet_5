# OpenClassrooms_projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

# Description du projet 
L'objectif est de migrer des données d'un fichier CSV vers une base de données MongoDB via un script python, puis de tester l'integrité des données insérées via un script python, tout cela dans une architecture containérisée (Docker).

# Pré-requis 
Avoir Docker déjà installé.

# Mise en place de l'architecture

## Dockerfile

  FROM alpine:3.22
  
  ### Notre répertoire de travail sera la racine du système de fichier du conteneur
  WORKDIR /·
  ### copie du dossier dans le container
  COPY /migration /migration
  
  ### On met à jour les dépendances système afin de limiter les risques 
  RUN apk update<br/>
  RUN apk upgrade
  
  ### install build dependencies and needed tools
  RUN apk add python3<br/>
  RUN apk add poetry
  
  ### garder le container actif
  CMD ["sh", "-c", "tail -f /dev/null"]


## Arborescence du dossier copié dans le container (dockerfile command lors du Build de l'image : COPY /migration /migration)
<img width="340" height="668" alt="image" src="https://github.com/user-attachments/assets/1e5beec5-f375-43a8-890e-66a179a7d08a" />

## contenu du fichier pyproject.toml

[project]<br/>
name = "csv-mongodb"<br/>
version = "0.1.0"<br/>
description = ""<br/>
authors = [{name = "******"}]<br/>
readme = "README.md"<br/>
requires-python = ">=3.12"<br/>
dependencies = ["pymongo (>=4.15.3,<5.0.0)"]<br/>
<br/>
[build-system]<br/>
requires = ["poetry-core>=2.0.0,<3.0.0"]<br/>
build-backend = "poetry.core.masonry.api"<br/>


## Lancement des scripts
