import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_clean.csv")
df["date"] = pd.to_datetime(df["date"])

# total hospitalisations par jour (tout départements)
daily = df.groupby("date")["hospitalisations"].sum()

plt.figure(figsize=(14, 6))
plt.plot(daily.index, daily.values, color="#0070AD", linewidth=1.5)
plt.title("Hospitalisations COVID en France par jour", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Nombre de patients hospitalisés")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("hospitalisations.png", dpi=150)
plt.show()
print("Graphique sauvegardé")