import requests
import pandas as pd
import io

# Données hospitalières COVID - data.gouv.fr (fichier stable et connu)
url = "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"

print("Téléchargement des données...")
response = requests.get(url, timeout=30)
print(f"Statut HTTP : {response.status_code}")

# Lecture directe depuis la réponse
df = pd.read_csv(io.StringIO(response.text), sep=";", on_bad_lines="skip")
print(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
print(df.columns.tolist())
print(df.head())