#include<iostream>
#include<vector>
#include<map>
using namespace std;

#include "header_cube.h"
void running_game(map<int,vector<int>>* game_status);
void fill_center(map<int,vector<int>>* game_status);
void get_current_boards(map<int,vector<int>>* game_status);

void running_game(map<int,vector<int>>* game_status)
{
    // Game status is a hashmap with int: list

    // Trying something for this one
    // For a general case, try to go to middle element and then wait for user to play his/her turn
    // Then try to make two {for now take any point opposite + 1 left to the user's chance as optimal second move}
    // Then check whether machine is making a win by checking for linearity for the points and then checking the sum thing euqal to 42, 
    // Then if that is vacant or not, if yes then fill else again untill all points are done
    // After this too if no move found, then check for poss win of user/human, and try to block it if it is vacant
    // For last case, when no victory for anyone, mark any corners, if not then any other remaining point {oprimisation needed  here}
    // Also make a hashmap for the points and poistions that are redundant now.. redundant as in they are already marked 
    
    fill_center(game_status);
}


void fill_center(map<int,vector<int>>* game_status)
{
    // making a default move to center if it is empty
    for(auto it = game_status->cbegin(); it!= game_status->cend(); it++)
    {
        int x = it->second[0];   
        int y = it->second[1];   
        int z = it->second[2];   
        int move = it->second[3];   

        vector<int> new_move = {x, y, z, 1};
        
        // Mening centre block is empty then fill it
        if(x==1&&y==1&&z==1&&move==-1)
        {
            (*game_status)[it->first] = new_move;
        }
    }
}
vector<int> get_user_move()
{
    vector<int> response;

    int x,y,z;
    cin>>x>>y>>z;
    
    response.push_back(x);
    response.push_back(y);
    response.push_back(z);

    return response;
}

// Working now. To get current board position
void get_current_boards(map<int,vector<int>>* game_status)
{
    magicCube a = magicCube(3);
    a.make_cube_using_map(*game_status);
    a.print_game_cube();
}