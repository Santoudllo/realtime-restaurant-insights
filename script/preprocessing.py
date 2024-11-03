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
    group_id=f'my-group-{uuid.uuid4()}',  
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=60000 
)


output_csv_file = '../kafka_messages.csv'  

with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['review_id', 'review_text', 'sentiment'])

    message_count = 0
    for message in consumer:
       
        data = message.value
        print(f"Message reçu: {data}")  
       
        writer.writerow([data['review_id'], data['review_text'], data['sentiment']])
        message_count += 1

    if message_count == 0:
        print("Aucun message n'a été consommé.")
    else:
        print(f"{message_count} messages ont été consommés et enregistrés dans le fichier CSV.")

try:
    df = pd.read_csv(output_csv_file)
    if df.empty:
        print("\nLe fichier CSV est vide.")
    else:
        print("\nLes données du CSV :")
        print(df)
except Exception as e:
    print(f"Erreur lors de la lecture du fichier CSV: {e}")
