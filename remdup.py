import pandas as pd
file_path="C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\ODI_3.csv"
data=pd.read_csv(file_path)
clean_data=data.dropna()
cleaned_path="C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\solution.csv"
clean_data.to_csv(cleaned_path,index=True)
print(cleaned_path)