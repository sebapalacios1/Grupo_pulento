class Bateria:
    def __init__(self, marca):
        self.marca = marca
        # Usamos __ para que sea privada (encapsulamiento)
        self.__carga = 100 

    def usar_bateria(self, gasto):
        self.__carga -= gasto
        # Si la carga baja de 0, la dejamos en 0 y avisamos
        if self.__carga <= 0:
            self.__carga = 0
            print("Batería agotada")

    def ver_carga(self):
        # Para poder leer la carga privada
        return self.__carga

#Pruebas según la guía
mi_bat = Bateria("LiPo-Max")

print(f"Carga al empezar: {mi_bat.ver_carga()}%")

# Primer uso: 40%
mi_bat.usar_bateria(40)
print(f"Carga tras primer uso: {mi_bat.ver_carga()}%")

# Segundo uso: 80% (acá debería quedar en 0)
mi_bat.usar_bateria(80)
print(f"Carga final: {mi_bat.ver_carga()}%")