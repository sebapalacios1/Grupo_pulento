#ejercicio_1

def trama(a):
    try:
       
        partes = a.split(":") 
        sensor = partes[0]
        valor = float(partes[1])
        print(f"Sensor {sensor} operativo: {valor} unidades.")
        
    except IndexError:
        
        print("Error: Trama mal formateada (falta delimitador ':').")
    except ValueError:
        
        print("Error: El valor recibido no es numérico.")
    except Exception as e:
        
        print(f"Ocurrió un error inesperado: {e}")

# Pruebas
#procesar_trama("TEMP:25.4")  # Correcto
#procesar_trama("HUM_40")      # Gatilla IndexError
#procesar_trama("PRES:N/A")    # Gatilla ValueError

