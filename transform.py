import pandas as pd
import io
import requests

# rechargement des données
url = "https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
response = requests.get(url, timeout=30)
df = pd.read_csv(io.StringIO(response.text), sep=";", on_bad_lines="skip")

# nettoyage
df["jour"] = pd.to_datetime(df["jour"])
df = df[df["sexe"] == 0]  # 0 = total (pas de filtre par sexe)
df = df.dropna(subset=["hosp", "rea", "dc"])

# renommage des colonnes
df = df.rename(columns={
    "dep": "departement",
    "jour": "date",
    "hosp": "hospitalisations",
    "rea": "rea",
    "dc": "deces",
    "rad": "retour_domicile"
})

# sélection des colonnes utiles
df = df[["departement", "date", "hospitalisations", "rea", "deces", "retours_domicile"]]

print(f"Données transformées : {df.shape[0]} lignes")
print(df.head(10))
print("\nStats globales :")
print(df[["hospitalisations", "rea", "deces"]].describe())

# sauvegarde
df.to_csv("data_clean.csv", index=False)
print("\nFichier data_clean.csv sauvegardé.")
