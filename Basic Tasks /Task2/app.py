import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
# Load data
data = pd.read_csv('user_data.csv')

# Display the first few rows of the data
print(data.head())

# Example structure of data
# data = pd.DataFrame({
#     'age': [23, 45, 34, 50, 28],
#     'gender': ['F', 'M', 'M', 'F', 'F'],
#     'page_views': [100, 150, 120, 180, 90],
#     'time_spent': [20, 45, 35, 60, 25],
#     'behavior': [0, 1, 0, 1, 0]  # 0: Not Interested, 1: Interested
# })

# Convert categorical variables to numerical
data['gender'] = pd.get_dummies(data['gender'], drop_first=True)

# Define features and target variable
X = data[['age', 'gender', 'page_views', 'time_spent']]
y = data['behavior']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

print('Classification Report:')
print(classification_report(y_test, y_pred))

# Feature Importances
features = X.columns
importances = model.feature_importances_

# Create a DataFrame for visualization
feature_importance_df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df)
plt.title('Feature Importances')
plt.show()

import joblib

# Save the model
joblib.dump(model, 'user_behavior_model.pkl')

# Load the model
loaded_model = joblib.load('user_behavior_model.pkl')
