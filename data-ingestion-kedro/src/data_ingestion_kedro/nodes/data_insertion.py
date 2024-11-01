# src/data_ingestion_kedro/nodes/data_insertion.py
import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

def insert_data_to_mongodb(data):
    load_dotenv()

    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    dbname = os.getenv('MONGO_DBNAME')
    mongodb_uri = os.getenv('MONGO_URI').replace("<db_password>", password)

    if not username or not password or not dbname or not mongodb_uri:
        raise ValueError("Les informations de connexion MongoDB sont manquantes dans les variables d'environnement.")

    client = MongoClient(
        mongodb_uri,
        tls=True,
        tlsCAFile=certifi.where()
    )

    db = client[dbname]
    collection = db['Alimconfiance']
    try:
        if data:
            result = collection.insert_many(data)
            return len(result.inserted_ids)
        else:
            return 0
    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'insertion dans MongoDB : {e}")
    finally:
        client.close()
