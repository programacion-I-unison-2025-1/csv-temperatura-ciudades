# Ejercicio: Análisis con archivos CSV - Temperatura


### 🎯 Objetivo
- Manipulación de DataFrames con Pandas.
- Creación y aplicación de funciones personalizadas (apply).
- Cálculo de estadísticas descriptivas (mínimo, máximo, promedio).
- Visualización de datos (Scatter plot).
- Exportación de datos a CSV.

### 📝 Descripción del Problema
El script carga un archivo CSV (data.csv) que contiene registros históricos de temperatura en grados Kelvin de tres ciudades distintas. El ejercicio consiste en convertir estas temperaturas a grados Celsius, analizar los datos de una ciudad específica (Phoenix), visualizar la variación de temperatura a lo largo del año y exportar los resultados a un nuevo archivo CSV.

## Instrucciones

Sigue los pasos a continuación para completar el ejercicio:

**1. Conversión de Unidades**

Crea una función llamada `kelvin_to_celsius` que acepte una temperatura en **Kelvin** y retorne su equivalente en **Celsius**.

$$C = K - 273.15$$

Posteriormente, aplica esta función a las columnas de las ciudades (San Diego, Phoenix, Toronto) y guarda los resultados en un nuevo DataFrame llamado `df_celsius`.

**2. Análisis de Datos (Phoenix)**

Utilizando el DataFrame transformado (`df_celsius`), calcula e imprime en consola los siguientes datos para la ciudad de Phoenix con su respectivo mensaje.  
**Nota:** redondea los resultados de temperatura a 2 decimales

1. ¿Qué día y a que hora se registró la temperatura minima en Phoenix durante 2016?
   ```
   El día con la temperatura minima en Phoenix fue: {fecha hora}
   ```

2. ¿Cuál fue la temperatura mínima registrada en Phoenix durante 2016?
   ```
   La temperatura minima registrada en Phoenix fue de: {temperatura} °C
   ```

3. ¿Qué día y a que hora se registró la temperatura maxima en Phoenix durante 2016?
   ```
   El día con la temperatura maxima en Phoenix fue: {fecha hora}
   ```

4. ¿Cuál fue la temperatura máxima registrada en Phoenix durante 2016?
   ```
   La temperatura maxima registrada en Phoenix fue de: {temperatura} °C
   ```

5. ⁠Temperatura promedio del año en Phoenix
   ```
   La temperatura promedio durante 2016 en Phoenix fue de: {temperatura} °C
   ```

**3. Visualización**

Genera un gráfico de dispersión (*scatter plot*) que muestre la variación de la temperatura en Phoenix a lo largo del año. El código base ya incluye la configuración para graficar la temperatura de Phoenix.
- Debes guardar la gráfica generada como un archivo de imagen llamado: `temperatura_phoenix_2016.png`.

**4. Exportación**

Finalmente, exporta el DataFrame con las temperaturas ya convertidas a Celsius a un nuevo archivo CSV llamado `data_celsius.csv`.

### 🛠️ Resumen

El archivo de código contiene comentarios marcados como `# TODO` donde debes implementar las soluciones para cada uno de los pasos descritos anteriormente. Asegúrate de seguir las instrucciones cuidadosamente y de probar tu código para verificar que funciona correctamente antes de finalizar el ejercicio.

---

## 📂 Estructura del Repositorio

```
.
├── README                        # Instrucciones de la tarea [No modificar]
├── data.csv                      # Dataset original (Temperaturas en Kelvin)
├── main.py                       # Archivo para ejecutar el programa
├── .gitignore                    # Archivo para ignorar archivos en Git [No modificar]
├── requirements.txt              # Archivo para dependencias [No modificar]
├── disparador_autoevaluacion.py  # Archivo de respaldo para disparar la autoevaluación [Modificar solo si es necesario]
```

## 🚀 Cómo ejecutar el proyecto en tu computadora

### 🛠️ Parte 1: Preparación del Entorno

1. **Instala Python**
   
   Si aún no lo tienes, necesitarás Python (versión 3.9 o más reciente).
   - Puedes descargarlo desde python.org.
   - Importante (en Windows): Durante la instalación, asegúrate de marcar la casilla que dice "Add Python to PATH".

2. **Descarga el código de la tarea**
   
   - Opción A (Recomendada): Clonar con Git (necesitas tener Git instalado).
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   ```

   - Opción B: Descargar el ZIP
     1. En la página del repositorio (GitHub, GitLab, etc.), busca un botón verde que dice "Code" o un botón de descarga.
     2. Elige "Download ZIP".
     3. Descomprime el archivo ZIP en una carpeta donde vayas a trabajar.

3. **Abre una Terminal en la carpeta de la tarea**
   
   - En Windows: Entra a la carpeta, haz clic derecho en un espacio vacío y selecciona "Abrir en Terminal" o "Abrir PowerShell aquí".
   - En macOS/Linux: Entra a la carpeta, haz clic derecho y busca una opción similar a "Abrir en Terminal".

4. **Crea y activa tu entorno virtual**
   
   Vamos a crear un "entorno virtual". Piensa en él como una caja separada donde instalaremos las herramientas solo para este proyecto, sin afectar el resto de tu computadora. Es una práctica estándar y muy importante.
   - Crea el entorno (esto crea una nueva carpeta llamada .env):
     ```
     python -m venv .env
     ```
   - Activa el entorno (tu terminal cambiará para mostrar (.env) al inicio):

     - En Windows:
       ```
       .env\Scripts\activate
       ```

     - En macOS/Linux:
       ```
       source .env/bin/activate
       ```
   *Nota*: Cada vez que cierres y vuelvas a abrir la terminal para trabajar en este proyecto, deberás repetir este paso de activación.

5. **Instala las dependencias**
   
   Las "dependencias" son paquetes de código adicionales (herramientas) que el proyecto necesita para funcionar. Con tu entorno virtual activado, ejecuta:

   ```
   pip install -r requirements.txt
   ```

### 🛠️ Parte 2: A trabajar

1. **Resuelve los `TODO`**
   
   Abre la carpeta del proyecto en tu editor de código (como VS Code). Busca los archivos .py y encuentra los comentarios que dicen TODO. ¡Ahí es donde debes escribir tu solución!

2. **Ejecuta el programa**
    
   Para ejecutar el programa y poder introducir datos manualmente, abre tu terminal en la carpeta del proyecto e introduce el siguiente comando:
   ```
   python main.py
   ```