#include<iostream>
#include<vector>
#include<map>
using namespace std;

#include "header_square.h"

class magicCube{
    public:
    int size;
    // Squares having the values from any magic square
    square magic_square_1;
    square magic_square_2;
    square magic_square_3;

    // Assuming that we have a perfect magical cube,
    // Map such that Map:- Numerical Value:->{x,y,z, Chance_value(X,O,_)}
    // Definition of Chance Value:  -1 => _   //vacant
    //                               1 =>  O   // played by machine
    //                               2 =>  X // played by user
    map<int,vector<int>> game_status;

    // Values of first element
    square *current_square = (square*)malloc(sizeof(square)); // Will govern z
    int curr_x; // Will govern x
    int curr_y; // Will govern y
    int curr_z;

    //METHODS USED
    // magicCube(int s);
    // void make_magic_cube(int x, int y, int z);
    // void make_magic_cube();
    // void start_game();
    // map<int,vector<int>>* get_game_status();
    // void make_cube_using_map(map<int,vector<int>> game_status_passed);
    // void print_cube();
    // void print_game_cube();

    magicCube(int s)
    {
        size = s;
        magic_square_1.initiate_square(size);
        magic_square_1.add_basic_values(-1);
        
        magic_square_2.initiate_square(size);
        magic_square_2.add_basic_values(-1);
        
        magic_square_3.initiate_square(size);
        magic_square_3.add_basic_values(-1);

        magic_square_1.next_sqaure(&magic_square_2); //linking 1 to 2 
        magic_square_2.next_sqaure(&magic_square_3); //linking 2 to 3
        magic_square_3.next_sqaure(&magic_square_1); //linking 3 to 1

    }

    void make_magic_cube(int x, int y, int z)
    {
        curr_x = x;  //current positions
        curr_y = y;
        curr_z = z;
        if(z==0)  //means the top most layer
        {   
            current_square = &magic_square_1;
        }
        else if(z==1) //means the second layer
        {
            current_square = &magic_square_2;
        }
        else if(z==2) //means the third layer
        {
            current_square = &magic_square_3;
        }

        make_magic_cube(); // Call the no argument make_magic_cube()
    }

    void make_magic_cube()
    {
        
        for(int i=0; i<size*size*size; i++)
        {
            // 2d pointer integer matrix
            current_square->square_matrix[curr_x][curr_y] = i+1; // is 1 for first iteration, allocating numbers
            
            // Hash map for game record
            game_status[i+1] = {curr_x, curr_y, curr_z, -1}; // AS -1 meaning blank(_)
            
            // for debugging
            // cout<<curr_x<<", "<<curr_y<<", "<<curr_z<<"--"<<endl;

            curr_x--;   // here the same process of moving north west
            curr_y--;
            if(curr_x<0)
            {
                curr_x = size + curr_x;   // if after subtraction terms turn negative, then add size to go in a cyclic way
            }
            if(curr_y<0)
            {
                curr_y = size + curr_y;     // if after subtraction terms turn negative, then add size to go in a cyclic way
            }
            //general case would be when northwest is vacant: case1 (eg: going 1 to 2)
            if(current_square->square_matrix[curr_x][curr_y]>0)  //bcuz intially -1, when northwest is filled :case2 (eg: going 3 to 4), 
            {
                // Saving current state in temporary variables to return back if case 3 is observed
                square * tmp_square = (square*)malloc(sizeof(square));
                tmp_square = current_square;
                int tmp_x = curr_x;
                int tmp_y = curr_y;
                int tmp_z = curr_z;

                // Go to next square
                curr_z++;
                if(curr_z==size)
                    curr_z = 0;

                current_square = current_square->next;
                curr_x--; // One step up in next square
                if(curr_x<0)
                {
                    curr_x = size + curr_x;
                }
                if(curr_y<0)
                {
                    curr_y = size + curr_y;
                }
                if(current_square->square_matrix[curr_x][curr_y]>0)   //case 3 (eg going 9 to 10) , checking second time
                {
                    // Go back to the previous square
                    current_square = current_square->next->next;  //returning back to the square we started with
                    curr_z--;
                    if(curr_z<0)
                        curr_z = size-1;

                    // Go back to last entry
                    curr_x = tmp_x;
                    curr_y = tmp_y;
                    
                    // One step below in last entry
                    curr_y++;
                    if(curr_y==size)
                        curr_y = 0; //cyclic
                    curr_x--;
                    if(curr_x==-1)
                        curr_x = size-1;
                }
            }
        }
    }
    
    void start_game()
    {  //prints the whole big table
        cout<<"Value:  x, y, z, \tChance\n";
        for(auto it = game_status.cbegin(); it!=game_status.cend(); ++it)  //game_status is a hashmap in the class magic_cube
        {
            cout<<it->first<<": \t"<<it->second[0]<<", "<<it->second[1]<<", "<<it->second[2]<<", \t"<<it->second[3]<<endl;
        }
    }

    map<int,vector<int>>* get_game_status()
    {
        return &game_status;  //returns the address of the hashmap
    }

    void make_cube_using_map(map<int,vector<int>> game_status_passed)
    {
        for(auto it = game_status_passed.cbegin(); it!= game_status_passed.cend(); it++)
        {
            int x = it->second[0];
            int y = it->second[1];
            int z = it->second[2];
            char value;

            if(it->second[3]==-1)
            {
                value = '_';
            }
            else if(it->second[3]==1)
            {
                value = 'O';
            }
            else
            {
                value = 'X';
            }

            if(z==0)
            {
                current_square = &magic_square_1;
            }
            else if(z==1)
            {
                current_square = &magic_square_2;
            }
            else
            {
                current_square = &magic_square_3;
            }
            
            current_square->game_matrix[x][y] = value;

        }
    }

    void print_cube()
    {
        cout<<endl<<"Square 1 is: "<<endl;
        magic_square_1.print_square();
        cout<<endl<<"Square 2 is: "<<endl;
        magic_square_2.print_square();
        cout<<endl<<"Square 3 is: "<<endl;
        magic_square_3.print_square();
        cout<<endl;
    }

    void print_game_cube()
    {
        cout<<endl<<"Square 1 is: "<<endl;
        magic_square_1.print_game_matrix();
        cout<<endl<<"Square 2 is: "<<endl;
        magic_square_2.print_game_matrix();
        cout<<endl<<"Square 3 is: "<<endl;
        magic_square_3.print_game_matrix();
        cout<<endl;
    }
};

