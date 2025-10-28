# OpenClassrooms_projet_5
Maintenez et documentez un système de stockage des données sécurisé et performant

# Description du projet 
L'objectif est de migrer des données d'un fichier CSV vers une base de données MongoDB via un script python, puis de tester l'integrité des données insérées via un script python, tout cela dans une architecture contenairisée (Docker).

# Pré-requis 
Avoir Docker déjà installé.

# Mise en place de l'architecture

## Container MongoDB contenant le serveur de base de données

Voir fichier Container/MongoDbServer/README.md

## Container python contenant le script de migration

Voir fichier Container/Python_migration/README.md

## Container python contenant le script de test

Voir fichier Container/Python_test/README.md
