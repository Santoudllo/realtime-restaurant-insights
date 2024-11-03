import requests
import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

# Classe pour interagir avec l'API Alimconfiance
class AlimconfianceAPIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, limit=20):
        try:
            # Afficher l'URL de l'API et la limite des enregistrements
            print(f"Récupération des données depuis l'API : {self.api_url} avec une limite : {limit}")
            response = requests.get(self.api_url, params={'limit': limit})

            # Afficher le code de statut de la réponse
            print(f"Code de statut de la réponse : {response.status_code}")

            # Vérifier si la requête est réussie
            if response.status_code == 200:
                json_data = response.json()
                total_records = json_data.get('total_count', None)  # Obtenir le nombre total d'enregistrements

                # Les enregistrements se trouvent directement dans 'results'
                records = json_data.get('results', [])  # Assurez-vous d'obtenir la bonne clé

                # Afficher un exemple de données reçues pour vérification
                if records:
                    print(f"Exemple de données reçues : {records[0]}")  # Afficher un exemple de données reçues
                return records, total_records
            else:
                print(f"Échec de la récupération des données. Code de statut : {response.status_code}, Réponse : {response.text}")
                return None, None

        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des données de l'API : {e}")
            return None, None

# Classe pour gérer l'insertion dans MongoDB
class MongoDBPipeline:
    def __init__(self):
        # Charger les variables d'environnement
        load_dotenv()

        # Récupérer les informations de connexion depuis les variables d'environnement
        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.dbname = os.getenv('MONGO_DBNAME')
        self.mongodb_uri = os.getenv('MONGO_URI').replace("<db_password>", self.password)

        # Vérifier si les informations de connexion sont disponibles
        if not self.username or not self.password or not self.dbname or not self.mongodb_uri:
            raise ValueError("Les informations de connexion MongoDB sont manquantes dans les variables d'environnement.")

        # Initialiser la connexion à MongoDB
        self.client = MongoClient(
            self.mongodb_uri,
            tls=True,
            tlsCAFile=certifi.where()
        )

        self.db = self.client[self.dbname]
        self.collection = self.db['Alimconfiance']  # Nom de la collection

    def insert_data_to_mongodb(self, data):
        try:
            if data:
                # Insérer les enregistrements directement dans MongoDB
                documents = []
                for record in data:
                    document = record  # Chaque 'record' est déjà un dictionnaire contenant les champs nécessaires
                    if document:  # Assurez-vous qu'il y a des données à insérer
                        documents.append(document)

                if documents:
                    result = self.collection.insert_many(documents)
                    print(f"{len(result.inserted_ids)} documents insérés dans MongoDB.")
                else:
                    print("Aucune donnée à insérer après traitement.")
            else:
                print("Aucune donnée reçue de l'API à insérer.")
        except Exception as e:
            print(f"Erreur lors de l'insertion des données dans MongoDB : {e}")

    def close_connection(self):
        # Fermer la connexion MongoDB
        self.client.close()
        print("Connexion à MongoDB fermée.")

# Fonction principale
def main():
    # Charger les variables d'environnement
    load_dotenv()

    # Récupérer l'URL de l'API depuis le fichier .env
    api_url = os.getenv("API_URL")

    if not api_url:
        print("L'API_URL n'est pas définie dans le fichier .env.")
        return

    # Créer une instance du client API
    api_client = AlimconfianceAPIClient(api_url)

    # Récupérer les données depuis l'API
    data, total_records = api_client.fetch_data(limit=50)  # Exemple avec une limite de 50 enregistrements

    if data:
        print(f"{len(data)} enregistrements récupérés avec succès depuis l'API.")

        if total_records is not None:
            print(f"Total des enregistrements dans l'API : {total_records}")
        else:
            print("Le nombre total d'enregistrements n'est pas disponible.")

        # Initialiser le pipeline MongoDB
        mongo_pipeline = MongoDBPipeline()

        # Insérer les données dans MongoDB
        mongo_pipeline.insert_data_to_mongodb(data)

        # Fermer la connexion MongoDB
        mongo_pipeline.close_connection()
    else:
        print("Échec de la récupération des données depuis l'API.")

# Point d'entrée du script
if __name__ == "__main__":
    main()