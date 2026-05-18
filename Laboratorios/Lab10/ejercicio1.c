#include <stdio.h>

int main() {
    int temp;

    printf("Ingrese el valor de la temperatura en °C: ");
    scanf("%d", &temp);

    if (temp < 20) {
        printf("Estado: Subenfriamiento \n");
    } else if (temp >= 20 && temp <= 45) {
        printf("Estado: Operación Nominal\n");
    } else {
        printf("Estado: Alarma de Sobrecalentamiento\n");
    }
printf("la temperatura actual es %d°", temp);
    return 0;
}