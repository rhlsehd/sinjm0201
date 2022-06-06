#include <stdio.h>

struct person
{
	char name[20];
	char phoneNUM[20];
	int age;
};

int main()
{

	struct person arr[3];

	int i;
	for (i = 0; i < 3; i++)
	{
		printf("이름 :");
		scanf_s("%s", arr[i].name,sizeof(arr[i].name));
		printf("전화번호 : ");
		scanf_s("%s", arr[i].phoneNUM,sizeof(arr[i].phoneNUM));
		printf("나이 : ");
		scanf_s("%d", &arr[i].age);
	}

	for (i = 0; i < 3; i++)
	{
		printf("%s %s %d \n", arr[i].name, arr[i].phoneNUM, arr[i].age);
	}

	return 0;
}




