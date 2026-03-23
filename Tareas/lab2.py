#datos

red_esp8266 = {
    "Nodo_Tanque": {"ip": "192.168.1.10", "estado": "activo", "salida_dac": 3000},
    "Nodo_Motor": {"ip": "192.168.1.11", "estado": "falla", "salida_dac": 0},
    "Nodo_Valvula": {"ip": "192.168.1.12", "estado": "inactivo", "salida_dac": 150},
    "Nodo_Caldera": {"ip": "192.168.1.13", "estado": "activo", "salida_dac": 4000}
}

coords_x = [2, 8, 8, 2]
coords_y = [1, 1, 5, 5]

angulos_prueba = (45, 90, -30, 15)
configuracion_robot = {
    "velocidad": 50,
    "torque_max": 120,
    "herramienta": "pinza"
}


#ejercicio1 

def auditar_red(nodos):
    tot_nodos= len(nodos)
    nodos_falla =[]
    suma_dac=0
    contador_activos =0
    
    for nombre, datos in nodos.items():
        if datos["estado"] in ["falla", "inactivo"]:
            nodos_falla.append(datos["ip"])
        
        elif datos["estado"] == "activo":
            suma_dac+= datos["salida_dac"]
            contador_activos +=1
            
    promedio_dac=suma_dac/ contador_activos if contador_activos > 0 else 0
    
    return tot_nodos, nodos_falla, promedio_dac

print("solucion 1")
total, fallas, promedio = auditar_red(red_esp8266)
print(f"nodos totales: {total}")
print(f"IPs fallas o inactivos: {fallas}")
print(f"promedio dac activos: {promedio}")


#ejercicio 2


def evaluar_zona_poligono(cord_x, cord_y):
    ancho =max(cord_x)-min(cord_x)
    alto=max(cord_y)-min(cord_y)
    area= ancho*alto
    
    centrogeo_x=(max(cord_x) + min(cord_x))/2
    centrogeo_y= (max(cord_y) + min(cord_y))/ 2
    
    return (ancho, alto), area, (centrogeo_x, centrogeo_y)

print("\n solucion 2 ")
totalejercicio2, area_final, centro=evaluar_zona_poligono(coords_x, coords_y)
print(f"Área calculada: {area_final}")
print(f"Centro del polígono: {centro}")


#ejercicio 3


def calibrar_robot(*args, **kwargs):
    desplazamiento_tot = sum(args)
    print(f"movimiento: {len(args)}")
    print(f"desplazamiento total: {desplazamiento_tot} grados")
    
    if "torque_max" in kwargs and kwargs["torque_max"]>100:
        print("sobrecarga")
        
    print("-" * 20)
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
    print("-" * 20)



print("\n solucion3")
calibrar_robot(*angulos_prueba, **configuracion_robot)



