import pandas as pd
import joblib
from sklearn.calibration import LabelEncoder

# Load the trained Random Forest model
rf_model = joblib.load('trained_rf_model.pkl')

# Load the column order of the training data
model_columns = joblib.load('model_columns.pkl')

# Gather user input (replace these values with actual user input)
user_input = {
    'entreprise_id': 102,
    'industrie': 'fabrication',
    'chiffre_affaires': 45000000,
    'dépenses': 30000000,
    'employés': 2800,
    'catégorie_d\'actifs': 'Non-Amortissable',
    'valeur_d\'actifs': 2200000,
    'âge_d\'actifs': 10,
    'imposition_supplémentaire_évaluée': 100000,
    'créances_irrécouvrables': 0,
}

# Convert user input into a DataFrame
user_df = pd.DataFrame(user_input, index=[0])

# Preprocess user input
# One-hot encode categorical features
user_df = pd.get_dummies(user_df, columns=['industrie', 'catégorie_d\'actifs'])

# add missing categorical feature columns if any (the model may expect some features that the user didn't provide)

for col in model_columns:
    if col not in user_df.columns:
        user_df[col] = 0

# Reorder user input columns to match the model's expected column order
user_df = user_df[model_columns]

# Predict using the trained model
user_prediction = rf_model.predict(user_df)

# Display the prediction result
if user_prediction[0] == 0:
    print("No tax problem is predicted for the company.")
else:
    print("A tax problem is predicted for the company.")
