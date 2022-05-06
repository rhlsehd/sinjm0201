#include <stdio.h>

void showfiboseries(int num)
{
	int f1 = 0, f2 = 1, f3, i;

	if (num == 1)
		printf("%d ", f1);
	else printf("%d %d ", f1, f2);

	for (i = 0; i < num - 2; i++)
	{
		f3=f1+f2;
		printf("%d ", f3);
		f1 = f2;
		f2 = f3;
	}
}

int main()
{
	int n;
	printf("����ϰ��� �ϴ� �Ǻ���ġ ������ ���� : ");
	scanf_s("%d", &n);
	if (n < 1)
	{
		printf("1�̻��� ���� �Է��ϼ���. \n");
		return -1;
	}
	showfiboseries(n);
	return 0;
}



