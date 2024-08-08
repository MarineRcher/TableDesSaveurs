# Utiliser une image officielle de Python comme image de base
FROM python:3.8-slim

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean

# Définir le répertoire de travail
WORKDIR /code

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . /code/

# Exposer le port utilisé par l'application
EXPOSE 5000

# Démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]

