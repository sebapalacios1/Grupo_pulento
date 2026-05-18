#include <stdio.h>

int main() {
    int N, contador = 0;

    // Pedir al usuario un límite positivo
    printf("Ingrese un valor límite N (entero positivo): ");
    scanf("%d", &N);

    // Si el usuario ingresa un número negativo, lo dejamos en 0 para evitar problemas
    if (N < 0) {
        N = 0;
        printf("Se ingresó un número negativo, se usará N = 0\n");
    }

    printf("\nNúmeros pares entre 0 y %d:\n", N);

    // Bucle for: recorremos desde 0 hasta N
    for (int i = 0; i <= N; i++) {
        // Verificamos si el número es par usando el módulo
        if (i % 2 == 0) {
            printf("%d ", i);
            contador++;   // incrementamos el contador cada vez que encontramos un par
        }
    }

    printf("\n\nTotal de números pares en el intervalo [0, %d]: %d\n", N, contador);

    return 0;
}