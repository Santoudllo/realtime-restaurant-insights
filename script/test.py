from pymongo import MongoClient

mongodb_uri = "mongodb+srv://alimousantou:c2U16agfAPFf8cqH@ailab.wku4a.mongodb.net/?retryWrites=true&w=majority"
db_name = "restaurantInsightsDB"

try:
    client = MongoClient(mongodb_uri)
    db = client[db_name]
    # Vérifiez si la connexion est réussie
    client.admin.command('ping')
    print("Connexion réussie à MongoDB !")
except Exception as e:
    print(f"Erreur lors de la connexion à MongoDB : {e}")
finally:
    client.close()
