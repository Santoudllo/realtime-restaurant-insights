import json
import csv
import pandas as pd
import uuid
from kafka import KafkaConsumer

# Initialisation du consommateur Kafka avec un group_id unique
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=f'my-group-{uuid.uuid4()}',  # Utiliser un UUID pour obtenir un group_id unique à chaque exécution
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=60000  # Augmenté à 60 secondes pour avoir plus de temps pour la lecture des messages
)

# Nom du fichier CSV
output_csv_file = '/home/santoudllo/Desktop/PROJETS/realtime-restaurant-insights/data/kafka_messages.csv'  # Sauvegarde dans le dossier spécifié

# Initialisation du fichier CSV avec l'en-tête des colonnes
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Définir l'en-tête du CSV
    writer.writerow(['review_id', 'review_text', 'sentiment'])

    # Boucle pour lire les messages du Kafka consumer
    message_count = 0
    for message in consumer:
        # Récupérer la valeur du message
        data = message.value
        print(f"Message reçu: {data}")  # Ajout d'une ligne de débogage
        # Ecrire chaque message en tant que ligne dans le fichier CSV
        writer.writerow([data['review_id'], data['review_text'], data['sentiment']])
        message_count += 1

    if message_count == 0:
        print("Aucun message n'a été consommé.")
    else:
        print(f"{message_count} messages ont été consommés et enregistrés dans le fichier CSV.")

# Lecture du fichier CSV avec pandas et affichage
try:
    df = pd.read_csv(output_csv_file)
    if df.empty:
        print("\nLe fichier CSV est vide.")
    else:
        print("\nLes données du CSV :")
        print(df)
except Exception as e:
    print(f"Erreur lors de la lecture du fichier CSV: {e}")
