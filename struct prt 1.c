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
	strcpy(man1.name, "�ȼ���");
	strcpy(man1.phoneNum, "010-1122-3344");
	man1.age = 23;

	printf("�̸� �Է� : "); scanf_s("%s", man2.name);
	printf("��ȣ �Է� : "); scanf_s("%s", man2.phoneNum);
	printf("���� �Է� : "); scanf_s("%d", &(man2.age));

	printf("�̸� : "); scanf_s("%s", man1.name);
	printf("��ȣ : "); scanf_s("%s", man1.phoneNum);
	printf("���� : "); scanf_s("%d", man1.age);

	printf("�̸� : "); scanf_s("%s", man2.name);
	printf("��ȣ : "); scanf_s("%s", man2.phoneNum);
	printf("���� : "); scanf_s("%d", man2.age);

	return 0;
}