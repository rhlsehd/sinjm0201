#include <iostream>

int main()
{
	int num;

	while (1)
	{

		std::cout << "�Ǹ� �ݾ��� ���� ������ �Է� (-1 to end) : ";
		std::cin >> num;
		if (num == -1)
		{
			std::cout << "���α׷��� �����մϴ�." << std::endl;
			break;
		}

		else
			std::cout << "�̹� �� �޿� : " << 50 + num * 0.12 << "����" << std::endl;
	}

	return 0;
}