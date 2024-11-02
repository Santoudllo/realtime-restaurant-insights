import os
import certifi
import json
from textblob import TextBlob
from kafka import KafkaProducer
from pymongo import MongoClient
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Récupérer les informations de connexion à MongoDB et Kafka
mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_dbname = os.getenv('MONGO_DBNAME')
kafka_broker = os.getenv('KAFKA_BROKER')
kafka_topic = os.getenv('KAFKA_TOPIC')

# Construire la chaîne de connexion MongoDB
mongo_uri = f"mongodb+srv://{mongo_username}:{mongo_password}@ailab.wku4a.mongodb.net/{mongo_dbname}?retryWrites=true&w=majority"

# Configuration de MongoDB
client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
db = client[mongo_dbname]
collection = db['Alimconfiance']

# Configuration de Kafka
producer = KafkaProducer(
    bootstrap_servers=kafka_broker,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Récupérer les avis clients depuis MongoDB (tous les documents)
def fetch_reviews():
    return collection.find()

# Analyser les avis clients avec TextBlob
def analyze_sentiment(text):
    try:
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positif'
        elif analysis.sentiment.polarity < 0:
            return 'negatif'
        else:
            return 'neutre'
    except Exception as e:
        print(f"Erreur lors de l'analyse du sentiment : {e}")
        return None

# Envoyer les résultats à Kafka
def send_to_kafka(data):
    producer.send(kafka_topic, value=data)
    producer.flush()
    print(f"Message envoyé au topic Kafka : {data}")

# Processus principal
def main():
    # Récupérer tous les avis de MongoDB
    reviews = fetch_reviews()
    
    # Analyser chaque avis et envoyer le résultat à Kafka
    for review in reviews:
        review_text = review.get('app_libelle_etablissement', '')  # Vous pouvez modifier ce champ selon la structure de vos données
        if review_text:
            sentiment = analyze_sentiment(review_text)
            if sentiment:
                data = {
                    "review_id": str(review["_id"]),
                    "review_text": review_text,
                    "sentiment": sentiment
                }
                send_to_kafka(data)

if __name__ == "__main__":
    main()
