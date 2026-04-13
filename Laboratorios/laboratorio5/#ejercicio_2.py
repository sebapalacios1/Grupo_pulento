#ejercicio_2 
 
def mover_Servo(b):
    try:
        if not isinstance(b,int):
            raise TypeError("el valor del angulo debe ser entero")
   

        assert 0<=b<=180,f"angulo {b} fuera de rango(0°-180°)"
        print("moviendo motor en" ,{b}, " ° ")    
    except TypeError as e:
        print(f"fallo de software:{e}")
    except AssertionError as e:
        print(f"fallo de seguridad en hardware {e}")
   
    finally:
        print("estado del motor: standby.") 

#pruebbas 
#mover_Servo(109)
#mover_Servo(200)
#mover_Servo("a")
