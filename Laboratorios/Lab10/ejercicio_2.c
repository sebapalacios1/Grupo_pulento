#include <stdio.h>
int main(){
    int option;
    do { 
        printf("\n PANEL DE CONTROL \n1. Activar motores\n2. detener motores\n3. retroceder motores\n4. Salir del panel de control");
        printf("\ningrese su opcion\n");
        scanf("%d:", &option);
        switch(option)
        {
        case 1:
        printf("motores encendidos, mover vehiculo\n");
        break;
        case 2:
        printf("detener motores\n");
        break;
        case 3:
        printf("generar lectura de los sensores\n");
        break;
        case 4:
        printf("Salir del panel de control\n");
        break;
    }
    } while (option !=4);
    return 0;

}
