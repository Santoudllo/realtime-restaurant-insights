# src/data_ingestion_kedro/nodes/data_collection.py
import requests

def fetch_data_from_api(api_url: str, limit: int):
    try:
        response = requests.get(api_url, params={'limit': limit})
        if response.status_code == 200:
            json_data = response.json()
            records = json_data.get('results', [])
            total_records = json_data.get('total_count', None)
            return records, total_records
        else:
            raise ValueError(f"Échec de la récupération des données. Code de statut : {response.status_code}")
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la récupération des données : {e}")
