class Refrigerador:
    def __init__(self, marca):
        self.marca = marca
        self.__temperatura = 4  # temperatura por defecto

    def get_temp(self):
        return self.__temperatura

    def set_temp(self, grados):
        # El rango seguro del refri es entre 1 y 7 grados
        if 1 <= grados <= 7:
            self.__temperatura = grados
            print(f"[{self.marca}] Temperatura actualizada a {self.__temperatura}°C")
        else:
            print(f"[{self.marca}] Error: {grados}°C es un valor inválido")

if __name__ == "__main__":
    mi_refri = Refrigerador("refri")
    
    print(f"Temp de fábrica: {mi_refri.get_temp()}°C")
    
    mi_refri.set_temp(3)
    mi_refri.set_temp(-5)  # Esto debería tirar el error
    
    print(f"Temp final: {mi_refri.get_temp()}°C")