import pandas as pd
from sqlalchemy import create_engine

# connexion PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:Buisson07!@localhost:5432/healthcare")

# chargement du CSV nettoyé
df = pd.read_csv("data_clean.csv")
df["date"] = pd.to_datetime(df["date"])

# insertion dans PostgreSQL
df.to_sql("hospitalisations", engine, if_exists="replace", index=False)
print(f"{len(df)} lignes insérées dans la table 'hospitalisations'.")
