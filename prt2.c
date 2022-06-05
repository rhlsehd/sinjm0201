#include <stdio.h>

void select();
void even(int*p);
void odd(int*p);
int large_num(int*p);
int small_num(int*p);

int main()
{
	int i,sel; // 변수 선언.
	int arr[10]; // 배열 선언
	
	for (i = 0; i < 10; i++) // 숫자를 받는 반복문
	{
		printf("%d번 수를 입력해주세요 : ", i+1); scanf_s("%d", &arr[i]);
	}
	
	select();

	scanf_s("%d", &sel);

	switch (sel)
	{
	case 0: // sel이 0 일떄 실행
		printf("프로그램을 종료합니다. \n");
		break;
	case 1: // sel이 1 일떄 실행
		even(arr);
		odd(arr);
		break;
	case 2: // sel이 2 일떄 실행
		printf("가장 큰 수는 %d 입니다. \n", large_num(arr));
		break;
	case 3: // sel이 3 일떄 실행
		printf("가장 작은 수는 %d 입니다. \n", small_num(arr));
		break;
	}
}

void select() //문장을 출력해주는 함수.
{
	printf("이 프로그램은 배열과 함수를 이용하여 수를 입력받고, 홀짝을 구분하거나 가장 큰 수 또는 가장 작은 수를 구하는 프로그램 입니다. \n");
	printf("1. 홀짝을 구분하여라\n2. 가장 큰 수를 찾아라.\n3. 가장 작은 수를 찾아라.\n 종료는 0입니다. 메뉴를 선택해주세요.\n");
}

void even(int*p) //짝수를 구별해주는 함수.
{
	int i;
	for (i = 0; i < 10; i++)
	{
		if (p[i] % 2 == 0)
		{
			printf("짝수 : %d \n", p[i]);
		}

	}
}

void odd(int*p) //홀수를 구별해주는 함수.
{
	int i;
	for (i = 0; i < 10; i++)
	{
		if (p[i] % 2 == 1)
		{
			printf("홀수 : %d \n", p[i]);
		}

	}
}

int large_num(int*p) //가장 큰 수를 출력해주는 함수.
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

int small_num(int*p) // 가장 작은 수를 출력해주는 함수.
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