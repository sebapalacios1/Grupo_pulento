class Sensor:
    def medir(self):
        print("Midiendo datos base...")

class SensorTemperatura(Sensor):
    # sobreescribo el metodo de arriba
    def medir(self):
        print("Midiendo temperatura en grados Celsius")

class SensorLuz(Sensor):
    def medir(self):
        print("Midiendo nivel de luz en Lux")

# funcion suelta, fuera de las clases
def iniciar_medicion(sensor):
    sensor.medir()

# testeando el polimorfismo
s1 = SensorTemperatura()
s2 = SensorLuz()

iniciar_medicion(s1)
iniciar_medicion(s2)