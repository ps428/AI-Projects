#include<iostream>
#include<vector>
#include<map>
using namespace std;

#include "header_cube.h"

void machine_chance(map<int,vector<int>>* game_status)
{
}

// Working now
void get_current_boards(map<int,vector<int>>* game_status)
{
    magicCube a = magicCube(3);
    a.make_cube_using_map(*game_status);
    a.print_game_cube();
}