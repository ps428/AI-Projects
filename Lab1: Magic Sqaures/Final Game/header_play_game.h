#include<iostream>
#include<vector>
#include<map>
#include<string>
using namespace std;

#include "header_cube.h"

bool fill(vector<int> move, map<int,vector<int>>* game_status);
void running_game(map<int,vector<int>>* game_status);
void fill_center(map<int,vector<int>>* game_status);
void get_current_boards(map<int,vector<int>> game_status);
void move_pc_ai(map<int,vector<int>>* game_status);
vector<int> get_user_move();

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

    // A variable move count to keep track of moves made in the game
    int move_count = 0;
    
    // User first or mchine first
    int type = 1;//default case for debugging and testing

    // TODO
    cout<<"Welcome to the Tic Tak Toe Blah blah blah";
    
    string name;
    cout<<"Enter you name: ";
    cin>>name;

    char play_first;
    cout<<"Hello "<<name<<" this is an AI. Nice to meet you! Would you like to play first (y->yes or n->no): ";
    cin>> play_first;

    if(play_first=='n')
    {
        type = 1; //Machine first
    }
    if(play_first=='y')
    {
        type = 2;// User first
    }

    while(move_count<27) // Total at max 27 moves possible
    {
        // Being a general AI, check for a vacant center for first two chances        
        // if(type==1&&move_count==0)
        // {
        //     fill_center(game_status);
        // }
        // if(type==2&&move_count==1)
        // {
        //     fill_center(game_status);
        // }    
        
        // Considering only machine first
        if(move_count%2==0) //ML Casse
        {
            // First move, fill center
            if(move_count==0) 
            {
                fill_center(game_status);
            }    
            else
            {
                move_pc_ai(game_status);
            }
        }
        else
        {
            // User input part is done for now
            vector<int> user_move = get_user_move();
            user_move.push_back(2); //For user
            bool filled_or_not = fill(user_move, game_status);
            while(1)
            {
                if(filled_or_not)
                    break;

                
                get_current_boards(*game_status);
                cout<<"\n-------ERROR BLOCK IS ALREADY FILLED------\nPlease enter correct vacant blocks: ";
                user_move = get_user_move();
                user_move.push_back(2); //For user
                filled_or_not = fill(user_move, game_status);
            }             
        } 
        
        printf("You made a nice move, here's the board: \n");
        
        get_current_boards(*game_status);

        move_count++;
    }    
}


void fill_center(map<int,vector<int>>* game_status)
{
    // making a default move to center if it is empty
    vector<int> move = {1,1,1,1}; // Filling center with 1 if it is vacant
    fill(move, game_status);
}

bool fill(vector<int> move, map<int,vector<int>>* game_status)
{
    bool filled_or_not = false;
    for(auto it = game_status->cbegin(); it!= game_status->cend(); it++)
    {
        int x = move[0];
        int y = move[1];
        int z = move[2];
        int chance_made = move[3]; //1 for machine 2 for user

        //If blanka nd queries match, then add the required value
        if(it->second[0]==x&&it->second[1]==y&&it->second[2]==z&&it->second[3]==-1)
        {
            (*game_status)[it->first] = move;
    // cout<<filled_or_not<<"ssssssssss";
            filled_or_not = true;
        }
    }
    return filled_or_not;
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
void get_current_boards(map<int,vector<int>> game_status)
{
    magicCube a = magicCube(3);
    a.make_cube_using_map(game_status);
    a.print_game_cube();
}

void move_pc_ai(map<int,vector<int>>* game_status)
{
    // These three linked lists will hold the keys from hashmap 
    // based on the values filled in their postions on the boards
    vector<int> machine_values;
    vector<int> user_values;
    vector<int> vacant_values;
    bool filled = false; // A bool to check if it is filled or not

    for(auto it = game_status->cbegin(); it!= game_status->cend(); it++)
    {
        int switcher = it->second[3];
        switch (switcher)
        {
        case 1:
            machine_values.push_back(it->first);
            break;

        case 2:
            user_values.push_back(it->first);
            break;

        default:
            vacant_values.push_back(it->first);
            break;
        }
    }
    
    // kind of poss win for machine function and fill if in a winning position
    for(int i=0;i<machine_values.size()-1;i++)
    {
        for(int j=i+1;j<machine_values.size();j++)
        {
            int a = machine_values[i];
            int b = machine_values[j];
            int diff = 42-a-b;
            int vacancy = (*game_status)[diff][3];// To check whether it is vacant or not

            if(vacancy==-1 && diff>=1 && diff<=27)
            {
                vector<int> point1 = (*game_status)[a];
                vector<int> point2 = (*game_status)[b];
                vector<int> point3 = (*game_status)[diff];
                
                int x1 = point1[0];
                int x2 = point2[0];
                int x3 = point3[0];

                int y1 = point1[1];
                int y2 = point2[1];
                int y3 = point3[1];

                int z1 = point1[2];
                int z2 = point2[2];
                int z3 = point3[2];
                
                bool linear_or_not = check_linearity(x1,y1,z1,x2,y2,z2,x3,y3,z3);
                
                if(linear_or_not)
                {
                    vector<int> move = {x3,y3,z3,1}; // Picking the third point
                    filled = fill(move, game_status); // Filling the third point if it is collinear
                    
                    // If returned and successful fill above, then return out of this function else fo further
                    if(filled)
                        return;
                }
            } 
        }
    }

    // Poss win kind of something for user, if user in wiing position, then block it
    for(int i=0;i<user_values.size()-1;i++)
    {
        for(int j=i+1;j<user_values.size();j++)
        {
            int a = user_values[i];
            int b = user_values[j];
            int diff = 42-a-b;
            int vacancy = (*game_status)[diff][3];// To check whether it is vacant or not

            if(vacancy==-1 && diff>=1 && diff<=27)
            {
                vector<int> point1 = (*game_status)[a];
                vector<int> point2 = (*game_status)[b];
                vector<int> point3 = (*game_status)[diff];
                
                int x1 = point1[0];
                int x2 = point2[0];
                int x3 = point3[0];

                int y1 = point1[1];
                int y2 = point2[1];
                int y3 = point3[1];

                int z1 = point1[2];
                int z2 = point2[2];
                int z3 = point3[2];
                
                bool linear_or_not = check_linearity(x1,y1,z1,x2,y2,z2,x3,y3,z3);
                
                // Exact same logic just on user now, if user in winnig position, then fill and block it
                if(linear_or_not)
                {
                    vector<int> move = {x3,y3,z3,1}; // Picking the third point
                    filled = fill(move, game_status); // Filling the third point if it is collinear
                    
                    // If returned and successful fill above, then return out of this function else fo further
                    if(filled)
                        return;
                }
            } 
        }
    }

    // TODO Needs Optimisation
    if(!filled)
    {
        // Pick x,y,z of first vacant point
        vector<int> x = (*game_status)[vacant_values[0]];
        vector<int> move = {x[0],x[1],x[2],1};
        filled = fill(move, game_status);
    }
    // printf("\n\n-------------%d------\n\n",filled);
    // for(int i=0;i<6;i++)
    // {
    //     printf("%d ",machine_values[i]);
    // }
}