#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;


class Avg_Calculate
{
public :
	int score[5][3];
	int count[5];

	void result();
	void descending_order();
};

void Avg_Calculate::result()
{
	for (int i = 0; i < 5; i++)
	{
		int sum = 0;
		for (int j = 0; j < 3; j++)
		{
			sum += score[i][j];
		}
		count[i] = sum / 3;
	}
}

void Avg_Calculate::descending_order()
{
	int temp;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; 4 - j; j++)
		{
			if (count[j] > count[j + 1])
			{
				temp = count[j];
				count[j] = count[j + 1];
				count[j + 1] = temp;
			}
		}
	}
}
int main()
{
	Avg_Calculate n;

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			cin >> n.score[i][j];
		}
	}

	n.result();
	n.descending_order();

	ofstream ofstr;
	ofstr.open("calculate");

	if (!ofstr.is_open())
	{
		cout << "열리지 않음";
		assert(false);
	}

	ofstr << "shin ji min" << endl;
	for (int i = 0; i < 5; i++)
	{
		ofstr << n.count[i] << endl;
	}
	return 0;
}