#include <stdio.h>

void select();
void even(int*p);
void odd(int*p);
int large_num(int*p);
int small_num(int*p);

int main()
{
	int i,sel; // ���� ����.
	int arr[10]; // �迭 ����
	
	for (i = 0; i < 10; i++) // ���ڸ� �޴� �ݺ���
	{
		printf("%d�� ���� �Է����ּ��� : ", i+1); scanf_s("%d", &arr[i]);
	}
	
	select();

	scanf_s("%d", &sel);

	switch (sel)
	{
	case 0: // sel�� 0 �ϋ� ����
		printf("���α׷��� �����մϴ�. \n");
		break;
	case 1: // sel�� 1 �ϋ� ����
		even(arr);
		odd(arr);
		break;
	case 2: // sel�� 2 �ϋ� ����
		printf("���� ū ���� %d �Դϴ�. \n", large_num(arr));
		break;
	case 3: // sel�� 3 �ϋ� ����
		printf("���� ���� ���� %d �Դϴ�. \n", small_num(arr));
		break;
	}
}

void select() //������ ������ִ� �Լ�.
{
	printf("�� ���α׷��� �迭�� �Լ��� �̿��Ͽ� ���� �Է¹ް�, Ȧ¦�� �����ϰų� ���� ū �� �Ǵ� ���� ���� ���� ���ϴ� ���α׷� �Դϴ�. \n");
	printf("1. Ȧ¦�� �����Ͽ���\n2. ���� ū ���� ã�ƶ�.\n3. ���� ���� ���� ã�ƶ�.\n ����� 0�Դϴ�. �޴��� �������ּ���.\n");
}

void even(int*p) //¦���� �������ִ� �Լ�.
{
	int i;
	for (i = 0; i < 10; i++)
	{
		if (p[i] % 2 == 0)
		{
			printf("¦�� : %d \n", p[i]);
		}

	}
}

void odd(int*p) //Ȧ���� �������ִ� �Լ�.
{
	int i;
	for (i = 0; i < 10; i++)
	{
		if (p[i] % 2 == 1)
		{
			printf("Ȧ�� : %d \n", p[i]);
		}

	}
}

int large_num(int*p) //���� ū ���� ������ִ� �Լ�.
{
	int i,max;
	max = p[0];

	for (i = 0; i < 10; i++)
	{
		if (max < p[i])
		{
			max = p[i];
		}
	}
	return max;
}

int small_num(int*p) // ���� ���� ���� ������ִ� �Լ�.
{
	int i, min;
	min = p[0];

	for (i = 0; i < 10; i++)
	{
		if (min > p[i])
		{
			min = p[i];
		}
	}
	return min;
}