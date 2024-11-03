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
            
            print(f"Récupération des données depuis l'API : {self.api_url} avec une limite : {limit}")
            response = requests.get(self.api_url, params={'limit': limit})

           
            print(f"Code de statut de la réponse : {response.status_code}")

            if response.status_code == 200:
                json_data = response.json()
                total_records = json_data.get('total_count', None)  

                records = json_data.get('results', [])  

                if records:
                    print(f"Exemple de données reçues : {records[0]}")  
                return records, total_records
            else:
                print(f"Échec de la récupération des données. Code de statut : {response.status_code}, Réponse : {response.text}")
                return None, None

        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des données de l'API : {e}")
            return None, None


class MongoDBPipeline:
    def __init__(self):
       
        load_dotenv()

        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.dbname = os.getenv('MONGO_DBNAME')
        self.mongodb_uri = os.getenv('MONGO_URI').replace("<db_password>", self.password)

        
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
               
                documents = []
                for record in data:
                    document = record  
                    if document:  
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
      
        self.client.close()
        print("Connexion à MongoDB fermée.")

def main():
   
    load_dotenv()

    
    api_url = os.getenv("API_URL")

    if not api_url:
        print("L'API_URL n'est pas définie dans le fichier .env.")
        return

    
    api_client = AlimconfianceAPIClient(api_url)

   
    data, total_records = api_client.fetch_data(limit=50)  

    if data:
        print(f"{len(data)} enregistrements récupérés avec succès depuis l'API.")

        if total_records is not None:
            print(f"Total des enregistrements dans l'API : {total_records}")
        else:
            print("Le nombre total d'enregistrements n'est pas disponible.")

      
        mongo_pipeline = MongoDBPipeline()

        
        mongo_pipeline.insert_data_to_mongodb(data)

        mongo_pipeline.close_connection()
    else:
        print("Échec de la récupération des données depuis l'API.")


if __name__ == "__main__":
    main()