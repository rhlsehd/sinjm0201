#include <stdio.h>

int main()
{
	int arr[5];
	int i;
	int total = 0;
	int max, min;
	for (i = 0; i < 5; i++)
	{
		printf("배열에 들어갈 수 를 입력하세요 : ");
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


	printf("배열에 입력된 정수 중에서 최댓값은 %d 입니다.\n", max);
	printf("배열에 입력된 정수 중에서 최솟값은 %d 입니다.\n", min);
	printf("배열에 입력된 정수의 총 합은 %d 입니다. \n", total);
	return 0;
}