# Commandes pour effectuer la migration des données du fichier CSV vers la base de donnée MongoDB

## Prérequis : "docker compose build" et "docker compose up" effectué, base de données mongoDb coneteneurisée et paramétrée

## entrer dans le container de migration afin d'effectuer la migration des données
docker exec -it "container ID" sh

## Revenir à la base 
cd ..

## se positionner dans le dossier ou se trouve le fichier .toml afin de créer l'environnement virtuel python
cd migration/csv_mongoDb

## Installer les dépendances contenu dans le fichier toml (pymongo)
poetry install

## activer l'environnement virtuel poetry
eval $(poetry env activate)

## se positionner dans le dossier ou se trouve le script
cd healthCare

## lancer le script de migration avec python
python healthcare.py
