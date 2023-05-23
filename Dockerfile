# Utilisez une image python de base
FROM python:3.10.11-slim-buster

# Spécifiez le répertoire de travail
WORKDIR /app

# Installer les dépendances requises pour l'application
COPY api.py .
COPY cookies.json .
COPY requirement.txt .
RUN pip install -r requirement.txt

# Exposer le port 8000 pour l'application FastAPI
EXPOSE 7000

# Lancer l'application avec Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7000"]
