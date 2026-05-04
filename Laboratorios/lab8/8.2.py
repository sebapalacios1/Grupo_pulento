import pandas as pd

# Datos que venían en la guía
datos = {
    "Componente": ["Arduino", "Resistencia 1k", "Capacitor", "Motor DC"],
    "Stock": [5, 500, 120, 3]
}

# Creamos la tabla (DataFrame)
df = pd.DataFrame(datos)

# Filtramos los que tengan menos de 10 unidades
df_critico = df[df["Stock"] < 10]

# Mostramos solo lo que falta reponer
print("--- Stock Crítico en Bodega ---")
print(df_critico)