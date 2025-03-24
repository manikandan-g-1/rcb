import pandas as pd
odi1=pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\ODI_1.csv")
odi2=pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\ODI_2.csv")
odi_unique=odi2[['strike_rate','team','minutes','opponent']].drop_duplicates(subset=['strike_rate'])
merge_data=pd.merge(odi1,odi_unique,on='strike_rate',how='left')
merge_data.to_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\ODI_3.csv",index=False)
print('merged data')