import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

# URL de la Bolsa de Cereales o el sitio que quieras extraer datos
url = "https://www.bolsadecereales.com/datasets/"

# Hacemos la petición y obtenemos el HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraemos las tablas que contienen los precios de los granos
tables = soup.find_all('table', class_='some-class')  # Cambia 'some-class' por la clase real

# Almacenaremos los datos en una lista
data = []

# Recorrer cada tabla para extraer filas
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 1:
            fecha = cols[0].text.strip()   # Fecha
            tipo_grano = cols[1].text.strip()  # Tipo de grano
            precio = cols[2].text.strip()    # Precio
            
            # Convertir la fecha
            fecha_formateada = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')
            
            data.append({
                'fecha': fecha_formateada,
                'tipo_grano': tipo_grano,
                'precio': float(re.sub(',', '', precio))  # Limpiar precios si hay separadores de miles
            })

# Crear un DataFrame
df = pd.DataFrame(data)

# Guardar el dataset
df.to_csv("./data/raw/precios_granos.csv", index=False)
print("Datos extraídos y guardados correctamente.")