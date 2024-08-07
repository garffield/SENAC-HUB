#include <stdio.h>

int main(){

    int i, x, res;
    
    printf("Digite um numero: ");
    scanf("%d", &x);
    for (i = 0; i <= 10; i++){
        res = x * i;
        printf("%d x %d = %d\n", x , i, res);
    }




}