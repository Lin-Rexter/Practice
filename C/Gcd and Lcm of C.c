#include <stdio.h>
#include <stdlib.h>

//�̤j���]��(GCD)
int GCD(int a,int b){
	b == 0 ? a : GCD(b,a%b);
}

//�̤p������(LCM)
int LCM(int a,int b){
	return a*b/GCD(a,b);
}

int main()
{
    int num1, num2, gcd, lcm;
 
    printf("�п�J�Ʀr1 (Please enter number1): ");
    scanf("%d", &num1); 
	printf("�п�J�Ʀr2 (Please enter number2): ");
    scanf("%d", &num2); 

    printf("\n�̤j���]�� (GCD of %d and %d) = %d\n", num1, num2, GCD(num1,num2) );
	printf("�̤p������ (LCM of %d and %d) = %d\n\n", num1, num2, LCM(num1,num2) );
	
	system("pause");
	return 0;
}