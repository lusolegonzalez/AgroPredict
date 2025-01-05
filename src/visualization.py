import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset limpio
file_path = './data/processed/cleaned_fao_food_price_indices.csv' 
df_fao_cleaned = pd.read_csv(file_path)

# Convertir la columna 'Date' a tipo datetime si es necesario
df_fao_cleaned['Date'] = pd.to_datetime(df_fao_cleaned['Date'], errors='coerce')

# Select key columns to plot trends
columns_to_plot = ['Food Price Index', 'Cereals', 'Meat', 
                   'Dairy', 'Sugar', 'Oils']

# Configure figure size
plt.figure(figsize=(14, 8))

# Plot each column of interest
for col in columns_to_plot:
    plt.plot(df_fao_cleaned['Date'], df_fao_cleaned[col], label=col)

# Add title, labels, and legend
plt.title('Tendencias de los precios de alimentos a lo largo del tiempo', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Índice de precios', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Show plot
plt.tight_layout()
plt.show()