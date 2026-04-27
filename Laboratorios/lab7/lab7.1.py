class Termostato:
    def __init__(self, hab):
        self.hab = hab
        self.__temperatura = 20 # la variable privada
        
    def ver_temperatura(self):
        return self.__temperatura
        
    def cambiar_temperatura(self, nuevo_val):
        # checkear que esté en el rango para q no se rompa el aire
        if nuevo_val >= 15 and nuevo_val <= 30:
            self.__temperatura = nuevo_val
            print(f"temp cambiada a {self.__temperatura}")
        else:
            print("Error: Temperatura no permitida")

# prueba
termo = Termostato("pieza")
print(termo.ver_temperatura())
termo.cambiar_temperatura(24)
termo.cambiar_temperatura(100) # indica el error