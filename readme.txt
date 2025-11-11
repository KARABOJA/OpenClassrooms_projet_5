# 1 : prérequis : avoir docker et docker compose installé

# 2 : mettre son fichier CSV dans le dossier "dataToMigrate"

# 3 : Executer le fichier docker-compose.yml (création de la bdd, lancement de la migration, vérification de la migration) avec les commandes suivante :

docker compose build
docker compose up

# 4 : ouvrir le fichier "resultatMigration" (situé dans le conteneur de test) et verifier que le script d'erreur pytest n'a pas relevé d'erreurs (une erreur est volontairement faite afin de verifier le bon fonctionnement de l'architecture Docker)