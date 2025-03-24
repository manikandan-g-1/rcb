import pandas as pd
from sklearn.preprocessing import MinMaxScaler ,LabelEncoder
data=pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\OUT.csv")
attribute="Player"
# data['runs_normalized']=train_test_split(data,test_size=0.4,stratify=data[attribute],random_state=42)
le=LabelEncoder()
data[attribute]=le.fit_transform(data[attribute])
scaler = MinMaxScaler()
data1= scaler.fit_transform(data[[attribute]])
print(data1)

# print(data['runs_normalized'].value_count(normalize=True))
# out="nor.csv"
# data.to_csv(out,index=False)
# print("Normalized data:",{out})