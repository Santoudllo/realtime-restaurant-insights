import os
import certifi
import json
from kafka import KafkaProducer
from pymongo import MongoClient
from dotenv import load_dotenv
from textblob import TextBlob  # Ajouter TextBlob comme alternative

# Charger les variables d'environnement
load_dotenv()

# Récupérer les informations de connexion à MongoDB et Kafka
mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_dbname = os.getenv('MONGO_DBNAME')
kafka_broker = os.getenv('KAFKA_BROKER')
kafka_topic = os.getenv('KAFKA_TOPIC')

# Construire MONGO_URI avec les informations disponibles
mongo_uri = f"mongodb+srv://{mongo_username}:{mongo_password}@ailab.wku4a.mongodb.net/{mongo_dbname}?retryWrites=true&w=majority"

# Configuration de MongoDB
try:
    client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
    db = client[mongo_dbname]
    collection = db['Alimconfiance']
    
    document = collection.find_one()
    if document:
        print("Connexion réussie à MongoDB. Voici un document exemple :", document)
    else:
        print("Connexion réussie à MongoDB, mais aucun document trouvé dans la collection.")
except Exception as e:
    print(f"Erreur lors de la connexion à MongoDB : {e}")
    exit(1)

# Configuration de Kafka
try:
    producer = KafkaProducer(
        bootstrap_servers=kafka_broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
except Exception as e:
    print(f"Erreur lors de la configuration de Kafka : {e}")
    exit(1)

# Récupérer les avis clients depuis MongoDB
def fetch_reviews(limit=3):
    return collection.find().limit(limit)

# Analyser les avis clients
def analyze_sentiment(text, use_textblob=True):
    if use_textblob:
        try:
            analysis = TextBlob(text)
            if analysis.sentiment.polarity > 0:
                return "positive"
            elif analysis.sentiment.polarity < 0:
                return "negative"
            else:
                return "neutre"
        except Exception as e:
            print(f"Erreur lors de l'analyse de l'avis avec TextBlob : {e}")
            return None
    else:
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"Analyse le sentiment de cet avis : \"{text}\". Réponds par 'positive', 'negative', ou 'neutre'.",
                max_tokens=10
            )
            sentiment = response.choices[0].text.strip().lower()
            return sentiment
        except Exception as e:
            print(f"Erreur lors de l'appel à l'API OpenAI : {e}")
            return None

# Envoyer les résultats à Kafka
def send_to_kafka(data):
    try:
        producer.send(kafka_topic, value=data)
        producer.flush()
        print(f"Message envoyé au topic Kafka : {data}")
    except Exception as e:
        print(f"Erreur lors de l'envoi du message à Kafka : {e}")

# Processus principal
def main():
    reviews = fetch_reviews(limit=3)
    for review in reviews:
        review_text = review.get('app_libelle_etablissement', '')  # Modifiez ce champ selon la structure de vos données
        if review_text:
            sentiment = analyze_sentiment(review_text, use_textblob=True)  # Changez `use_textblob=False` pour tester OpenAI
            if sentiment:
                data = {
                    "review_id": str(review["_id"]),
                    "review_text": review_text,
                    "sentiment": sentiment
                }
                send_to_kafka(data)

if __name__ == "__main__":
    main()
