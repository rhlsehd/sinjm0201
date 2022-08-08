#pragma warning(disable:4996) //c4996 ���� ����
#define _TM_ // struct ������ ���� ����
#define MAX_LENGTH 128
#include <stdio.h>
#include <time.h> //localtime �������
#include <windows.h> //system(cls) �������

#if !defined(_TM_) //localtime ����ü
struct tm
{
	int tm_mday;
	int tm_mon;
	int tm_year;
};
#endif

int total = 50000;

void manage();
void open();
int main()
{
	int sel;
	printf("1 : ����\n2 : ���� ����\n");
	scanf_s("%d", &sel);
	system("cls");

	switch (sel)
	{
	case 1:
		manage();
		break;
	case 2:
		open();
		break;
	}
	system("pause>null"); 
	return 0;
}

void manage()
{
	FILE* fp = fopen("accountbook.txt", "a");
	int income, expense;
	time_t timer;
	struct tm* t;
	timer = time(NULL);
	t = localtime(&timer);

	printf("���糯¥ : %d�� %d�� %d�� \n", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);
	printf("���� : ");
	scanf_s("%d", &income);
	printf("���� : ");
	scanf_s("%d", &expense);
	printf("�ܾ� : %d\n", total - (expense - income));

	int *result = total - (expense - income);
	
	fprintf(fp, "%d�� %d�� %d�� \n", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);
	fprintf(fp, "���� : %d\n", income);
	fprintf(fp, "���� : %d\n", expense);
	fprintf(fp, "�ܾ� : %d\n", result);
	fprintf(fp, "----------------\n");
	fclose(fp);
}

void open()
{
	int line_count = 0;
	char buffer[MAX_LENGTH];
	FILE* fp = NULL;

	if (0 == fopen_s(&fp, "accountbook.txt", "rt"))
	{
		printf("accountbook.txt ������ ������ ������ �����ϴ�. \n\n");
	}

	while (fgets(buffer, MAX_LENGTH, fp) != NULL)
	{
		line_count++;
		printf("%s", buffer);
	}
	fclose(fp);

	printf("\n\n");
}