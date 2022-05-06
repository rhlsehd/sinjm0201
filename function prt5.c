#include <stdio.h>

int problem(int num);

int main()
{
	int num;
	printf("정수입력 : ");
	scanf_s("%d", &num);
	printf("2의 %d승은 %d", num, problem(num));
}

int problem(int num)
{
	int i;
	int result = 1;
	for (i = 1; i <= num; i++)
	{
		result *= 2;
	}
	return result;
}
