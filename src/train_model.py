import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_data(filepath):
    """Cargar el dataset limpio."""
    return pd.read_csv(filepath)

if __name__ == "__main__":
    # Ruta al dataset limpio
    processed_data_path = "./data/processed/precios_granos_limpios.csv"

    try:
        # Cargar los datos
        data = load_data(processed_data_path)

        # Variables independientes (X) y dependiente (y)
        X = data[['fecha']].apply(lambda x: pd.to_datetime(x).astype('int64') // 10**9).values.reshape(-1, 1)
        y = data['precio'].values

        # Dividir datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Entrenar el modelo
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predicciones y evaluación
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Error cuadrático medio (MSE): {mse}")

    except Exception as e:
        print(f"Error al entrenar el modelo: {e}")