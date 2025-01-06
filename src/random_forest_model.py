import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Cargar el dataset preprocesado
df_fao_cleaned = pd.read_csv("./data/cleaned/cleaned_fao_food_price_indices.csv")

# Convertir fechas a timestamp para usar como característica
df_fao_cleaned['Timestamp'] = pd.to_datetime(df_fao_cleaned['Date']).astype('int64') // 10**9

# Definir variables independientes y dependientes
X = df_fao_cleaned[['Timestamp']]
y = df_fao_cleaned['Food Price Index']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = rf_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R²): {r2}")

# Guardar el modelo
joblib.dump(rf_model, "./models/random_forest_model.pkl")