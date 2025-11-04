FROM alpine:3.22

# Notre répertoire de travail sera la racine du système de fichier du conteneur
WORKDIR /·

COPY /test /test

# On met à jour les dépendances système afin de limiter les risques 
RUN apk update
RUN apk upgrade

# install build dependencies and needed tools
RUN apk add python3
RUN apk add poetry

# garder le container actif
CMD ["sh", "-c", "tail -f /dev/null"]
