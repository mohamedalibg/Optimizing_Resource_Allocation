import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

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

    # Create additional features (e.g., total number of technologies used)
    data['num_technologies'] = techs.sum(axis=1)

    # Define columns to be encoded and scaled
    categorical_features = ['Risk Level']
    numeric_features = ['Complexity', 'Duration (days)', 'Budget (TND)', 'num_technologies'] + list(techs.columns)

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

def split_data(data_processed):
    """Split data into training and testing sets."""
    X = data_processed.drop(['cat__Risk Level_High', 'cat__Risk Level_Medium', 'cat__Risk Level_Low'], axis=1)
    y = data_processed[['cat__Risk Level_High', 'cat__Risk Level_Medium', 'cat__Risk Level_Low']]

    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    """Train and evaluate different models with hyperparameter tuning."""

    # Define models and parameters
    models = {
        'RandomForest': RandomForestClassifier(),
        'GradientBoosting': GradientBoostingClassifier(),
        'XGBoost': XGBClassifier()
    }

    params = {
        'RandomForest': {
            'n_estimators': [100, 200],
            'max_depth': [10, 20],
            'min_samples_split': [2, 5]
        },
        'GradientBoosting': {
            'n_estimators': [100, 200],
            'learning_rate': [0.01, 0.1],
            'max_depth': [3, 5]
        },
        'XGBoost': {
            'n_estimators': [100, 200],
            'learning_rate': [0.01, 0.1],
            'max_depth': [3, 5]
        }
    }

    best_models = {}
    for model_name, model in models.items():
        grid_search = GridSearchCV(model, params[model_name], cv=3, scoring='f1_weighted', n_jobs=-1)
        grid_search.fit(X_train, y_train)
        best_models[model_name] = grid_search.best_estimator_
        print(f"Best parameters for {model_name}: {grid_search.best_params_}")
    
    # Evaluate the best model
    for model_name, model in best_models.items():
        y_pred = model.predict(X_test)
        print(f"Classification report for {model_name}:")
        print(classification_report(y_test, y_pred))

def main():
    # Load data
    data = load_data("C:/Users/MOHAMED/Desktop/Optimizing_Resources_Allocation/scripts/generated_project_data_with_hours.csv")

    # Preprocess data
    if data is not None:
        data_processed = preprocess_data(data)
        if data_processed is not None:
            data_processed.to_csv("C:/Users/MOHAMED/Desktop/Optimizing_Resources_Allocation/scripts/processed_data.csv", index=False)

            # Split data
            X_train, X_test, y_train, y_test = split_data(data_processed)

            # Train and evaluate models
            train_and_evaluate_model(X_train, X_test, y_train, y_test)
        else:
            print("Data preprocessing failed due to missing necessary columns.")
    else:
        print("Data loading failed.")

if __name__ == '__main__':
    main()
