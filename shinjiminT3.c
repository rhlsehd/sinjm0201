#include <stdio.h>

void avr1(int p[][4]);
void avr2(int p[][4]);
void avr3(int p[][4]);

int main()
{
	int hanshin_apart[3][4] = { {3,3,3,2},{3,3,2,2},{4,4,4,3} };

	printf("*** Hanshin Apart Report *** \n");
	printf("** 1�� 1ȣ���� ���� : %x \n", &hanshin_apart[0][0]);
	avr1(hanshin_apart);
	avr2(hanshin_apart);
	avr3(hanshin_apart);
	printf("*** Reported by Shin Jimin \n");

	return 0;
}

void avr1(int p[][4])
{
	int i,j;
	int total = 0;
	for (i = 0; i < 1; i++)
	{
		for (j = 0; j < 4; j++)
		{
			p[i][j];
			total += p[i][j];
		}
	}
	
	 printf("** 1�� �ֹμ� : %d ��, 1�� �ֹμ� ��� : %.2f ��\n", total, (float)total/4);
	
}

void avr2(int p[][4])
{
	int i, j;
	int total = 0;
	for (i = 1; i < 2; i++)
	{
		for (j = 0; j < 4; j++)
		{
			p[i][j];
			total += p[i][j];
			
		}
	}
	
	printf("** 2�� �ֹμ� : %d ��, 2�� �ֹμ� ��� : %.2f ��\n", total, (float)total/4);
}

void avr3(int p[][4])
{
	int i, j;
	int total = 0;
	for (i = 2; i < 3; i++)
	{
		for (j = 0; j < 4; j++)
		{
			p[i][j];
			total += p[i][j];
		}
	}
	
	printf("** 3�� �ֹμ� : %d ��, 3�� �ֹμ� ��� : %.2f ��\n", total, (float)total/4);
}