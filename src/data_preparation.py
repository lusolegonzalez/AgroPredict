import pandas as pd

# Ruta del archivo subido por el usuario
file_path = './data/raw/fao_food_price_indices.csv'
processed_data_path = './data/cleaned/cleaned_fao_food_price_indices.csv'

# Cargar el dataset
df_fao = pd.read_csv(file_path)

# Mostrar las primeras filas y la información general para revisión
df_fao.head(), df_fao.info()

# Limpiar las columnas innecesarias y procesar filas útiles

# Renombrar columnas basándose en la primera fila y descartar las demás filas de metadatos
df_fao_cleaned = df_fao.rename(columns=df_fao.iloc[1]).drop([0, 1, 2])

# Eliminar columnas que son completamente nulas o irrelevantes
df_fao_cleaned = df_fao_cleaned.dropna(axis=1, how='all')

# Filtrar solo las filas que tienen datos en la columna de fecha (Date)
df_fao_cleaned = df_fao_cleaned[df_fao_cleaned['Date'].notnull()]

# Convertir la columna 'Date' en un formato de fecha reconocible
df_fao_cleaned['Date'] = pd.to_datetime(df_fao_cleaned['Date'], errors='coerce')

# Eliminar filas donde la fecha no se pudo convertir
df_fao_cleaned = df_fao_cleaned.dropna(subset=['Date'])

# Convertir el resto de las columnas numéricas al tipo adecuado (float)
for col in df_fao_cleaned.columns[1:]:  # Ignorar la columna de fecha
    df_fao_cleaned[col] = pd.to_numeric(df_fao_cleaned[col], errors='coerce')

# Mostrar una vista previa de los datos limpiados
df_fao_cleaned.head(), df_fao_cleaned.info()

df_fao_cleaned.to_csv(processed_data_path, index=False)
print(f"Datos procesados y guardados en {processed_data_path}")