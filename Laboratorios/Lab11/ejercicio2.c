#include <stdio.h>

// funcion que recibe un puntero a un entero
void duplicarValor(int *numero) {
    // multiplicamos por 2 el valor al que apunta el puntero
    // el * sirve para acceder a ese valor
    *numero = *numero * 2;
}

int main() {
    // declaramos una variable entera llamada voltaje y le ponemos 12
    int voltaje = 12;

    // mostramos el valor antes de llamar a la funcion
    printf("--- Antes de llamar a la funcion ---\n");
    printf("Valor de voltaje en main: %d\n\n", voltaje);

    // llamamos a la funcion pasandole la direccion de voltaje
    // usamos & para obtener la direccion de memoria
    duplicarValor(&voltaje);

    // mostramos otra vez el valor, deberia ser 24
    printf("--- Despues de llamar a la funcion ---\n");
    printf("Valor de voltaje en main: %d\n", voltaje);

    return 0;
}