#include <stdio.h>
void right_tri(int sel);
void re_right_tri(int sel);
void pyramid(int sel);
void re_pyramid(int sel);

int main()
{
	int sel,flo;
	
	printf(" 1) 직각삼감형 \n 2) 역직각삼각형 \n 3) 피라미드 \n 4) 역피라미드 : \n");
	printf("도형을 선택하세요 : ");
	scanf_s("%d", &sel);
	printf("층 수를 입력하세요 : ");
	scanf_s("%d", &flo);
	
	if (sel == 1)
		right_tri(flo);
	else if (sel == 2)
		re_right_tri(flo);
	else if (sel == 3)
		pyramid(flo);
	else if (sel == 4)
		re_pyramid(flo);
	else
		printf("다시 입력해주세요, \n");
	return 0;
}

void right_tri(int sel)
{
	int i = 0, j = 0;
	char a = 'A';
	while (i < sel)
	{
		while (j <= i)
		{
			printf("%c", a);
			j++;
		}
		a++;
		printf("\n");
		j = 0;
		i++;
	}
}

void re_right_tri(int sel)
{
	int i = 0, j = 0;
	int sel1 = sel;
	char a = 'A'+sel-1;
	while (i < sel)
	{
		while (j < sel1)
		{
			printf("%c",a);
			j++;
		}
		a--;
		j = 0;
		sel1--;
		printf("\n");
		i++;
	}
}

void pyramid(int sel)
{
	int i = 0, j = 0, k = 0, h = 0;
	char a = 'A';
	while (i < sel)
	{
		int blank = sel - i;
		while (h <= blank)
		{
			printf(" ");
			h++;
		}
		h = 0;
		while (j <= k)
		{
			printf("%c",a);
			j++;
		}
		a++;
		j = 0;
		k = k+2;
		printf("\n");
		i++;
	}
}

void re_pyramid(int sel)
{
	int i = 0, j = 0, h = 0;
	int sel1 = sel*2-1;
	char a = 'A'+sel-1;
	while (i < sel)
	{

		int blank = i-1;
		while (h <= blank)
		{
			printf(" ");
			h++;
		}
		blank++;
		h = 0;
		while (j < sel1)
		{
			printf("%c", a);
			j++;
		}
		sel1 = sel1 - 2;
		a--;
		j = 0;
		printf("\n");
		i++;
	}
}