import pandas as pd
import joblib
import numpy as np

# 1. Cargar el modelo entrenado
model_path = "./models/xgboost_model.pkl"
rf_model = joblib.load(model_path)
print("Modelo Random Forest cargado correctamente.")

# 2. Crear un DataFrame para las fechas futuras
future_dates = ['2025-01-01', '2025-02-01', '2025-03-01']
future_df = pd.DataFrame({'Date': future_dates})

# 3. Convertir las fechas a timestamps
future_df['Timestamp'] = pd.to_datetime(future_df['Date']).astype('int64') // 10**9

# 4. Usar el modelo para predecir
predictions = rf_model.predict(future_df[['Timestamp']])

# 5. Mostrar las predicciones
for date, prediction in zip(future_dates, predictions):
    print(f"Predicción para {date}: {prediction:.2f}")