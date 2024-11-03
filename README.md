# Projet Intégré : Évaluation de la Qualité et de la Perception des Restaurants

## Technologies Utilisées

### Langage

![Python](https://img.shields.io/badge/Python-3.10.12-blue?logo=python&logoColor=white)

### Frameworks et Outils de Développement

![Confluent Kafka](https://img.shields.io/badge/Confluent%20Kafka-3.2.0-yellow?logo=apachekafka&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.3.1-red?logo=apachespark&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-20.10.7-blue?logo=docker&logoColor=white)

### Cloud & Bases de Données

![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.15.0-blue?logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-8.15.0-orange?logo=kibana&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green?logo=mongodb&logoColor=white)

### Analyse des Sentiments & Intelligence Artificielle

![OpenAI API](https://img.shields.io/badge/OpenAI%20API-3.5-green?logo=openai&logoColor=white)

### Bibliothèques de Données & Machine Learning

![Pandas](https://img.shields.io/badge/Pandas-1.5.2-brightgreen?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.21.0-blue?logo=numpy&logoColor=white)

### Outils de Visualisation

![Kibana](https://img.shields.io/badge/Kibana-8.15.0-orange?logo=kibana&logoColor=white)

### Conteneurisation et Déploiement

![Docker](https://img.shields.io/badge/Docker-20.10.7-blue?logo=docker&logoColor=white)

### Outils de Débogage et de Terminal

![IPython](https://img.shields.io/badge/IPython-8.0.0-blue?logo=ipython&logoColor=white)

---
Ces outils ont été utilisés pour le développement du projet Realtime Restaurant Insights, visant à ingérer, transformer, et analyser des données en temps réel pour obtenir des insights sur les avis clients de différents restaurants. Le traitement des données en temps réel est facilité par Kafka, tandis que l'analyse des sentiments est effectuée grâce à l'API d'OpenAI, et les données sont ensuite indexées et visualisées à l'aide d'Elasticsearch et Kibana.


## Objectif du Projet
Ce projet vise à combiner les données de conformité sanitaire fournies par l'API **Alim'confiance** avec l'analyse des sentiments des **avis clients** pour offrir une vue d'ensemble de la qualité des établissements de restauration. Cette approche permettrait d'identifier des corrélations entre les évaluations sanitaires officielles et la perception des consommateurs, offrant ainsi une vision complète pour améliorer la sécurité et la satisfaction client.

## 🎭 Mes cibles

Mes cibles principales incluent :

- **Restaurateurs et Propriétaires de Restaurants** qui souhaitent surveiller les avis des clients en temps réel pour améliorer la satisfaction client et la qualité du service.

- **Gestionnaires de Chaînes de Restaurants** pour obtenir une vue d'ensemble des performances des établissements sur différents sites et agir rapidement sur les retours négatifs.

- **Services Marketing** qui souhaitent personnaliser leurs campagnes en fonction des retours clients et cibler plus efficacement les publics.

- **Plateformes de Critiques et de Réservations** qui souhaitent offrir une meilleure expérience utilisateur en filtrant et analysant les retours clients de manière plus précise.

- **Consultants en Restauration** qui peuvent utiliser ces insights pour conseiller leurs clients sur l'amélioration de la qualité des services.

- **Fournisseurs de Services de Livraison de Repas** qui souhaitent optimiser leur offre en fonction des avis clients sur les restaurants partenaires.

- **Analystes de Données et Chercheurs** qui souhaitent étudier les tendances de consommation et les préférences des clients en matière de restauration.



## Architecture du Projet


![alt text](image.png)

### Workflow et Schéma d'Architecture

1. **Ingestion des Données de Contrôles Sanitaires (API Alim'confiance)** :
   - Extraction des informations sur les établissements et leurs contrôles sanitaires via l'API Alim'confiance, envoi des données dans Kafka.

2. **Ingestion des Avis Clients** :
   - Extraction d'avis clients à partir de sources disponibles (plateformes d'avis ou réseaux sociaux, dans le respect des règles d'utilisation).
   - Envoi des avis dans Kafka pour une ingestion en flux continu.

3. **Traitement des Données** :
   - **Analyse des Sentiments** : Utilisation de l'API OpenAI pour identifier le sentiment général (positif, neutre, négatif) et les sentiments par aspect (qualité de la nourriture, service, ambiance).
   - **Transformation des Données** : Spark nettoie et enrichit les données, en ajoutant des informations telles que la date, la région, le département et le type d’établissement.

4. **Indexation et Stockage** :
   - Les données enrichies sont stockées dans Elasticsearch, indexées par établissement, par date, par région, et par catégorie (avis clients et contrôles sanitaires).

5. **Visualisation et Analyse** :
   - Kibana est utilisé pour créer des tableaux de bord interactifs, permettant de suivre la conformité sanitaire et l’expérience client en temps réel.

## Fonctionnalités du Projet

1. **Suivi des Contrôles Sanitaires**
   - **Objectif** : Fournir une vue d’ensemble des niveaux d’hygiène pour chaque établissement.
   - **Description** : Identifier les établissements avec des niveaux "à corriger de manière urgente" ou "à améliorer" pour cibler les interventions nécessaires.

2. **Analyse des Sentiments des Avis Clients**
   - **Objectif** : Quantifier le sentiment des clients pour chaque établissement en fonction de l'expérience (service, nourriture, ambiance).
   - **Description** : Évaluer les avis clients pour chaque aspect du service, afin d'identifier des tendances et des aspects nécessitant une amélioration.

3. **Corrélation entre Sentiment Client et Hygiène Sanitaire**
   - **Objectif** : Identifier les corrélations entre la satisfaction des clients et le niveau de conformité sanitaire.
   - **Description** : Analyser si les établissements avec de meilleures pratiques sanitaires obtiennent des avis plus positifs, ou si un mauvais niveau d'hygiène entraîne une perception négative dans les avis.

4. **Analyse Géographique et Temporelle**
   - **Objectif** : Identifier les zones géographiques avec des tendances sanitaires ou de satisfaction particulières, ainsi que l’évolution de la perception des établissements au fil du temps.
   - **Description** : Créer des cartes géographiques dans Kibana pour visualiser les établissements à risque et les sentiments des clients par région.

5. **Rapports et Indicateurs de Qualité**
   - **Objectif** : Créer des rapports consolidés sur la qualité globale des établissements et générer des indicateurs (ex. score de conformité, score de satisfaction).
   - **Description** : Agréger les scores de conformité et de satisfaction pour chaque établissement pour créer un tableau de classement des restaurants.

## Déroulement Technique du Projet

### **Étapes d'installation :**

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Santoudllo/realtime-restaurant-insights.git
  cd realtime-restaurant-insights
   ```

2. **Créer un environnement virtuel :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   # Ou
   venv\Scripts\activate     # Windows
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement :**
   Créez un fichier `.env` et renseignez les informations de connexion MongoDB et Elasticsearch :
   ```env
MONGO_USERNAME="*****"
MONGO_PASSWORD="*******"
MONGO_DBNAME="*********"
MONGO_URI="************"
API_URL=https://dgal.opendatasoft.com/api/explore/v2.1/catalog/datasets/export_alimconfiance/records
OPENAI_API_KEY="********"
KAFKA_BROKER=localhost:9092
KAFKA_TOPIC="*******"
 ```

### Sous-Projet : Ingestion et Préparation des Données

Cette partie du projet est un sous-projet spécifique à l'ingestion et à la préparation des données, inclus dans notre projet global intitulé Évaluation de la Qualité et de la Perception des Restaurants. Deux pipelines Kedro ont été mis en place pour gérer ces données et les rendre disponibles pour l'analyse et la visualisation :

#### Pipeline ETL

Ce pipeline collecte les données brutes à partir de l'API Alim'confiance, les transforme via des étapes de nettoyage et d'enrichissement, puis les stocke dans une base de données MongoDB. Le stockage dans MongoDB permet de centraliser les données transformées pour une utilisation ultérieure, facilitant ainsi les opérations d'analyse et de visualisation.

![alt text](image-4.png)

### **Exécuter localement :**
- **Exécuter tous les pipelines :**
   ```bash
   kedro run
   ```

#### Pipeline d'Ingestion des Avis Clients

Ce pipeline charge les données à partir de Spark, les fusionne pour créer un ensemble de données cohérent, puis les stocke dans Elasticsearch. Le stockage dans Elasticsearch facilite l'indexation des données et leur visualisation ultérieure, en offrant une recherche rapide et efficace pour l'évaluation des avis clients.






### Extraction et Ingestion
   - **Données de l’API Alim'confiance** : Extraction des données sanitaires avec Python et envoi dans Kafka.
   - **Avis clients** : Extraction et validation de conformité des données d'avis, envoi dans Kafka.

### Traitement avec Spark
   - **Analyse des sentiments** : Utilisation de l'API OpenAI pour analyser les sentiments des avis clients.
   - **Enrichissement** : Ajout d'informations temporelles et géographiques aux données sanitaires et aux avis clients.

### Stockage et Indexation avec Elasticsearch
   - Stockage des données d’établissement, des niveaux d’hygiène et des avis clients dans Elasticsearch.

### Visualisation avec Kibana
   - Création de tableaux de bord pour :
     - Suivre la répartition des niveaux d’hygiène.
     - Visualiser les sentiments des clients.
     - Suivre les corrélations et les tendances.

## Analyses et Indicateurs Attendus

1. **Indice de Conformité et de Satisfaction** : Calculer un score global pour chaque établissement en fonction de la conformité sanitaire et des sentiments clients.
2. **Corrélations entre Hygiène et Sentiment** : Identifier si les établissements mal notés pour leur hygiène ont aussi des avis négatifs des clients.
3. **Zones à Risque** : Localiser les zones géographiques où les niveaux d'hygiène et les avis clients sont insatisfaisants.
4. **Tendances Temporelles** : Analyser l’évolution dans le temps des niveaux de satisfaction et des niveaux d’hygiène.

## Exemples de Cas d'Usage

- **Pour les autorités** : Prioriser les contrôles dans les zones ou établissements avec des niveaux d'hygiène et de satisfaction faible.
- **Pour les restaurateurs** : Identifier les aspects (hygiène ou service) à améliorer pour répondre aux attentes des clients.
- **Pour les analystes** : Suivre les tendances régionales en matière de conformité sanitaire et de satisfaction client.

## Déploiement

- **Docker** : Conteneurisation des services (Kafka, Spark, Elasticsearch, Kibana) pour simplifier le déploiement et le scaling.
- **Configurations** : Variables d’API et paramètres de stockage configurables via des fichiers `.env`.
- **Automatisation** : Script de déploiement pour exécuter le pipeline complet.

##  📜 Conclusion <a name="conclusion"></a>

L'application Realtime Restaurant Insights s'est avérée être un atout considérable pour les acteurs de la restauration cherchant à comprendre et à exploiter les retours clients en temps réel. Grâce à l'intégration harmonieuse d'outils tels que Kafka pour l’ingestion de données en temps réel, Apache Spark pour le traitement, et Elasticsearch et Kibana pour l’indexation et la visualisation, l'application permet une exploitation rapide et efficace des données critiques.

Cette solution offre aux restaurateurs une capacité inédite de suivre la satisfaction client, d’identifier les problématiques de manière proactive, et de mettre en œuvre des actions correctives immédiates. Les gestionnaires de chaînes peuvent obtenir une vue d’ensemble de leurs multiples établissements, facilitant une gestion centralisée tout en gardant un œil sur chaque restaurant. Cette vision consolidée améliore non seulement la qualité du service, mais permet aussi une prise de décision fondée sur des informations vérifiées et actuelles.

En utilisant l’API d’OpenAI pour analyser les sentiments des avis clients, l'application est capable de transformer de simples commentaires en indicateurs concrets, fournissant des insights sur les aspects positifs et négatifs du service et des produits. Cela aide non seulement à rehausser l'expérience client, mais permet également aux équipes marketing d’orienter leurs stratégies de manière plus personnalisée et pertinente.

Les fonctionnalités de visualisation des données, avec Kibana, apportent une dimension interactive qui permet de transformer des volumes importants de données en tableaux de bord intuitifs. Ces visualisations permettent aux utilisateurs d'explorer les tendances, de suivre la satisfaction des clients en temps réel, et de prendre des décisions éclairées.

En somme, l’application "Realtime Restaurant Insights" se positionne comme un outil essentiel pour quiconque souhaite rester compétitif dans le secteur de la restauration. Elle aide à optimiser la satisfaction client, améliorer la qualité des services, et exploiter les retours clients de manière constructive. En mettant la donnée au centre de la prise de décision, cette solution représente une avancée majeure vers une gestion proactive et axée sur les résultats pour le secteur de la restauration.



🚧 Difficultés Rencontrées

- **Quota Limité pour l'API d'OpenAI** 
Une des principales difficultés rencontrées concernait l'utilisation de l'API d'OpenAI pour l'analyse des sentiments. L'accès à l'API est limité par un quota d'utilisation, ce qui a parfois restreint le traitement de grands volumes de données en temps réel. Ce quota a nécessité des ajustements dans la fréquence des appels API et une priorisation des avis clients à analyser, surtout en période de forte activité. En conséquence, une stratégie de gestion de quota a dû être mise en place, impliquant notamment la mise en cache des résultats et l'utilisation sélective de l'API pour les avis les plus pertinents.

![alt text](image-1.png)

## Améliorations Futures

1. **Machine Learning pour la prédiction des niveaux de conformité** : Utilisation de modèles pour anticiper les besoins d'inspection.
2. **Intégration d'autres sources d'avis (réseaux sociaux)** : Agrégation d'avis de sources variées pour enrichir les données.
3. **Développement d’une API** : Fournir un accès en temps réel aux indicateurs de qualité des établissements pour des applications externes.

---

##  📊 Docs <a name="documentation"></a>
j'ai documenté plusieurs étapes critiques du projet :

**Airflow**  est utilisé pour orchestrer les pipelines de collecte de données via des DAGs. Un exemple de DAG est utilisé pour envoyer nos données de MongoDB vers Kafka. Ce script Airflow s'exécute toutes les 8 heures. Voici une images du  DAG :

![alt text](image-3.png)

## Contributeurs

- Alimou DIALLO (@santoudllo): Data engineer -**alimousantou@gmail.com**


## Licence

Ce projet est sous licence MIT. N'hésitez pas à utiliser et modifier le code pour vos propres projets.