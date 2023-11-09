import imaplib
from email import message_from_string
from dotenv import load_dotenv
import os
import re

# Charger les informations sensibles depuis le fichier .env
load_dotenv()
EMAIL = os.getenv("MAIL-USER")
MAIL_PASSWORD = os.getenv("MAIL-PASSWORD")
IMAP_SERVER = os.getenv("SERVEUR-MAIL")
IMAP_PORT = os.getenv("PORT-IMAP-MAIL")

# Se connecter au serveur IMAP
imap_server = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# S'authentifier avec votre adresse e-mail et mot de passe
imap_server.login(EMAIL, MAIL_PASSWORD)

# Sélectionner la boîte de réception
imap_server.select("inbox")

# Recherche d'e-mails avec un objet spécifique
search_criteria = r'(X-GM-RAW "subject:\"Enregistrement du \"") UNSEEN'
status, email_ids = imap_server.search(None, search_criteria)
# print('STATUS: ', status)

# Vérifier si la recherche a abouti
if status == "OK":
    email_ids = email_ids[0].split()
    for email_id in email_ids:
        # Marquer l'e-mail comme lu
        imap_server.store(email_id, '+FLAGS', '(\Seen)')
        # Maintenant, vous pouvez extraire et traiter les e-mails correspondants
        status, email_data = imap_server.fetch(email_id, '(RFC822)')
        # print('STATUS: ', status)
        if status == "OK":
            email_text = email_data[0][1]
            msg = message_from_string(email_text.decode('utf-8'))
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    email_text = part.get_payload(decode=True).decode(part.get_content_charset())
                    # print(email_text)

                    # Utiliser une expression régulière pour extraire les informations
                    match = re.search(r'Le départ de (.*?) (.*?) \((.*?)\) a été enregistré avec une date de sortie au ([\w\s]+ [\d]+ [\w\s]+ [\d]+)', email_text)
                    if match:
                        nom = match.group(1)
                        prenom = match.group(2)
                        ipn = match.group(3)
                        date_depart = match.group(4)
                        print(f"NOM: {nom}")
                        print(f"PRENOM: {prenom}")
                        print(f"IPN: {ipn}")
                        print(f"DATE DE DEPART: {date_depart}")
else:
    print("Aucun e-mail non lu correspondant à la recherche.")

# Fermer la connexion IMAP lorsque vous avez terminé
imap_server.logout()
