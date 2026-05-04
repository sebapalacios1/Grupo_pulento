import numpy as np
import matplotlib.pyplot as plt

# Definimos el tiempo de 0 a 10 con 100 puntos como dice la pista
t = np.linspace(0, 10, 100)

# Sacamos el seno de t
y = np.sin(t)

# Empezamos a armar el gráfico
plt.plot(t, y, color='blue')
plt.title("Simulación de Sensor AC (Senoidal)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True) # para que se vea la malla de fondo

plt.show()