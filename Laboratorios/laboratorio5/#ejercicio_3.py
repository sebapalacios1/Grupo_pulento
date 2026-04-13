#ejercicio_3

sensores={"temp":[22.5,23.1,22.8], "presion":[1013,1015], "humedad":[]}
sensor=str(input("ingrese el sensor que desea obtener datos "))
try:    
    sensor_elegido=sensores[sensor][:]
    promedio= sum(sensor_elegido)/ len(sensor_elegido)
    print("el promedio es del sensor " ,{sensor}, " es ",{promedio})
except KeyError:
    print("el sensor elegido no existe en el diccionario")
except ZeroDivisionError:
    print("el sensor humedad se encuentra sin valores")

finally: 
    print("el proceso de consulta a finalizado")

