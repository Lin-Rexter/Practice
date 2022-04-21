#include <stdio.h>
#include <stdlib.h>

//程そ计(GCD)
int GCD(int a,int b){
	b == 0 ? a : GCD(b,a%b);
}

//程そ计(LCM)
int LCM(int a,int b){
	return a*b/GCD(a,b);
}

int main()
{
    int num1, num2, gcd, lcm;
 
    printf("叫块计1 (Please enter number1): ");
    scanf("%d", &num1); 
	printf("叫块计2 (Please enter number2): ");
    scanf("%d", &num2); 

    printf("\n程そ计 (GCD of %d and %d) = %d\n", num1, num2, GCD(num1,num2) );
	printf("程そ计 (LCM of %d and %d) = %d\n\n", num1, num2, LCM(num1,num2) );
	
	system("pause");
	return 0;
}