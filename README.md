# Installation

Installer un environnement virtuel, se placer dans le répertoire du dépot

    $ mkvirtualenv -ppython3 user_server

## Configuration du projet

Pour configurer le projet dans l'environnement virtuel, se placer dans le dossier user_server ( le plus haut dans l'arbre ) puis effectuer les commandes suivantes

    # Permet d'utiliser cdproject
    $ setvirtualenvproject $VIRTUAL_ENV $(pwd)

    # Edition du fichier postactivate
    $ echo "export DJANGO_SETTINGS_MODULE=user_server.settings.dev" >> $VIRTUAL_ENV/bin/postactivate

    # Edition du fichier postdeactivate
    $ echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

    # Rechargement de l'environnement virtuel
    $ workon user_server

## Installation des librairies

Pour installer les librairies

    $ cdproject
    $ pip install -r requirements/dev.txt

## Lancer le serveur de développement

Pour finaliser l'installation et lancer le serveur

    $ chmod u+x manage.py
    $ ./manage.py migrate
    $ ./manage.py runserver
