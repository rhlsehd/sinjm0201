#include <stdio.h>

int main()
{
	char voca[100];

	int len = 0, i;
	char max = 0;

	printf("���ܾ� �Է� : ");
	scanf_s("%s", voca);

	while (voca[len] != '\0')
		len++;

	for (i = 0; i < len; i++)
		if (max < voca[i])
			max = voca[i];


	printf("���� ū �ƽ�Ű �ڵ� ���� ���� : %c \n", max);
	return 0;
}