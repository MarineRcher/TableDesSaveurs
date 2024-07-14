# Dockerfile dans le dossier tds_api
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev

# Copier les fichiers de requirements
COPY requirements.txt /app/

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet
COPY . /app/

# Exposer le port de l'application
EXPOSE 5000

# Commande pour démarrer le serveur Django
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "tds_api.wsgi:application"]
