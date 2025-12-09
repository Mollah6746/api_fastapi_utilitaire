# 1. On importe FastAPI ET BaseModel de Pydantic
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# --- MODÈLE DE DONNÉES (C'est nouveau !) ---
# On crée une classe pour définir à quoi doivent ressembler
# les données que l'utilisateur nous envoie.
# Ici, on s'attend à recevoir un objet JSON avec un champ "contenu" qui est du texte (str).
class TexteInput(BaseModel):
    contenu: str

# --- ROUTES ---

@app.get("/")
def lire_racine():
    return {"message": "Bienvenue sur mon API utilitaire ! Va sur /docs pour la tester."}

# Notre nouvelle route utilitaire.
# Note le @app.post au lieu de @app.get, car on ENVOIE des données.
@app.post("/analyser-texte")
def analyser_mon_texte(texte_recu: TexteInput):
    """
    Prend un texte en entrée et renvoie des statistiques dessus.
    """
    # FastAPI a déjà vérifié que 'texte_recu' correspondait au modèle TexteInput.
    # On récupère la vraie chaîne de caractères dedans :
    data = texte_recu.contenu

    # --- Logique "métier" (notre traitement) ---
    nb_caracteres_total = len(data)
    # On sépare les mots par les espaces pour les compter
    mots = data.split()
    nb_mots = len(mots)
    # On met tout en majuscules
    en_majuscules = data.upper()

    # --- On renvoie le résultat en JSON ---
    return {
        "analyse": {
            "caracteres": nb_caracteres_total,
            "mots": nb_mots,
            "version_majuscule": en_majuscules
        },
        "texte_original_recu": data
    }