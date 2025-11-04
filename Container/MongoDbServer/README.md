## Container MongoDB contenant le serveur de base de données

Téléchargement et run du container : mongodb/mongodb-community-server<br/>
ports binding lors du run (dans notre cas) : 27016:27017

## Création des utilisateurs de la base de données

### créer un utilisateur dev qui a des droits en lecture et en écriture dans la base de donnée test et prod
db.createUser(
  {
    user: "dev",
    pwd:  "dev", 
    roles: [ { role: "readWrite", db: "test" },
             { role: "readWrite", db: "prod" } ]
  }
)

### créer un utilisateur user qui a des droits en lecture dans la base de donnée prod
db.createUser(
  {
    user: "user",
    pwd:  "user", 
    roles: [ { role: "read", db: "prod" } ]
  }
)

## Schéma de la base de données



## Schéma de la base de données format json


