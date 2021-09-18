#include<iostream>
#include<vector>
#include<map>
using namespace std;

class square
{
    public:
    int size;
    int ** square_matrix;
    char ** game_matrix;
    square * next = (square*)malloc(sizeof(square));

    square();
    square(int s);


    square()
    {
        // Defualt constructor
    }

    square(int s)
    {
        size = s;
        
        square_matrix = (int **)malloc(sizeof(int*)*size);
        
        for (int i=0; i<size; i++)
            square_matrix[i] = (int *)malloc(size * sizeof(int));

        game_matrix = (char **)malloc(sizeof(char*)*size);
        
        for (int i=0; i<size; i++)
            game_matrix[i] = (char *)malloc(size * sizeof(char)); 
    }

    void initiate_square(int s) // Looks redundant but useful when a square is initiated with unknown size..so important
    {
        size = s;
        square_matrix = (int **)malloc(sizeof(int*)*size);
        
        for (int i=0; i<size; i++)
            square_matrix[i] = (int *)malloc(size * sizeof(int));

        game_matrix = (char **)malloc(sizeof(char*)*size);
        
        for (int i=0; i<size; i++)
            game_matrix[i] = (char *)malloc(size * sizeof(char)); 
    }

    void print_square()
    {
        for(int i=0; i<size; i++)
        {
            for(int j=0; j<size; j++)
            {
                cout<<square_matrix[i][j]<<" ";
                // printf("%d, ",square_matrix[i][j]);
            }
            printf("\n");
        }
    }
    void print_game_matrix()
    {
        for(int i=0; i<size; i++)
        {
            for(int j=0; j<size; j++)
            {
                cout<<game_matrix[i][j]<<" ";
                // printf("%d, ",square_matrix[i][j]);
            }
            printf("\n");
        }
    }

    void add_basic_values(int n)
    {
        for(int i=0; i<size; i++)
        {
            for(int j=0; j<size; j++)
            {
                square_matrix[i][j] = -1;
            }
        }
    }

    void next_sqaure(square * next_sq)
    {
        next = next_sq;
    }

};
