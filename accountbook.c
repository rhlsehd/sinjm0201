#pragma warning(disable:4996) //c4996 오류 방지
#define _TM_ // struct 재정의 오류 방지
#define MAX_LENGTH 128
#include <stdio.h>
#include <time.h> //localtime 헤더파일
#include <windows.h> //system(cls) 헤더파일

#if !defined(_TM_) //localtime 구조체
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
	printf("1 : 관리\n2 : 파일 열기\n");
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

	printf("현재날짜 : %d년 %d월 %d일 \n", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);
	printf("수입 : ");
	scanf_s("%d", &income);
	printf("지출 : ");
	scanf_s("%d", &expense);
	printf("잔액 : %d\n", total - (expense - income));

	int *result = total - (expense - income);
	
	fprintf(fp, "%d년 %d월 %d일 \n", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);
	fprintf(fp, "수입 : %d\n", income);
	fprintf(fp, "지출 : %d\n", expense);
	fprintf(fp, "잔액 : %d\n", result);
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
		printf("accountbook.txt 파일의 내용은 다음과 같습니다. \n\n");
	}

	while (fgets(buffer, MAX_LENGTH, fp) != NULL)
	{
		line_count++;
		printf("%s", buffer);
	}
	fclose(fp);

	printf("\n\n");
}