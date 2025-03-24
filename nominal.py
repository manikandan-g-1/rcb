import pandas as pd
data=pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\mani\OUT.csv")
def classify_attribute(df):
    nominal=[]
    numeric=[]
    for column in df.columns:
        if df[column].dtype =='object':
            nominal.append(column)
        else:
            numeric.append(column)
    return nominal,numeric
nominal_att,numeric_att=classify_attribute(data)
print("nominal Attribute",nominal_att)
print("numeric Attribute",numeric_att)
