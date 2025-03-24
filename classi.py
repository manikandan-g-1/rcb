import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = r"C:\Drivers\MANIKANDAN\STUDIES\LAB4.csv"  
df = pd.read_csv(file_path)

# Selecting relevant features and target variable
features = ["Mat", "Inns", "NO", "Runs", "BF", "strike_rate", "50", "minutes"]
target = "100"  # Column representing centuries

# Encoding non-numeric values (if any)
df_encoded = df.copy()
label_encoders = {}
for col in df_encoded.columns:
    if df_encoded[col].dtype == 'object':
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])
        label_encoders[col] = le

# Convert the "100" column to binary classification (1 if century scored, 0 otherwise)
df_encoded[target] = (df_encoded[target] > 0).astype(int)

# Splitting data into training and testing sets
X = df_encoded[features]
y = df_encoded[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Creating and training the Random Forest model
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=42)
rf_clf.fit(X_train, y_train)

# Model evaluation
y_pred = rf_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --- 1️⃣ Decision Tree from Random Forest (Visualizing One Tree) ---
plt.figure(figsize=(21, 7))
plot_tree(rf_clf.estimators_[0], feature_names=features, class_names=["No Century", "Century"], filled=True, rounded=True)
plt.title("Single Decision Tree from Random Forest")
plt.show()

