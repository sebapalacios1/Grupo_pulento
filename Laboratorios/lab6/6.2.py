class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.en_marcha = False

    def arrancar(self):
        self.en_marcha = True
        print(f"[{self.marca}] Motor encendido. Listo para salir.")

    # Función estática: la dejo acá porque sirve para cualquier vehículo
    @staticmethod
    def presion_ok(psi):
        # asumo que lo ideal es entre 30 y 35
        return 30 <= psi <= 35


class AutoHibrido(Vehiculo):
    def __init__(self, marca, bateria):
        super().__init__(marca) # llama al init de la clase padre
        self.bateria = bateria
    
    def usar_modo_ev(self):
        if not self.en_marcha:
            print(f"[{self.marca}] Error: Primero tienes que arrancar el auto.")
            return
            
        if self.bateria > 20:
            print(f"[{self.marca}] Modo 100% eléctrico activado (Batería: {self.bateria}%).")
        else:
            print(f"[{self.marca}] Batería muy baja para usar el modo eléctrico.")


if __name__ == "__main__":
    # Probando la función estática directo desde la clase sin instanciar
    presion_rueda = 28
    print(f"¿La presión de {presion_rueda} psi está bien?: {Vehiculo.presion_ok(presion_rueda)}\n")
    
    # Probando el auto
    mi_auto = AutoHibrido("Peugeot", 45)
    
    mi_auto.usar_modo_ev()  # Va a reclamar porque está apagado
    mi_auto.arrancar()      # Método heredado
    mi_auto.usar_modo_ev()  # Ahora sí entra