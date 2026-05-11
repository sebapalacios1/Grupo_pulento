#include <stdio.h>

int main() {
    // Definimos las variables como pide la guia
    int base, altura, area, perimetro;

    // Entrada de datos
    printf("base del rectangulo: ");
    scanf("%d", &base); // No olvidar el ampersand

    printf("altura del rectangulo: ");
    scanf("%d", &altura);

    // Operaciones
    area = base * altura;
    perimetro = (2 * base) + (2 * altura);

    // Salida de resultados
    printf("\nCalculos del rectangulo:\n");
    printf("area calculada : %d\n", area);
    printf(" perimetro calculado : %d\n", perimetro);

    return 0;
}
