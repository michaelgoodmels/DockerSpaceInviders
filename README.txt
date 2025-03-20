Das klingt nach einem spannenden Projekt! Um ein Docker-Projekt zu erstellen, das von Kubernetes verwaltet wird und das Spiel "Space Invaders" in Python enthält, sind mehrere Schritte erforderlich. Ich werde dir die wichtigsten Komponenten und einen Überblick über den Prozess geben:

### 1. **Erstellen des Space Invaders Spiels mit Python**
Zuerst müssen wir ein einfaches Space Invaders Spiel in Python erstellen. Hierzu werden wir eine Bibliothek wie `pygame` verwenden, die für die Erstellung von 2D-Spielen gut geeignet ist.

### 2. **Dockerfile erstellen**
Das Dockerfile definiert, wie die Docker-Umgebung aussehen soll, in der das Python-Spiel laufen wird.

### 3. **Kubernetes-Manifest erstellen**
Kubernetes wird verwendet, um das Docker-Image zu verwalten und das Spiel in einem Cluster zu starten. Wir erstellen ein Kubernetes-Deployment und einen Service, um das Spiel zugänglich zu machen.

### 4. **Docker und Kubernetes in einem CI/CD-Workflow integrieren (optional)**
Wenn du möchtest, kannst du auch ein CI/CD-System wie GitLab CI, GitHub Actions oder Jenkins verwenden, um das Projekt automatisch zu bauen und zu deployen.

---

### Schritt 1: **Space Invaders Spiel in Python mit Pygame**

Erstelle ein Python-Skript namens `space_invaders.py` mit einem einfachen Spiel. Hier ist ein sehr grundlegender Start, der Pygame verwendet:

```python
import pygame
import random

# Initialisierung von pygame
pygame.init()

# Bildschirmgrößen und Farben
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Spieler
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Alien
alien_width = 50
alien_height = 50
alien_speed = 3
aliens = []

# Projektile
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Spielschleife
def game_loop():
    global player_x, player_y
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Bewegung des Spielers
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])
        
        # Bewegung der Schüsse
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Bewegung der Aliens
        for alien in aliens:
            alien[1] += alien_speed
        
        # Kollisionen und Rendering
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))  # Spieler
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))  # Schüsse
        for alien in aliens:
            pygame.draw.rect(screen, (255, 0, 0), (alien[0], alien[1], alien_width, alien_height))  # Aliens

        pygame.display.flip()
        clock.tick(60)

# Aliens erzeugen
def generate_aliens():
    global aliens
    for i in range(5):  # 5 Reihen von Aliens
        for j in range(10):  # 10 Aliens pro Reihe
            aliens.append([j * (alien_width + 10), i * (alien_height + 10)])

generate_aliens()

if __name__ == "__main__":
    game_loop()
    pygame.quit()
```

Dieses Beispiel enthält einen grundlegenden Raumfahrer, der nach links und rechts bewegt werden kann und Schüsse abfeuert. Die Aliens erscheinen am oberen Rand und bewegen sich nach unten.

### Schritt 2: **Dockerfile erstellen**

Nun müssen wir ein Dockerfile erstellen, um das Python-Spiel in einem Docker-Container laufen zu lassen. Erstelle eine Datei namens `Dockerfile` im Projektordner:

```Dockerfile
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
```

### Schritt 3: **Kubernetes-Manifest erstellen**

Jetzt musst du ein Kubernetes-Deployment und einen Service einrichten, um das Docker-Image im Cluster zu verwalten.

Erstelle eine Datei namens `k8s-deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: space-invaders-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: space-invaders
  template:
    metadata:
      labels:
        app: space-invaders
    spec:
      containers:
      - name: space-invaders
        image: <dein-docker-image-name>  # Ersetze dies mit deinem Docker-Image-Namen
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: space-invaders-service
spec:
  selector:
    app: space-invaders
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

Dieses Manifest erstellt eine Deployment-Ressource und einen Service, der auf den Container zugreift.

### Schritt 4: **Kubernetes ausrollen**

1. Baue das Docker-Image:

   ```bash
   docker build -t <dein-docker-image-name> .
   ```

2. Lade das Docker-Image auf Docker Hub oder eine andere Container-Registry hoch.

3. Wende das Kubernetes-Manifest an:

   ```bash
   kubectl apply -f k8s-deployment.yaml
   ```

4. Überprüfe den Status des Deployments:

   ```bash
   kubectl get pods
   ```

5. Wenn du Kubernetes lokal verwendest, kannst du Minikube oder Kind (Kubernetes in Docker) verwenden, um das Deployment zu testen.

### Schritt 5: **Optional: CI/CD-Integration**

Du kannst das Projekt in ein CI/CD-Setup integrieren, um automatisch das Docker-Image zu bauen und zu deployen, wenn Codeänderungen vorgenommen werden.

---

Das sind die grundlegenden Schritte, um dein Space Invaders-Spiel in einem Docker-Container zu betreiben und von Kubernetes verwalten zu lassen. Wenn du weitere Details benötigst oder bei einem bestimmten Schritt Hilfe brauchst, lass es mich wissen!