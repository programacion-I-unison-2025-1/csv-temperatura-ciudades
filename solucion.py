import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    # celsius = int(celsius)
    return celsius
    

# Copiar el DataFrame original para mantener los datos sin modificar
df_celsius = df.copy()

# Convertir la columna San Diego, Phoenix y Toronto de Kelvin a Celsius
df_celsius['San Diego'] = df_celsius['San Diego'].apply(kelvin_to_celsius)
df_celsius['Phoenix'] = df_celsius['Phoenix'].apply(kelvin_to_celsius)
df_celsius['Toronto'] = df_celsius['Toronto'].apply(kelvin_to_celsius)


# Analisis

# 1. ¿Qué día y a que hora se registró la temperatura minima en Phoenix durante 2016?
date_min_temp = df_celsius['Phoenix'].idxmin()
print("El día con la temperatura minima en Phoenix fue:", date_min_temp)

# 2. ¿Cuál fue la temperatura mínima registrada en Phoenix durante 2016?
min_temp_phoenix = df_celsius['Phoenix'].min()
min_temp_phoenix = min_temp_phoenix.round(2)
print("La temperatura minima registrada en Phoenix fue de:", min_temp_phoenix, "°C")

# 3. ¿Qué día y a que hora se registró la temperatura maxima en Phoenix durante 2016?
date_max_temp = df_celsius['Phoenix'].idxmax()
print("El día con la temperatura maxima en Phoenix fue:", date_max_temp)

# 4. ¿Cuál fue la temperatura máxima registrada en Phoenix durante 2016?
max_temp_phoenix = df_celsius['Phoenix'].max()
max_temp_phoenix = max_temp_phoenix.round(2)
print("La temperatura maxima registrada en Phoenix fue de:", max_temp_phoenix, "°C")

# 5. ⁠Temperatura promedio del año en Phoenix
avg_temp_phoenix = df_celsius['Phoenix'].mean()
avg_temp_phoenix = avg_temp_phoenix.round(2)
print("La temperatura promedio durante 2016 en Phoenix fue de:", avg_temp_phoenix, "°C")

# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")


