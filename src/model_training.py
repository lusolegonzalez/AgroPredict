import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(data_path):
    # Cargar datos procesados
    data = pd.read_csv(data_path)

    # Preparar variables
    data['year'] = pd.to_datetime(data['fecha']).dt.year
    data['month'] = pd.to_datetime(data['fecha']).dt.month
    X = data[['tipo_grano', 'year', 'month']]
    y = data['precio']

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar modelo
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluar modelo
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    return model

if __name__ == "__main__":
    model = train_model("../data/processed/precios_granos_limpios.csv")