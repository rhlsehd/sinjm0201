#include <stdio.h>

int problem(int num);

int main()
{
	int num;
	printf("�����Է� : ");
	scanf_s("%d", &num);
	printf("2�� %d���� %d", num, problem(num));
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
