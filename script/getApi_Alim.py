import requests
from dotenv import load_dotenv
import os

class BelibAPIClient:

    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, limit=20):
        try:
            # Afficher l'URL de l'API et la limite des enregistrements
            print(f"Récupération des données depuis l'API : {self.api_url} avec une limite : {limit}")

            response = requests.get(self.api_url, params={'limit': limit})

            # Afficher le code de statut de la réponse
            print(f"Code de statut de la réponse : {response.status_code}")

            # Afficher le contenu de la réponse
            print(f"Contenu de la réponse : {response.text}")

            if response.status_code == 200:
                json_data = response.json()
                total_records = json_data.get('total_count', None)  # Obtenir le nombre total d'enregistrements
                records = json_data.get('results', [])  # Obtenir les résultats
                return records, total_records
            else:
                print(f"Échec de la récupération des données. Code de statut : {response.status_code}, Réponse : {response.text}")
                return None, None

        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des données de l'API : {e}")
            return None, None

def main():
    # Charger les variables d'environnement
    load_dotenv()

    # Récupérer l'URL de l'API depuis le fichier .env
    api_url = os.getenv("API_URL")

    if not api_url:
        print("L'API_URL n'est pas définie dans le fichier .env.")
        return

    # Créer une instance du client API
    api_client = BelibAPIClient(api_url)

    # Récupérer les données depuis l'API
    data, total_records = api_client.fetch_data(limit=50)  
    if data:
        print(f"{len(data)} enregistrements récupérés avec succès depuis l'API.")
        if total_records is not None:
            print(f"Total des enregistrements dans l'API : {total_records}")
        else:
            print("Le nombre total d'enregistrements n'est pas disponible.")
    else:
        print("Échec de la récupération des données depuis l'API.")

if __name__ == "__main__":
    main()
