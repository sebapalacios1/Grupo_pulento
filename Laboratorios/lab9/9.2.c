#include <stdio.h>

int main() {
    int num1, num2;

    // Pedimos los datos al usuario
    printf("primer numero: ");
    scanf("%d", &num1);
    printf("segundo numero: ");
    scanf("%d", &num2);

    // Hacemos los calculos directamente en el printf
    printf("\n--- Resultados ---\n");
    printf("Suma: %d\n", num1 + num2);
    printf("Resta: %d\n", num1 - num2);
    printf("Multiplicacion: %d\n", num1 * num2);
    printf("Modulo (Resto): %d\n", num1 % num2);

    return 0;
}
