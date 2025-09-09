#include <stdio.h>

int main(void) {
    int c = 55;
    int input;
    
    printf("Enter an integer: ");
    scanf("%d", &input);
    int sum = c + input;
    printf("The sum of c(%d) and %d is %d\n", c, input, sum);

    return 0;
}