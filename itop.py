# Fichier de configuration pour la connexion aux webservices de iTop et pour la création du ticket

from dotenv import load_dotenv
import os



# Charger les informations sensibles depuis le fichier .env
load_dotenv()
ITOP_USER = os.getenv("ITOP-USER")
ITOP_PASSWORD = os.getenv("ITOP-PASSWORD")
ITOP_URL = os.getenv("ITOP-URL")