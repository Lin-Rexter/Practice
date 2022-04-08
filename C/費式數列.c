#include <stdio.h>
#include <stdlib.h>
int f(int);

int main() {
	int in;
	printf("please input a number:");
	scanf("%d",&in);
	printf("f(%d)=%d \n",in,f(in));
	system("pause");
	return 0;
}

int f(int n){
	if(n==1 || n==2){
		return 1;
	}else{
		return (f(n-1)+f(n-2));
	}
} 

