import joblib
import pandas as pd
import numpy as np

# Cargar el modelo entrenado
model = joblib.load('./models/fao_price_model.pkl')

# Crear nuevas fechas para predecir (como ejemplo)
new_dates = ['2025-01-01', '2025-02-01', '2025-03-01']  # Ajusta según tus necesidades
new_timestamps = pd.to_datetime(new_dates).view('int64') // 10**9
X_new = np.array(new_timestamps).reshape(-1, 1)

# Realizar predicciones
predictions = model.predict(X_new)

# Mostrar resultados
for date, price in zip(new_dates, predictions):
    print(f"Predicción para {date}: {price:.2f}")