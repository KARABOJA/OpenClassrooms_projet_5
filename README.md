# OpenClassrooms_projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

# Description du projet 
L'objectif est de migrer des données d'un fichier CSV vers une base de données MongoDB via un script python, puis de tester l'integrité des données insérées via un script python, tout cela dans une architecture contenairisée (Docker).

# Pré-requis 
Avoir Docker et docker compose déjà installé.

# Architecture

<img width="1152" height="648" alt="DockerSchema" src="https://github.com/user-attachments/assets/7b74e4a0-2cbc-4e97-aa74-898fd0a089c8" />

## Configuration du Docker-compose (dossier racine)

- docker-compose.yml
- default.env
- dossier vide : logs/
- secrets/DB_ROOT_LOGIN.txt
- secrets/DB_ROOT_PASSWORD.txt
- dataToMigrate/healthCare.csv
- conteneur MongoDB - dossier : containerDatabase/
- conteneur de migration - dossier : containerMigration/
- conteneur de test - dossier : containerTest/

## Configuration du container MongoDB (dossier containerDatabase/)

 - Dockerfile
 - requirements.txt
 - scripts/createUser.js

## Configuration du container python (dossier containerMigration/)

 - Dockerfile
 - requirements.txt
 - scripts/scriptMigration.py

## Configuration du container python (dossier containerTest/)

 - Dockerfile
 - requirements.txt
 - scripts/scriptTest.py

## Schéma json des données

<img width="508" height="425" alt="image" src="https://github.com/user-attachments/assets/4cf82f3a-73f0-46ed-9d7f-d49ff4a2c72f" />

## Lancement des conteneurs

### 1 : mettre son fichier CSV dans le dossier "dataToMigrate" (fichier déjà présent)

### 2 : Executer le fichier docker-compose.yml (création de la bdd, lancement de la migration, vérification de la migration) avec les commandes suivante :

docker compose build<br>
docker compose up

### 3 : ouvrir le dossier "resultatMigration" et verifier que le script d'erreur pytest n'a pas relevé d'erreurs (une erreur est volontairement faite afin que le fichier logs.xml soit crée)

