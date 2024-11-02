from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialiser SparkSession avec le connecteur Kafka
spark = SparkSession.builder \
    .appName("KafkaDataProcessing") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .getOrCreate()

# Lire les données depuis Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "my-topic") \
    .load()

# Conversion des données Kafka en String
df = df.selectExpr("CAST(value AS STRING)")

# Définir le schéma des données JSON attendues (adapter selon vos données réelles)
schema = StructType([
    StructField("column1", StringType(), True),
    StructField("column2", IntegerType(), True),
    StructField("column3", StringType(), True)
])

# Convertir les données JSON en DataFrame structuré
json_df = df.withColumn("data", from_json(col("value"), schema)).select("data.*")

# Fonction pour afficher les données sur l'écran
def display_data(batch_df, batch_id):
    print(f"Batch ID: {batch_id}")
    batch_df.show(truncate=False)

# Utiliser foreachBatch pour afficher chaque batch des données Kafka
query = json_df.writeStream \
    .outputMode("append") \
    .foreachBatch(display_data) \
    .start()

# Attendre la fin du streaming
query.awaitTermination()
