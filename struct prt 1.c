#include <stdio.h>
#include <string.h>

struct person
{
	char name[20];
	char phoneNum[20];
	int age;
};

int main()
{
	struct person man1, man2;
	strcpy(man1.name, "안성준");
	strcpy(man1.phoneNum, "010-1122-3344");
	man1.age = 23;

	printf("이름 입력 : "); scanf_s("%s", man2.name);
	printf("번호 입력 : "); scanf_s("%s", man2.phoneNum);
	printf("나이 입력 : "); scanf_s("%d", &(man2.age));

	printf("이름 : "); scanf_s("%s", man1.name);
	printf("번호 : "); scanf_s("%s", man1.phoneNum);
	printf("나이 : "); scanf_s("%d", man1.age);

	printf("이름 : "); scanf_s("%s", man2.name);
	printf("번호 : "); scanf_s("%s", man2.phoneNum);
	printf("나이 : "); scanf_s("%d", man2.age);

	return 0;
}