#include <stdio.h>

void Swap(int*p1, int*p2);
void Title(int*test1, int*test2);
int main()
{
	int i;
	int test1[20], test2[20];
	
	for (i = 0; i < 20; i++)
	{
		scanf_s("%d", &test1[i]);
	}

	for (i = 0; i < 20; i++)
	{
		scanf_s("%d", &test2[i]);
	}

	Swap(test1, test2);
	
	return 0;
}

void Swap(int *p1, int*p2)
{
	int i;
	int tmp;

	for (i = 0; i < 20; i++)
	{
		tmp = p1[i];
		p1[i] = p2[i];
		p2[i] = tmp;
	}

	Title(p1, p2);
}

void Title(int *test1, int *test2)
{
	int i;

	printf("Shinjimin Program \n");
	printf("***test1*** \n");
	
	for (i = 0; i < 20; i++)
	{
		printf("test1[%d]=%d ", i, test1[i]);
	}
	
	printf("\n***test2***\n");
	
	for (i = 0; i < 20; i++)
	{
		printf("test2[%d]=%d ", i, test2[i]);
	}

	printf("\n\n");
}
