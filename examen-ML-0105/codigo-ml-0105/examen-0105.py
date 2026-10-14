
import sys
import os
import pandas as pd
import io
 # Iker Montoya

# Iker Montoya 0105
print("Eliseo Nava Machine Learning pandas, NC 0105")

# Diccionario de datos de granjas
datos_granjas = {
    "Granja": ["El Porvenir", "La Esperanza", "San José", "Los Pinos", "El Rosario", "Santa María"],
    "Hectareas": [50, 80, 35, 120, 65, 45],
    "Animales": [500, 800, 300, 1200, 600, 400]
}

# Variable para guardar los resultados en Markdown
contenido_md = []
encabezado_pie = "Eliseo Nava Machine Learning pandas, NC 0105"
contenido_md.append(f"# Reporte de Análisis de Granjas - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado y lo guarda en Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(datos_granjas)
registrar("1. DataFrame Convertido", df)

# 2. Información estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# 2.5 Información general
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas de hectáreas
registrar("3. Estadísticas de Hectáreas", df["Hectareas"].describe())

# 4. Ordenar ascendente por hectáreas
df_asc_hectareas = df.sort_values(by="Hectareas", ascending=True)
registrar("4. Orden Ascendente por Hectáreas", df_asc_hectareas)

# 5. Ordenar descendente por animales
df_desc_animales = df.sort_values(by="Animales", ascending=False)
registrar("5. Orden Descendente por Animales", df_desc_animales)

# 6. Estadísticas de animales
registrar("6. Estadísticas de Animales", df["Animales"].describe())

# 7. Guardar el reporte en la carpeta de resultados
carpeta_resultados = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "resultados-0105"
)
os.makedirs(carpeta_resultados, exist_ok=True)

ruta_archivo_md = os.path.join(
    carpeta_resultados,
    "resultados-granjas-0105.md"
)

contenido_md.append(f"\n`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Iker Montoya Machine Learning pandas, NC 0105")

