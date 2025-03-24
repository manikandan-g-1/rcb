import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\OUT.csv") 
top_players = df.nlargest(5, "Runs")  

plt.figure(figsize=(8, 5))
sns.barplot(x="Runs", y="Player", data=top_players, palette="viridis")
plt.xlabel("Total Runs")
plt.ylabel("Player")
plt.title("Top 5 Players with Highest Runs")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Runs"], y=df["strike_rate"], alpha=0.6, color="red")
plt.xlabel("Runs")
plt.ylabel("Strike Rate")
plt.title("Runs vs Strike Rate")
plt.grid(True)
plt.show()
