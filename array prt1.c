#include <stdio.h>

int main()
{
	int arr[5];
	int i;
	int total = 0;
	int max, min;
	for (i = 0; i < 5; i++)
	{
		printf("�迭�� �� �� �� �Է��ϼ��� : ");
		scanf_s("%d", &arr[i]);
		total += arr[i];
	}
	max = min = arr[0];
	for (i = 1; i < 5; i++)
	{
		if (max < arr[i])
			max = arr[i];
		if (min > arr[i])
			min == arr[i];
	}


	printf("�迭�� �Էµ� ���� �߿��� �ִ��� %d �Դϴ�.\n", max);
	printf("�迭�� �Էµ� ���� �߿��� �ּڰ��� %d �Դϴ�.\n", min);
	printf("�迭�� �Էµ� ������ �� ���� %d �Դϴ�. \n", total);
	return 0;
}