import pandas as pd
from sklearn.preprocessing import LabelEncoder
file_path = "C:/Drivers/MANIKANDAN/STUDIES/LAB4.csv"  
df = pd.read_csv(file_path)
categorical_cols = ['team', 'opponent']
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])  
output_file = "C:/Drivers/MANIKANDAN/STUDIES/LAB5.csv"  
df.to_csv(output_file, index=False)

print(f"Transformed dataset saved to: {output_file}")
