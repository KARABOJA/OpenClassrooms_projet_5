# Commandes pour paramétrer la base de donnée MongoDb

## Prérequis : "docker compose build" et "docker compose up" effectué

## entrer dans le container de base de donnée afin d'y exécuter des commandes
docker exec -it "container ID" sh

## se connecter en tant qu admin dans la base de donnée (défini dans le docker-compose)
mongosh -u mongoadmin

## rentrer le mot de passe demandé dans le prompt (défini dans le docker-compose)
mongopassword

## utiliser la base de donnée "admin"
use admin

## créer un utilisateur dev qui a des droits en lecture et en écriture dans la base de donnée test et prod
db.createUser(
  {
    user: "dev",
    pwd:  "dev", 
    roles: [ { role: "readWrite", db: "test" },
             { role: "readWrite", db: "prod" } ]
  }
)

## créer un utilisateur user qui a des droits en lecture dans la base de donnée prod
db.createUser(
  {
    user: "user",
    pwd:  "user", 
    roles: [ { role: "read", db: "prod" } ]
  }
)

## Vérifier que 3 utilisateurs existent (admin, dev, user)
db.system.users.find()

## Schéma de la base de données



## Schéma de la base de données format json


