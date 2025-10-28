# OpenClassrooms_projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

# Description du projet 
L'objectif est de migrer des données d'un fichier CSV vers une base de données MongoDB via un script python, puis de tester l'integrité des données insérées via un script python, tout cela dans une architecture containérisée (Docker).

# Pré-requis 
Avoir Docker déjà installé.

# Mise en place de l'architecture

## Container MongoDB contenant le serveur de base de données

Téléchargement et run du container : mongodb/mongodb-community-server<br/>
ports binding lors du run (dans notre cas) : 27016:27017

## Container python contenant le script de migration

### Dockerfile

  FROM alpine:3.22
  
  \# Notre répertoire de travail sera la racine du système de fichier du conteneur<br/>
  WORKDIR /·<br/>
  
  \# copie du dossier dans le container<br/>
  COPY /migration /migration<br/>
  
  \# On met à jour les dépendances système afin de limiter les risques <br/>
  RUN apk update<br/>
  RUN apk upgrade<br/>
  
  \# install build dependencies and needed tools<br/>
  RUN apk add python3<br/>
  RUN apk add poetry<br/>
  
  \# garder le container actif<br/>
  CMD ["sh", "-c", "tail -f /dev/null"]<br/>


### Arborescence du dossier copié dans le container (command dockerfile : COPY /migration /migration)
<img width="340" height="668" alt="image" src="https://github.com/user-attachments/assets/1e5beec5-f375-43a8-890e-66a179a7d08a" />

### contenu du fichier pyproject.toml

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


## Container python contenant le script de test
