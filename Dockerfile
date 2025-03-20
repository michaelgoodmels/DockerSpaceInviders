# Verwenden von Python als Basis-Image
FROM python:3.9-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere das Python-Skript in das Arbeitsverzeichnis
COPY space_invaders.py /app/

# Installiere pygame
RUN pip install pygame

# Definiere den Befehl zum Starten des Spiels
CMD ["python", "space_invaders.py"]
