from sklearn.model_selection import train_test_split
import pandas as pd
lab4_file_path = r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\lab4.csv"
df_lab4 = pd.read_csv(lab4_file_path)
train_df, test_df = train_test_split(df_lab4, test_size=0.2, random_state=42)
train_file_path = r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\lab4_train.csv"
test_file_path = r"C:\Drivers\MANIKANDAN\STUDIES\SEM 6\Data Warhouse\data\lab4_test.csv"
train_df.to_csv(train_file_path, index=False)
test_df.to_csv(test_file_path, index=False)
print(f"Training Set: {train_df.shape[0]} rows")
print(f"Testing Set: {test_df.shape[0]} rows")
