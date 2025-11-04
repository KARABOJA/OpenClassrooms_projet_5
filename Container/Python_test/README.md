

# entrer dans le container de test afin de vérifier que la migration s'est bien effectué
docker exec -it "container ID" sh

# Revenir à la base 
cd ..

# se positionner dans le dossier ou se trouve le fichier .toml afin de créer l'environnement virtuel python
cd test/pytest

# Installer les dépendances contenu dans le fichier toml (pymongo, pandas, pytest)
poetry install

# activer l'environnement virtuel poetry
eval $(poetry env activate)

# se positionner dans le dossier ou se trouve le script
cd healthCare

# lancer le script avc pytest
pytest healthcare.py
