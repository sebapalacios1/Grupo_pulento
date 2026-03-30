import random
import time
import numpy as np

cantidad = 5000000

datos = [random.random() for _ in range(cantidad)]

arreglo = np.array(datos)

inicio_python = time.time()
resultado_python = [valor**2 for valor in datos]
fin_python = time.time()
duracion_python = fin_python - inicio_python

inicio_numpy = time.time()
resultado_numpy = arreglo ** 2
fin_numpy = time.time()
duracion_numpy = fin_numpy - inicio_numpy

print(f"Tiempo usando Python: {duracion_python:.4f} segundos")
print(f"Tiempo usando NumPy: {duracion_numpy:.6f} segundos")

if duracion_numpy > 0:
    veces_mas_rapido = duracion_python / duracion_numpy
    print(f"NumPy fue aproximadamente {veces_mas_rapido:.2f} veces más rápido.")
