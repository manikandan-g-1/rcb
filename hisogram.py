import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\OUT.csv")
plt.figure(figsize=(8,5))
plt.hist(df["Runs"],bins=20,color='blue',edgecolor='black')
plt.xlabel("runs")
plt.ylabel("players")
plt.title("runs scored by player")
plt.show()      