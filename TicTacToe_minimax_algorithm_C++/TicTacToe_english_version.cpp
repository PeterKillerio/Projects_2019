#include "pch.h"
#include<iostream>
#include<vector>
using namespace std;

int Board[9];
string moznosti[8] = { "012", "345", "678", "048", "246", "036", "147", "258" };
int celkovoPrhl = 0;
int BestMove = -1;

int overPlochu(int *board)
{
	for (int i = 0; i < 8; ++i) {
		int pocet = 0;
		string sekvencia = moznosti[i];
		int prvaPoz = sekvencia[0] - 48;
		int znak;
		if (board[prvaPoz] == 1 || board[prvaPoz] == 2)
		{
			znak = board[prvaPoz];
			pocet++;
			for (int j = 1; j < 3; ++j) {
				if (board[sekvencia[j] - 48] == znak) { pocet++; }
				if (pocet == 3) { return 1; }
			}
		}
	}
	return 0;
}

int minimax(int board[9], int level, int hrac, int pocitac)
{
	int Score = 0;
	int BestScore = -2;
	int WorstScore = 2;
	int hlbka = level;
	hlbka++;

	int data = overPlochu(board);
	int predel = (hlbka % 2);

	if (data == 1)
	{
		if (predel == 1)
		{
			return -1;
		}
		else
		{
			return 1;
		}
	}
	for (int i = 0; i < 9; i++) {
		if (board[i] == 0)
		{
			if ((hlbka % 2) == 0)
			{
				board[i] = hrac;
				celkovoPrhl++;
				int doc = minimax(board, hlbka, hrac, pocitac);
				if (doc < WorstScore) { WorstScore = doc; }
				Score = WorstScore;
				board[i] = 0;
			}
			else if ((hlbka % 2) == 1)
			{
				board[i] = pocitac;
				celkovoPrhl++;
				int doc;
				doc = minimax(board, hlbka, hrac, pocitac);
				if (doc > BestScore)
				{
					BestScore = doc;

					if (hlbka == 1)
					{
						BestMove = i;
						cout << i << endl;
					}
				}
				Score = BestScore;
				board[i] = 0;
			}
		}
	}
	return Score;
}
int koniecHry(int *board)
{
	int poc = 0;
	for (int i = 0; i < 9; ++i) {
		if (board[i] == 0) { poc++; };
	}
	if (poc == 0) { return 1; }

	if (overPlochu(board)) { return 1; }
	return -1;
}
void hraX()
{
	while (koniecHry(Board) == -1)
	{
		for (int i = 0; i < 9; ++i) {
			if (Board[i] == 1) { cout << 'O' << " "; }
			if (Board[i] == 2) { cout << 'X' << " "; }
			if (Board[i] == 0) { cout << '-' << " "; }
			if ((i + 1) % 3 == 0) { cout << endl; }
		}cout << endl;

		int poz;
		cout << "its your turn: " << endl;
		cin >> poz;
		Board[poz] = 2;

		cout << "prediction: " << minimax(Board, 0, 2, 1) << endl;
		cout << "best move: " << BestMove << endl;
		cout << "all searches: " << celkovoPrhl << endl;
		celkovoPrhl = 0;
		Board[BestMove] = 1;

		for (int i = 0; i < 9; ++i) {
			if (Board[i] == 1) { cout << 'O' << " "; }
			if (Board[i] == 2) { cout << 'X' << " "; }
			if (Board[i] == 0) { cout << '-' << " "; }
			if ((i + 1) % 3 == 0) { cout << endl; }
		}cout << endl;
	}
	cout << "GAME OVER" << endl;
}
void hraO() {
	while (koniecHry(Board) == -1)
	{
		cout << "prediction: " << minimax(Board, 0, 1, 2) << endl;
		cout << "best move: " << BestMove << endl;
		cout << "all searches: " << celkovoPrhl << endl;
		celkovoPrhl = 0;
		Board[BestMove] = 2;

		for (int i = 0; i < 9; ++i) {
			if (Board[i] == 1) { cout << 'O' << " "; }
			if (Board[i] == 2) { cout << 'X' << " "; }
			if (Board[i] == 0) { cout << '-' << " "; }
			if ((i + 1) % 3 == 0) { cout << endl; }
		}cout << endl;

		if (koniecHry(Board) == 1) { break; }

		int poz;
		cout << "its your turn: " << endl;
		cin >> poz;
		Board[poz] = 1;
	}
	cout << "GAME OVER" << endl;

}
void initilize_game()
{
	char vstup = 0;
	char vst2 = 0;
	cout << "Do you wanna play as X or O ?  (x/o)" << endl;
	cin >> vstup;
	if (vstup == 'x')
	{
		hraX();
	}
	else if (vstup == 'o')
	{
		hraO();
	}
	else {
		cout << "Invalid input. Closing game." << endl;
		cout << endl;
		cout << "Do you want to play again? (y/n)" << endl;
		cin >> vst2;
		if (vst2 == 'y') { initilize_game(); }
		else if (vst2 == 'n') { initilize_game(); }
		else
		{
			cout << "Invalid input. Closing game." << endl;
			return;
		}
	}
}

int main()
{
	for (int i = 0; i < 9; ++i) {
		Board[i] = 0;
	}
	//human turn
	initilize_game();

	return 0;
}
