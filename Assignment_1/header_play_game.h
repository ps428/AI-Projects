#include<iostream>
#include<vector>
#include<map>
#include<string>
using namespace std;

#include "header_cube.h"

void running_game(map<int,vector<int>>* game_status);
void fill_center(map<int,vector<int>>* game_status);
bool fill(vector<int> move, map<int,vector<int>>* game_status);
vector<int> get_user_move();
void get_current_boards(map<int,vector<int>> game_status);
void move_pc_ai(map<int,vector<int>>* game_status);
void print_map(map<int,vector<int>> game_status);
void print_map_user(map<int,vector<int>> game_status);
void print_map_machine(map<int,vector<int>> game_status);
vector<int> print_total_score(map<int,vector<int>> game_status);

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
    vector<int> score;
    // type defines user first or machine first
    int type = 1;//machine first: default case for debugging and testing

    // TODO
    cout<<"\nWelcome to the 3-D Tic Tak Toe!";
    
    string name;
    cout<<"\nEnter you name: ";
    cin>>name;

    char play_first;
    cout<<"\nHello "<<name<<" this is an AI. Nice to meet you! Would you like to play first (y->yes or n->no): ";
    cin>> play_first;  //CONDITION TO play first yes/no

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
        if(type==1)
        {
            if(move_count%2==0) //ML Case,  every even chance will be of machine only as machine is starting, starting count from zero
            {
                // First move, fill center
                if(move_count==0) 
                {
                    fill_center(game_status);   //machine always moves in the centre only
                }    
                else
                {
                    move_pc_ai(game_status);
                }

                printf("\nYou made a nice move, here's the board: \n");
                
                // // Can comment these
                get_current_boards(*game_status);
                // // print_map(*game_status);
                // Uncomment these
                // print_map_machine(*game_status);
                // print_map_user(*game_status);
            }
            else
            {
                // User input part is done for now
                vector<int> user_move = get_user_move();
                user_move.push_back(2); //For user, user will always use X and i.e. 2
                // cout<<"\n\n-<<<----"<<user_move[3]<<"-----\n\n";
                bool filled_or_not = fill(user_move, game_status);
                while(1)
                {
                    if(filled_or_not)
                        break;

                    // uncomment
                    get_current_boards(*game_status);
                    cout<<"\n-------ERROR BLOCK IS ALREADY FILLED------\nPlease enter correct vacant blocks: ";
                    user_move = get_user_move();
                    user_move.push_back(2); //For user
                    filled_or_not = fill(user_move, game_status);
                }             
            }  
   
        }
        // user first
        if(type==2) 
        {
            if(move_count%2==1) //ML Casse
            {
                // First move, fill center
                // Resolved: TO-DO Error here in case 2, human first..
                // Reason, due to no value in machine's list, we are unable to iterate over the elements
                // In other cases, one element was there at centre
                // So error when human occupies the centre first
                if(move_count==1) 
                {
                    fill_center(game_status);
                }    
                else
                {
                    move_pc_ai(game_status);
                }

                printf("\nYou made a nice move, here's the board: \n");
                
                // // Can comment these
                get_current_boards(*game_status);
                // // print_map(*game_status);
                // print_map_machine(*game_status);
                // print_map_user(*game_status);
            }
            else
            {
                // User input part is done for now
                vector<int> user_move = get_user_move();
                user_move.push_back(2); //For user
                // cout<<"\n\n-<<<----"<<user_move[3]<<"-----\n\n";
                bool filled_or_not = fill(user_move, game_status);
                while(1)
                {
                    if(filled_or_not)
                        break;

                    // uncomment
                    get_current_boards(*game_status);
                    cout<<"\n-------ERROR! THIS BLOCK IS ALREADY FILLED------\nPlease enter correct vacant blocks: ";
                    user_move = get_user_move();
                    user_move.push_back(2); //For user
                    filled_or_not = fill(user_move, game_status);
                }             
            }  

        }

        if(move_count>=6)  //will display only after 6 moves AS SHOULD BE 3 MOVES EACH TO MAKE A LINE
        {
            score = print_total_score(*game_status);

            if(score[0]>=10)
            {
                cout<<"\n---------------------\nAI Won! Nice game.";
                cout<<"\nFINAL SCOREBOARD IS: ";
                print_total_score(*game_status);
                return;
            }
            if(score[1]>=10)
            {
                cout<<"\n---------------------\nCongrats! You Won "<<name<<"! Nice game.";
                cout<<"\nFINAL SCOREBOARD IS: ";
                print_total_score(*game_status);
                return;
            }

        }
        move_count++;
    }    

    cout<<"\n----------------------";
    cout<<"\n----------------------";
    if(score[0]<10 && score[1]<10)  //score[0] :machine score  and score[1]: user score
    {
        cout<<"\n------------------------\nDRAW!\n";
        cout<<"\nFINAL SCOREBOARD IS: ";
        print_total_score(*game_status);
    }

}


void fill_center(map<int,vector<int>>* game_status)
{
    // making a default move to center if it is empty
    vector<int> move = {1,1,1,1}; // Filling center with 1 bcuz by machine , 111 is the centre cell 
    bool test = fill(move, game_status);
    if(!test)
    {
        move = {2,2,2,1};   //optimal corner, all corners are optimal
        fill(move,game_status);
    }
}

bool fill(vector<int> move, map<int,vector<int>>* game_status)
{
    bool filled_or_not = false;
    for(auto it = game_status->cbegin(); it != game_status->cend(); it++)
    {
        int x = move[0];
        int y = move[1];
        int z = move[2];
        int chance_made = move[3]; //1 for machine 2 for user

        //If blanks and queries match, then add the required value
        if(it->second[0]==x && it->second[1]==y && it->second[2]==z && it->second[3]==-1) //second is inbuilt for the values, if we do first then it will give the key
        {
            (*game_status)[it->first] = move;  //fill key with this value of move
            filled_or_not = true;
        }
    }
    return filled_or_not;
}

vector<int> get_user_move()
{
    vector<int> response;

    int x,y,z;
    cout<<"\nEnter (x,y,z) for your moves: ";
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
//Either I will win, I will block the opponent or I will play the most appropriate (make_two). Both machine and user think this way.
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
        int switcher = it->second[3];   // for checking O,X,_
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
    for(int i=0;i<machine_values.size()-1;i++)   //machine_values.size()-1 bcuz j is i+1
    {

        for(int j=i+1;j<machine_values.size();j++)
        {
            int a = machine_values[i];
            int b = machine_values[j];
            int diff = 42-a-b;

            // VERY VERY IMPORTANT, GO RO CHECKING FOR DIFF IN HASH MAP 
            // ONLY IF THE VALUE OF DIFF IS FROM 1 TO 27 ELSE THERE WOULD BE SEGMENTATION ERROR
            if(diff>=1 && diff<=27)
            {               
                /// THIS IS VERY VERY IMPORTANT TO BE DONE AFTER CHEKCING THE VALUES OF DIFF 
                int vacancy = (*game_status)[diff][3];// To check whether it is vacant or not
                // printf("-----%d------\n",vacancy);

                if(vacancy==-1)
                {
                    vector<int> point1 = (*game_status)[a];
                    vector<int> point2 = (*game_status)[b];
                    vector<int> point3 = (*game_status)[diff];  // 4 values copied to point1,2,3
                    
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
    }

    // Poss win kind of something for user, if user in winning position, then block it

    //checking the third cell with sum 42 ,vacany, collinearity
    for(int i=0;i<user_values.size()-1;i++)
    {
        for(int j=i+1;j<user_values.size();j++)
        {
            int a = user_values[i];
            int b = user_values[j];
            int diff = 42-a-b;
            if(diff>=1 && diff<=27)
            {
                int vacancy = (*game_status)[diff][3];// To check whether it is vacant or not
                // printf("-----%d------\n",vacancy);

                if(vacancy==-1)
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
                    
                    // Exact same logic just on user now, if user in winning position, then fill and block it
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
    }

    int i=0;
    //randomized fill
    while(!filled)
    {
        // Pick x,y,z of first vacant point
        vector<int> x = (*game_status)[vacant_values[i]]; //first vacant value
        vector<int> move = {x[0],x[1],x[2],1};  // 1 again bcuz machine chance
        filled = fill(move, game_status);   // to link key with this move vector in hashmap

        // printf("\n\n-------RAndom fill-------\n\n");
    }
    // printf("\n\n-------------%d------\n\n",filled);
    // for(int i=0;i<6;i++)
    // {
    //     printf("%d ",machine_values[i]);
    // }
}

void print_map(map<int,vector<int>> game_status)
{
    cout<<"Value:  x, y, z, \tChance\n";
    for(auto it = game_status.cbegin(); it!=game_status.cend(); ++it)
    {
        cout<<it->first<<": \t"<<it->second[0]<<", "<<it->second[1]<<", "<<it->second[2]<<", \t"<<it->second[3]<<endl;
    }
}

void print_map_user(map<int,vector<int>> game_status)
{
    cout<<"\nUSER MOVES\n";
    cout<<"Value:  x, y, z, \tChance\n";
    for(auto it = game_status.cbegin(); it!=game_status.cend(); ++it)
    {
        if(it->second[3]==2)
        cout<<it->first<<": \t"<<it->second[0]<<", "<<it->second[1]<<", "<<it->second[2]<<", \t"<<it->second[3]<<endl;
    }
}

void print_map_machine(map<int,vector<int>> game_status)
{
    cout<<"\nMACHINE MOVES\n";
    cout<<"Value:  x, y, z, \tChance\n";
    for(auto it = game_status.cbegin(); it!=game_status.cend(); ++it)
    {
        if(it->second[3]==1)
        cout<<it->first<<": \t"<<it->second[0]<<", "<<it->second[1]<<", "<<it->second[2]<<", \t"<<it->second[3]<<endl;
    }
}

vector<int> print_total_score(map<int,vector<int>> game_status)
{
    int user_score = 0;
    int machine_score = 0;
    vector<int> machine_values;
    vector<int> user_values;
    vector<int> vacant_values;

    for(auto it = game_status.cbegin(); it!= game_status.cend(); it++)
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

    for(int i=0;i<user_values.size()-2;i++)   //atleast 3 values so 3 loops
    {
        for(int j=i+1;j<user_values.size()-1;j++)
        {
            for(int k = j+1; k<user_values.size(); k++)
            {
                int a = user_values[i];
                int b = user_values[j];
                int c = user_values[k];
                if(a+b+c==42)
                {
                    vector<int> point1 = (game_status)[a];
                    vector<int> point2 = (game_status)[b];
                    vector<int> point3 = (game_status)[c];

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
                        user_score++;   //when collinear and sum is 42 increment user score
                    } 
                }
            }
        }
    }
// how many triplets each for user or machine
for(int i=0;i<machine_values.size()-2;i++)
    {
        for(int j=i+1;j<machine_values.size()-1;j++)
        {
            for(int k = j+1; k<machine_values.size(); k++)
            {
                int a = machine_values[i];
                int b = machine_values[j];
                int c = machine_values[k];
                if(a+b+c==42)
                {
                    vector<int> point1 = (game_status)[a];
                    vector<int> point2 = (game_status)[b];
                    vector<int> point3 = (game_status)[c];

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
                            // printf("\n%d, %d, %d => %d\n",x1,y1,z1,a);
                            // printf("\n%d, %d, %d => %d\n",x2,y2,z2,b);
                            // printf("\n%d, %d, %d => %d\n",x3,y3,z3,c);
                        machine_score++;
                    }
                }
            }
        }
    }

    vector<int> score = {machine_score, user_score};

    // same for machine

    cout<<"\n-----------------------------------------------\nSCOREBOARD\nUser(X): ";
    cout<<user_score<<"\nMachine(O): "<<machine_score<<"\n";

    return score;


}
