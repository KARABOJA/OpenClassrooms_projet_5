FROM mongodb/mongodb-community-server:latest

# Notre répertoire de travail sera la racine du système de fichier du conteneur
WORKDIR /·

#copy du script de création des utilisateurs
COPY ./scripts /docker-entrypoint-initdb.d
