#include <stdio.h>

int main()
{
	int a, b, c;

	scanf_s("%d %d %d", &a, &b, &c);

	if (a == b)
	{
		if (a == c)
		{
			printf("%d", 10000 + a * 1000);
		}

		else
			printf("%d", 1000 + a * 100);
	}

	else if (a != b )
	{
		if (b != c)
		{

			if (a == c)
			{
				printf("%d", 1000 + a * 100);
			}

			else if (a > b)
			{
				if (a > c)
					printf("%d", a * 100);
				else
					printf("%d", c * 100);
			}

			else if (a < b)
			{
				if (b > c)
					printf("%d", b * 100);
				else
					printf("%d", c * 100);
			}
		}

		else
			printf("%d", 1000 + b * 100);
	}

	return 0;
}