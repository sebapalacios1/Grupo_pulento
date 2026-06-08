#include <stdio.h>

// definimos la estructura Sensor
struct Sensor {
    int id;           // numero entero para identificar
    float medicion;   // valor flotante de la medida
};

int main() {
    // declaramos una variable del tipo struct Sensor
    struct Sensor mi_sensor;

    // le asignamos el id 1
    mi_sensor.id = 1;
    // le asignamos una medicion de 25.5
    mi_sensor.medicion = 25.5;

    // mostramos los datos en pantalla
    printf("--- Datos del Sensor ---\n");
    printf("ID del Sensor: %d\n", mi_sensor.id);
    // mostramos la medicion con un solo decimal (aunque podria ser %f sin mas)
    printf("Medicion:     %.1f\n", mi_sensor.medicion);

    return 0;
}