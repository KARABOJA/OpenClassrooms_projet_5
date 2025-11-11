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

