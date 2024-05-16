import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
from imblearn.over_sampling import SMOTE

def load_data(filepath):
    """Load data from a CSV file."""
    data = pd.read_csv(filepath)
    print("Columns in data:", data.columns)  # This will print the column names
    return data

def preprocess_data(data):
    """Preprocess the data: clean, encode, and scale."""
    # Drop rows with any missing values
    data.dropna(inplace=True)

    # Feature Engineering: Split 'Technologies' into multiple binary columns
    if 'Technologies' in data.columns:
        techs = data['Technologies'].str.get_dummies(sep=', ')
        data = pd.concat([data, techs], axis=1)
        data.drop('Technologies', axis=1, inplace=True)
    else:
        print("The 'Technologies' column is missing from the data.")
        return None

    # Define columns to be encoded and scaled
    categorical_features = ['Risk Level']
    numeric_features = ['Complexity', 'Duration (days)', 'Budget (TND)']

    # Create transformers for categorical and numeric features
    transformers = [
        ('cat', OneHotEncoder(), categorical_features),
        ('num', StandardScaler(), numeric_features)
    ]

    # Initialize ColumnTransformer but leave technology columns untouched
    preprocessor = ColumnTransformer(transformers=transformers, remainder='passthrough')

    # Fit and transform the data
    data_processed = preprocessor.fit_transform(data)
    all_features = preprocessor.get_feature_names_out()

    # Create a DataFrame from the processed features
    data_processed = pd.DataFrame(data_processed, columns=all_features, index=data.index)

    return data_processed

def balance_data(X, y):
   
    smote = SMOTE()
    X_balanced, y_balanced = smote.fit_resample(X, y)
    return X_balanced, y_balanced

def split_data(data_processed):
    """Split data into training and testing sets."""
    # Assume the last column is the target (this needs to be adjusted based on your dataset's target variable)
    X = data_processed.iloc[:, :-1]
    y = data_processed.iloc[:, -1]

    return train_test_split(X, y, test_size=0.2, random_state=42)

def main():
    # Load data
    data = load_data("C:/Users/MOHAMED/Desktop/Optimizing_Resources_Allocation/scripts/generated_project_data_with_hours.csv")

    # Preprocess data
    if data is not None:
        data_processed = preprocess_data(data)
        
    else:
        print("Data loading failed.")

if __name__ == '__main__':
    main()
