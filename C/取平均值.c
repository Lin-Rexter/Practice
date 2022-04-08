#include<stdio.h>
#include<stdlib.h>

int main() {
    float num[3], sum=0;
    int i;
    for (i = 0; i < 3; i++) {
        printf("Input a number to num[%d] : ", i);
        scanf("%f", &num[i]);
        sum = sum + num[i];
    }
    printf("The average is %f\n", sum / i);
    system("pause");
    return 0;
}
