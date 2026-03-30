import random
import time
import numpy as np

valor = 100
lista1= [[random.random() for _ in range(valor)] for _ in range(valor)]
lista2 = [[random.random() for _ in range(valor)] for _ in range(valor)]

lista1_np = np.array(lista1)
lista2_np = np.array(lista2)

tiempo_python1 = time.time()
anidado = [[0 for _ in range(valor)] for _ in range(valor)]
for i in range(valor):
    for a in range(valor):
        for t in range(valor):
            anidado[i][a] += lista1[i][t] * lista2[t][a]
tiempo_python2 = time.time()
tiempo_pythonfinal = tiempo_python2 - tiempo_python1

tiempo_numpy1 = time.time()
multi = np.dot(lista1_np, lista2_np)
tiempo_numpy2 = time.time()
tiempo_numpyfinal = tiempo_numpy2 - tiempo_numpy1

# 5. Imprimir resultados y comparación
print(f"Tiempo de ejecución Python clásico: {tiempo_pythonfinal:.4f} segundos")
print(f"Tiempo de ejecución NumPy: {tiempo_numpyfinal:.6f} segundos")

if tiempo_numpyfinal > 0:
    print(f"NumPy fue {tiempo_pythonfinal / tiempo_numpyfinal:.2f} veces más rápido.")


