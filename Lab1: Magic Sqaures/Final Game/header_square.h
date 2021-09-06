#include<iostream>
#include<vector>
#include<map>
using namespace std;

class square
{
    public:
    int size;
    int ** square_matrix;
    square * next = (square*)malloc(sizeof(square));

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
    }

    void initiate_square(int s)
    {
        size = s;
        square_matrix = (int **)malloc(sizeof(int*)*size);
        
        for (int i=0; i<size; i++)
         square_matrix[i] = (int *)malloc(size * sizeof(int));
    }

    void print_square()
    {
        for(int i=0; i<size; i++)
        {
            for(int j=0; j<size; j++)
            {
                printf("%d, ",square_matrix[i][j]);
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
