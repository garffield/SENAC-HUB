#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5}; // Initialize the array with some values
    int sum = 0, i;

    for (i = 0; i < 5; i++)
        sum += numbers[i];

    printf("The sum of the numbers is: %d\n", sum);

    return 0;
}