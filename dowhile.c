#include <stdio.h>

int main(void)
{
    int x;
    
    do
    {
        printf("Insira um numero maior que 10: ");
        scanf("%i", &x);
        if(x <= 10)
            printf("O valor digitado e menor ou igual a 10.\n");
    } while (x < 10);
    
    return 0;
}