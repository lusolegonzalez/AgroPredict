import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Cargar el dataset limpio
df_fao_cleaned = pd.read_csv('./data/cleaned/cleaned_fao_food_price_indices.csv')

# Convertir la columna de fechas a timestamps
df_fao_cleaned['Timestamp'] = pd.to_datetime(df_fao_cleaned['Date']).astype('int64') // 10**9

# Preparar los datos de entrenamiento y prueba
X = df_fao_cleaned[['Timestamp']].values  # Fecha como característica
y = df_fao_cleaned['Food Price Index'].values  # Índice de precios como objetivo

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Imprimir métricas
print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación (R²): {r2}")

# Guardar el modelo entrenado (opcional)
import joblib
joblib.dump(model, './models/fao_price_model.pkl')