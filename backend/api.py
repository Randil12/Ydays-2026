from fastapi import FastAPI
import random

# Initialisation de l'API
app = FastAPI(title="Backend Débutant")

# Une seule route, la plus simple possible (GET)
@app.get("/api/message")
def generer_message():
    """Renvoie un message aléatoire au client qui le demande."""
    phrases = [
        "Le backend a bien reçu ta demande.",
        "La simplicité est la sophistication suprême.",
        "Arrête de brûler les étapes et comprends les bases.",
        "Le serveur tourne parfaitement."
    ]
    
    # On renvoie un dictionnaire Python, qui sera converti en JSON par FastAPI
    return {
        "statut": "succès",
        "message": random.choice(phrases)
    }