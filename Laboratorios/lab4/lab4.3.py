
import pandas as pd

df_notas = pd.read_csv("notas_alumnos.csv")

df_notas_limpio = df_notas.dropna()  #elimina valores nulos

df_notas_limpio["Promedio"] = (df_notas_limpio["Parcial_1"] + df_notas_limpio["Parcial_2"]) / 2

print(df_notas_limpio)