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
    // Definition of Chance Value:  -1 => _
    //                               1 => X
    //                               2 => O
    map<int,vector<int>> game_status;

    // Values of first element
    square *current_square = (square*)malloc(sizeof(square)); // Will govern z
    int curr_x; // Will govern x
    int curr_y; // Will govern y
    int curr_z;

    magicCube(int s)
    {
        size = s;
        magic_square_1.initiate_square(size);
        magic_square_1.add_basic_values(-1);
        
        magic_square_2.initiate_square(size);
        magic_square_2.add_basic_values(-1);
        
        magic_square_3.initiate_square(size);
        magic_square_3.add_basic_values(-1);

        magic_square_1.next_sqaure(&magic_square_2);
        magic_square_2.next_sqaure(&magic_square_3);
        magic_square_3.next_sqaure(&magic_square_1);

    }

    void make_magic_cube(int x, int y, int z)
    {
        curr_x = x;
        curr_y = y;
        curr_z = z;
        if(z==0)
        {   
            current_square = &magic_square_1;
        }
        else if(z==1)
        {
            current_square = &magic_square_2;
        }
        else if(z==2)
        {
            current_square = &magic_square_3;
        }

        make_magic_cube(); // Call the no argument make_magic_cube()
    }

    void make_magic_cube()
    {
        
        for(int i=0; i<size*size*size; i++)
        {
            current_square->square_matrix[curr_x][curr_y] = i+1;
            game_status[i+1] = {curr_x, curr_y, curr_z, -1}; // AS -1 meaning blank(_)
            // cout<<curr_x<<", "<<curr_y<<", "<<curr_z<<"--"<<endl;

            curr_x--;
            curr_y--;
            if(curr_x<0)
            {
                curr_x = size + curr_x;
            }
            if(curr_y<0)
            {
                curr_y = size + curr_y;
            }

            if(current_square->square_matrix[curr_x][curr_y]>0)
            {
                // Saving current state in temporary variables
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
                if(current_square->square_matrix[curr_x][curr_y]>0)
                {
                    // Go back to the previous square
                    current_square = current_square->next->next;
                    curr_z--;
                    if(curr_z<0)
                        curr_z = size-1;

                    // Go back to last entry
                    curr_x = tmp_x;
                    curr_y = tmp_y;
                    
                    // One step below in last entry
                    curr_y++;
                    if(curr_y==size)
                        curr_y = 0; 
                    curr_x--;
                    if(curr_x==-1)
                        curr_x = size-1;
                }
            }
        }
    }
    
    void start_game()
    {
        cout<<"Value:  x, y, z, \tChance\n";
        for(auto it = game_status.cbegin(); it!=game_status.cend(); ++it)
        {
            cout<<it->first<<": \t"<<it->second[0]<<", "<<it->second[1]<<", "<<it->second[2]<<", \t"<<it->second[3]<<endl;
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
};
