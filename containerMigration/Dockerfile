FROM alpine:3.22

# Notre répertoire de travail sera la racine du système de fichier du conteneur
WORKDIR /·

COPY /scripts /scripts
COPY /requirements.txt /requirements/requirements.txt
COPY --from=datatomigrate healthCare.csv /dataToMigrate/healthCare.csv

# On met à jour les dépendances système afin de limiter les risques 
RUN apk update
RUN apk upgrade

# install build dependencies and needed tools
RUN apk add $(cat /requirements/requirements.txt)

# lancer le script de migration
CMD ["python", "/scripts/scriptMigration.py"]