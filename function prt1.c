#include <stdio.h>

int bignumbercompare(int num1, int num2, int num3);
int smallnumbercompare(int num1, int num2, int num3);

int main()
{
	int num1, num2, num3;

	printf("�� ���� ���� �Է� : ");
	scanf_s("%d %d %d", &num1, &num2, &num3);
	printf("���� ���� ���� : %d \n", smallnumbercompare(num1, num2, num3));
	printf("���� ū ���� : %d \n", bignumbercompare(num1, num2, num3));
	return 0;
}

int bignumbercompare(int num1, int num2, int num3)
{
	if (num1 > num2)
		if (num1 > num3)
			return num1;
	if (num2 > num1)    //else if �� ������ �ȵ�(??)
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