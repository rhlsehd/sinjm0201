#include <stdio.h>

int bignumbercompare(int num1, int num2, int num3);
int smallnumbercompare(int num1, int num2, int num3);

int main()
{
	int num1, num2, num3;

	printf("세 개의 정수 입력 : ");
	scanf_s("%d %d %d", &num1, &num2, &num3);
	printf("가장 작은 수는 : %d \n", smallnumbercompare(num1, num2, num3));
	printf("가장 큰 수는 : %d \n", bignumbercompare(num1, num2, num3));
	return 0;
}

int bignumbercompare(int num1, int num2, int num3)
{
	if (num1 > num2)
		if (num1 > num3)
			return num1;
	if (num2 > num1)    //else if 로 넣으면 안됨(??)
		if (num2 > num3)
			return num2;
	else
			return num3;
}

int smallnumbercompare(int num1, int num2, int num3)
{
	if (num1 < num2)
		if (num1 < num3)
			return num1;
	if (num2 < num1)
		if (num2 < num3)
			return num2;
	else
			return num3;
}