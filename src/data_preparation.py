import pandas as pd
import os

def load_data(filepath):
    """Cargar dataset desde un archivo CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo no existe: {filepath}")
    return pd.read_csv(filepath)

def clean_data(df):
    """Limpiar y preparar el dataset."""
    # Convertir la columna de fecha a tipo datetime
    if 'fecha' in df.columns:
        df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')

    # Eliminar filas con valores nulos
    df = df.dropna()

    # Opcional: Eliminar duplicados
    df = df.drop_duplicates()

    # Asegurar que los datos estén ordenados por fecha
    if 'fecha' in df.columns:
        df = df.sort_values(by='fecha')

    return df

if __name__ == "__main__":
    # Ruta del dataset crudo
    raw_data_path = "./data/raw/precios_granos.csv"
    processed_data_path = "./data/processed/precios_granos_limpios.csv"

    # Cargar y limpiar los datos
    try:
        data = load_data(raw_data_path)
        print("Datos cargados con éxito.")
        clean_data = clean_data(data)
        clean_data.to_csv(processed_data_path, index=False)
        print(f"Datos procesados y guardados en {processed_data_path}")
    except Exception as e:
        print(f"Error durante la preparación de los datos: {e}")