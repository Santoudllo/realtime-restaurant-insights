import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Configurer la connexion à Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Chemin vers le fichier CSV
csv_file_path = "../data/kafka_messages.csv"

# Charger les données CSV
data = pd.read_csv(csv_file_path)

# Nom de l'index Elasticsearch
index_name = "kafka_messages"

# Supprimer l'index s'il existe déjà
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# Créer un nouvel index
es.indices.create(index=index_name)

# Préparer les données pour Elasticsearch
def generate_data(df):
    for _, row in df.iterrows():
        yield {
            "_index": index_name,
            "_source": row.to_dict(),
        }

# Insérer les données dans Elasticsearch
bulk(es, generate_data(data))

print("Importation terminée avec succès.")
