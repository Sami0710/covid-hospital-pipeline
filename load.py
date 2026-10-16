import pandas as pd
from sqlalchemy import create_engine

# Connexion PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:Buisson07!@localhost:5432/healthcare")

# Chargement du CSV nettoyé
df = pd.read_csv("data_clean.csv")
df["date"] = pd.to_datetime(df["date"])

# Insertion dans PostgreSQL
df.to_sql("hospitalisations", engine, if_exists="replace", index=False)
print(f"{len(df)} lignes insérées dans la table 'hospitalisations'.")