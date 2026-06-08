#include <stdio.h>

int main() {
    int resto;
    int N;
    int i;

    printf("Ingrese el numero hasta donde desea imprimir: ");
    scanf("%d", &N);

    for (i = 0; i < N; i++) {
        resto = i % 2;

        if (resto == 0) {
            printf("%d\n", i);
        }
    }

    return 0;
}
