# Utiliser Ubuntu comme image de base 
FROM ubuntu:22.04

# Étape de log
RUN echo "Je suis à l’étape ….."

# Empêcher les prompts interactifs (important pour apt)
ENV DEBIAN_FRONTEND=noninteractive

# Mettre à jour le système et installer curl
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean

# Commande par défaut à exécuter
CMD ["bash"]
