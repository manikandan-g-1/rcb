import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

def load_and_process_data(file_path, target_column):
    df = pd.read_csv(r"C:\Drivers\MANIKANDAN\STUDIES\LAB4.csv")
    
    # Handling missing values
    df = df.dropna()
    
    # Encoding categorical features
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    
    # Splitting features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Standardizing numerical features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y

def train_decision_tree(X, y):
    # Splitting dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Training Decision Tree
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    # Plot Decision Tree
    plt.figure(figsize=(15, 10))
    plot_tree(model, filled=True, feature_names=[str(i) for i in range(X.shape[1])], class_names=np.unique(y).astype(str))
    plt.show()
    
    return model, accuracy, report

# Example usage
file_path = "your_dataset.csv"
target_column = "100"
X, y = load_and_process_data(file_path, target_column)
model, accuracy, report = train_decision_tree(X, y)
print(f"Accuracy: {accuracy}\n{report}")
