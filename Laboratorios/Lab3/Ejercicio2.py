# Ejercicio 2
import matplotlib.pyplot as plt

encuesta = {'Python' : 45, 'C++': 28, 'C': 15, 'Java': 12, 'Rust':8}

lenguajes_encuesta = [] 
datos_encuesta = [] 

for lenguaje, datos in encuesta.items():
    lenguajes_encuesta.append(lenguaje)
    datos_encuesta.append(datos)
  
# Seccion de graficos
plt.bar(lenguajes_encuesta[0], datos_encuesta[0], color='#2290F0')
plt.bar(lenguajes_encuesta[1], datos_encuesta[1], color='#3D9EF5')
plt.bar(lenguajes_encuesta[2], datos_encuesta[2], color='#2E80C9')
plt.bar(lenguajes_encuesta[3], datos_encuesta[3], color='#E02D36')
plt.bar(lenguajes_encuesta[4], datos_encuesta[4], color='black')
plt.title('Gráfico de barras')
plt.ylabel('Popularidad')
plt.show()

