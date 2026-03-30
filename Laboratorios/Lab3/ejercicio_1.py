import numpy as np
import matplotlib.pyplot as plt

x=int(input("ingrese el valor n de la serie de fibonacci que desea(recomendamos un valor del 6 al 12):"))
fib=np.array([1,1])

for i in range(2,x):
    fib=np.append(fib,fib[i-1]+fib[i-2])

fib_fin=np.append([0],fib)
print(fib)

fig, ax = plt.subplots(figsize=(8, 8))

sx,sy=0,0
ang=0

for i in range(x):
    r=fib[i]
    
    theta = np.linspace(np.radians(ang), np.radians(ang + 90), 100)
    x_cos=sx+r*np.cos(theta)
    y_sen=sy+r*np.sin(theta)

    ax.plot(x_cos,y_sen, color="blue", lw=2)

    # actualizar centro para el siguiente arco
    if i < x - 1:
        r_next = fib[i+1]

        # punto final del arco actual
        theta_fin = np.radians(ang + 90)
        x_fin = sx + r*np.cos(theta_fin)
        y_fin = sy + r*np.sin(theta_fin)

        # el siguiente arco comienza en ang+90
        theta_inicio_sig = np.radians(ang + 90)

        # nuevo centro del siguiente arco
        sx = x_fin - r_next*np.cos(theta_inicio_sig)
        sy = y_fin - r_next*np.sin(theta_inicio_sig)

    ang += 90

ax.set_aspect('equal')
plt.title(f"Espiral de Fibonacci ({x} coeficientes)")
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
