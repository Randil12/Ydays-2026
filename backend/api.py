from fastapi import FastAPI
import random

# Initialisation de l'API
app = FastAPI(title="Backend Débutant")

input_message = []
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

@app.post("/api/message")
def recevoir_message(message: str):
    """Reçoit un message du client et le stocke dans une liste."""
    input_message.append(message)
    return {
        "statut": "succès",
        "message": f"Message reçu : {message}"
    }

@app.get("/api/messages")
def get_messages():
    """Renvoie tous les messages reçus du client."""
    return {
        "statut": "succès",
        "messages": input_message
    }