#include <stdio.h>

double celtofah(double c);
double fahtocel(double f);

int main()
{
	double num;
	int sel;

	printf("1. ������ ȭ���� 2. ȭ���� ������ \n");
	scanf_s("%d", &sel);

	if (sel == 1)
	{
		printf("���� �Է� : ");
		scanf_s("%lf", &num);
		printf("��ȯ�� ȭ�� : %f \n", celtofah(num));
	}

	else if (sel == 2)
	{
		printf("ȭ�� �Է� : ");
		scanf_s("%lf", &num);
		printf("��ȯ�� ȭ�� : %f \n", fahtocel(num));
	}

	else
		printf("���� ���� \n");
}

double celtofah(double c)
{
	return 1.8*c + 32;
}

double fahtocel(double f)
{
	return (f - 32) / 1.8;
}