#include<stdio.h>



int addtototal(int num)
{
	static int total = 0;
	total += num;
	return total;
}

int main()
{
	int num, i;
	for (i = 0; i < 3; i++)
	{
		printf("�Է� %d : ", i + 1);
		scanf_s("%d", &num);
		printf("���� : %d \n", addtototal(num));
	}
	return 0;
}
