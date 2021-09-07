#include<iostream>
#include<vector>
#include<map>
using namespace std;

// IMPORTANT: NO NEED TO INCLUDE THE HEADERS WHICH ARE ALREADY INCLUDED ONCE IN ONE OF THE HEADER FILES
// #include "header_cube.h"
#include "header_basics.h"
#include "header_play_game.h"

// hashmap : {number(1,2,3,4,5) } => {list: x, y, z and chance(X,O,_)}
// check fo empty pos _ ones
// then collinear ones ... then sum
// 1: _ 1,1,1
// 2: _ 2,1,1
// 21: O 1,0,1
// 
// 

int main(void)
{
    square magic_1(3);
    magic_1.add_basic_values(2);
    // magic_1.print_square();

    square magic_2(3);
    magic_2.add_basic_values(3);
    // magic_2.print_square();

    magic_1.next_sqaure(&magic_2);
    // magic_1.next->print_square();

    magicCube myCube(3);
    int x,y,z;
    cout<<"Enter co-ordinates (x,y,z) of first element: ";
    cin>>x>>y>>z;
    myCube.make_magic_cube(x,y,z);
    myCube.print_cube();
    myCube.start_game();
    // cout<<check_linearity(1,11,121,0,4,0,1,5,0);
    map<int,vector<int>>* game_status = myCube.get_game_status();

    get_current_boards(*game_status);

    running_game(game_status);
    get_current_boards(*game_status);

    return 0;
}
