import pandas as pd
data=pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\OUT.csv")
sample_data=data[["strike_rate","Runs"]].sample(n=10,random_state=42)
print(sample_data)