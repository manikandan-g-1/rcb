import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\OUT.csv"
df = pd.read_csv(file_path)
features = ["Runs", "Inns", "Ave", "strike_rate", "100", "50"]
df_selected = df[features]
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_selected)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(df_scaled)
print(df[["Player", "Runs", "Inns", "Ave", "strike_rate", "100", "50", "Cluster"]].head())
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["Runs"], y=df["Ave"], hue=df["Cluster"], palette="viridis")
plt.xlabel("Total Runs")
plt.ylabel("Batting Average")
plt.title("K-Means Clustering of Players")
plt.legend(title="Cluster")
plt.show()