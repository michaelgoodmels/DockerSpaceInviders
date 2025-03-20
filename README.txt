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
