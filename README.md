# OpenClassrooms_projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

# Description du projet 
L'objectif est de migrer des données d'un fichier CSV vers une base de données MongoDB via un script python, puis de tester l'integrité des données insérées via un script python, tout cela dans une architecture contenairisée (Docker).

# Pré-requis 
Avoir Docker et docker compose déjà installé.

# Architecture

<img width="1152" height="648" alt="DockerSchema" src="https://github.com/user-attachments/assets/c22d60e4-bce1-4020-a973-b87459ab7e52" />

## Container MongoDB contenant le serveur de base de données

Voir fichier Container/MongoDbServer/README.md

## Container python contenant le script de migration

Voir fichier Container/Python_migration/README.md

## Container python contenant le script de test

Voir fichier Container/Python_test/README.md

## Schéma json des données

<img width="1298" height="750" alt="image" src="https://github.com/user-attachments/assets/7ee4c254-63c2-45ff-92c6-e67223a450cf" />

## Lancement des conteneurs

### 1 : mettre son fichier CSV dans le dossier "dataToMigrate"

### 2 : Executer le fichier docker-compose.yml (création de la bdd, lancement de la migration, vérification de la migration) avec les commandes suivante :

docker compose build<br>
docker compose up

### 3 : ouvrir le doccier "resultatMigration" et verifier que le script d'erreur pytest n'a pas relevé d'erreurs (une erreur est volontairement faite afin que le fichier logs.xml soit crée)

