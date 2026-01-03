#include <iostream>
#include <map>
#include <string>

using namespace std;

// initialize grid
char grid[3][3] = {{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};

// possible win conditions
int win_conditions[8][3][2] = {
    {
        {0, 0}, {0, 1}, {0, 2}
    },{
        {1, 0}, {1, 1}, {1, 2}
    },{
        {2, 0}, {2, 1}, {2, 2}
    },{
        {0, 0}, {1, 0}, {2, 0}
    },{
        {0, 1}, {1, 1}, {2, 1}
    },{
        {0, 2}, {1, 2}, {2, 2}
    },{
        {0, 0}, {1, 1}, {2, 2}
    },{
        {2, 0}, {1, 1}, {0, 2}
    }};

// X or O
char current_player = 'X';

void end_game() {
    cout << current_player << " Won the game!\n";
    exit(0);
}

void place_thing() {
    cout << "Place now, " << current_player << "!\n";
    cout << "First type the X coordinate and then the y ex(0, 2):";
    int x;
    int y;
    cin >> x >> y;
    if (grid[x][y] == 0) {
        grid[x][y] = current_player;
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
    for (int i = 0; i < 8; i++) {
        int win_check = 0;
        for (int j = 0; j < 3; j++) {
            int check_x = win_conditions[i][j][0];
            int check_y = win_conditions[i][j][1];
            if (grid[check_x][check_y] == current_player) {
                win_check++;
            }
        }
        if (win_check == 3) end_game();
    }
    if (current_player == 'X') {
        current_player = 'O';
    }
    else {
        current_player = 'X';
    }
    }

int main() {
    cout << "Hello World!\n";
    while (true) {
        place_thing();
    }
}