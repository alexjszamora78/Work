import pandas as pd

df = pd.read_csv('bike.csv')

#Imprime as primeras 5 filas:
print(df.head())

#Cálculo de la media de una columna numérica:
print(df['duration'].mean())

#Filtrado de filas según una condición:
df_filtered = df[df['workingday'] == 0]

#Guardado del DataFrame en un archivo JSON:
df_filtered.to_json('bike.json')