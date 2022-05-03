#include <stdio.h>

double celtofah(double c);
double fahtocel(double f);

int main()
{
	double num;
	int sel;

	printf("1. ¼·¾¾¸¦ È­¾¾·Î 2. È­¾¾¸¦ ¼·¾¾·Î \n");
	scanf_s("%d", &sel);

	if (sel == 1)
	{
		printf("¼·¾¾ ÀÔ·Â : ");
		scanf_s("%lf", &num);
		printf("º¯È¯µÈ È­¾¾ : %f \n", celtofah(num));
	}

	else if (sel == 2)
	{
		printf("È­¾¾ ÀÔ·Â : ");
		scanf_s("%lf", &num);
		printf("º¯È¯µÈ È­¾¾ : %f \n", fahtocel(num));
	}

	else
		printf("¼±ÅÃ ¿À·ù \n");
}

double celtofah(double c)
{
	return 1.8*c + 32;
}

double fahtocel(double f)
{
	return (f - 32) / 1.8;
}