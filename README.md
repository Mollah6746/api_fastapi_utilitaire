# 🚀 API Utilitaire de Traitement de Texte (FastAPI)

Une API REST moderne et performante construite avec Python et le framework FastAPI. Ce projet démontre la création d'un service backend capable de recevoir des données JSON, de les valider et de les traiter.

## 🎯 Fonctionnalités

* **Endpoint d'analyse (`POST /analyser-texte`) :** Reçoit un texte et renvoie des statistiques détaillées (nombre de mots, nombre de caractères, conversion en majuscules).
* **Validation des données :** Utilisation de Pydantic pour s'assurer que les données d'entrée respectent le format attendu.
* **Documentation automatique :** Interface Swagger UI interactive intégrée pour tester l'API facilement.

## 🛠️ Stack Technique

* Python 3.x
* [FastAPI](https://fastapi.tiangolo.com/) (Framework Web)
* [Uvicorn](https://www.uvicorn.org/) (Serveur ASGI)
* Pydantic (Validation de données)

## 💻 Installation et Démarrage Local

Pour faire tourner cette API sur votre machine, suivez ces étapes :

### 1. Cloner le projet et préparer l'environnement

Il est recommandé d'utiliser un environnement virtuel.

```bash
# Cloner le dépôt
git clone [https://github.com/VOTRE-NOM/mon-api-fastapi.git](https://github.com/VOTRE-NOM/mon-api-fastapi.git)
cd mon-api-fastapi

# Créer un environnement virtuel (Windows)
python -m venv venv
.\venv\Scripts\Activate

# Créer un environnement virtuel (Mac/Linux)
# python3 -m venv venv
# source venv/bin/activate