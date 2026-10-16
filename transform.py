import pandas as pd
import io
import requests

# Rechargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
response = requests.get(url, timeout=30)
df = pd.read_csv(io.StringIO(response.text), sep=";", on_bad_lines="skip")

# Nettoyage
df["jour"] = pd.to_datetime(df["jour"])
df = df[df["sexe"] == 0]  # 0 = total (pas de filtre par sexe)
df = df.dropna(subset=["hosp", "rea", "dc"])

# Renommage des colonnes
df = df.rename(columns={
    "dep": "departement",
    "jour": "date",
    "hosp": "hospitalisations",
    "rea": "reanimations",
    "dc": "deces",
    "rad": "retours_domicile"
})

# Sélection des colonnes utiles
df = df[["departement", "date", "hospitalisations", "reanimations", "deces", "retours_domicile"]]

print(f"Données transformées : {df.shape[0]} lignes")
print(df.head(10))
print("\nStats globales :")
print(df[["hospitalisations", "reanimations", "deces"]].describe())

# Sauvegarde
df.to_csv("data_clean.csv", index=False)
print("\nFichier data_clean.csv sauvegardé.")