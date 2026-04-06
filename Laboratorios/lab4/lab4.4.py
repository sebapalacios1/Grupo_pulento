import pandas as pd
import matplotlib.pyplot as plt

ventas = pd.read_csv("ventas_tienda.csv")

plt.plot(ventas["Mes"], ventas["Laptops"], color="blue", label="Laptops")
plt.plot(ventas["Mes"], ventas["Smartphones"], color="red", label="Smartphones")

plt.title("Ventas Mensuales de Dispositivos Tecnológicos")
plt.xlabel("Mes")
plt.ylabel("Cantidad Vendida")
plt.legend()
plt.grid(True)
plt.show()