#include <stdio.h>
int main(){

    int dia;
    
    printf("Insira um numero de 1 a 7: ");
    scanf("%i", &dia);

    switch (dia){
        case 1:
            printf("Dia da semana: Domingo");
            break;
        case 2:
            printf("Dia da semana: Segunda-feira");
            break;
        case 3:
            printf("Dia da semana: Terça-feira");
            break;
        case 4:
            printf("Dia da semana: Quarta-feira");
            break;
        case 5:
            printf("Dia da semana: Quinta-feira");
            break;
        case 6:
            printf("Dia da semana: Sexta-feira");
            break;
        case 7:
            printf("Dia da semana: Sábado");
            break;
        default:
            printf("Valor Inválido");
            break;
    }


    return 0;
}