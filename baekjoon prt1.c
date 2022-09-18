#include <stdio.h>

int main()
{
	int a[10];
	int b[10];
	int i, j, first, temp;
	int n = 10;

	for (i = 0; i < 10; i++)
	{
		scanf_s("%d", &a[i]);

		b[i] = a[i] % 42;
	}

	for (i = 0; i < 10; i++)
	{
		for (j = i + 1; j < 10; j++)
		{
			if (b[i] > b[j])
			{
				temp = b[i];
				b[i] = b[j];
				b[j] = temp;
			}
		}

	}

	for (i = 0; i < 10; i++)
	{
		first = b[i];
		for (j = i+1; j < 10; j++)
		{
			if (first == b[j])
				if (b[j] == b[j + 1])
					continue;
				else
					n--;
		}
	}
	
	printf("%d", n);

	return 0;
}