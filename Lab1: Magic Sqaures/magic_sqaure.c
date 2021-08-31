#include<stdio.h>
#include<stdlib.h>
void print_matrix(int ** arr, int size);
void make_magic_square(int size, int x, int y );

// IMPORTANT PROPERTY: SUM OF N^2 SQAURE IS N*(N^2+1)/2

// PATTERN OBSERVED: A KIND OF CYCLE, SUCH THAT 
//  * 1 * * *
//  * * 2 * *
//  * * * 3 *
//  * * * * 4
//  5 * * * *

// And then,
//  7 1 * * *
//  * 8 2 * *
//  * * 9 3 *
//  * * * 10 4
//  5 * * * 6

// And
//  7 1 * * 13
//  14 8 2 * *
//  * 15 9 3 *
//  * * 11 10 4
//  5 * * 12 6

// And
//  7 1 * 19 13
//  14 8 2 * 20
//  16 15 9 3 *
//  * 17 11 10 4
//  5 * 18 12 6

// And finally
//  7 1 25 19 13
//  14 8 2 21 20
//  16 15 9 3 22
//  23 17 11 10 4
//  5 24 18 12 6

// So basically, elements are like 5*i+1

void make_magic_square(int size, int x, int y)
{
    int **arr = (int **)malloc(sizeof(int*)*size);
    for (int i=0; i<size; i++)
         arr[i] = (int *)malloc(size * sizeof(int));
         
    int sum = size*(size*size + 1)/2;

    //guessing a random x and y for position of first element i.e. 1
    int beg_pos_x = x;//rand()%size;
    int beg_pos_y = y;//rand()%size;

    // Some variables to be used in loop
    int curr_x=-100;
    int curr_y=-100;
    int iteration = 0;

    for(int i=0;i<size*size;i++)
    {
        if(curr_x==-100 && curr_y==-100)
        {
            curr_x = beg_pos_x;
            curr_y = beg_pos_y;
            iteration++;
        }
        else
        {
            curr_x++;
            curr_y++;
            iteration++;

            // When all numbers of a "category" are printed". With "category", for a 3X3 Magic square, {1,2,3}, {4,5,6}, {7,8,9} are the three categories
            if(iteration==size+1)
            {
                curr_x-=1;
                curr_y-=2;
                iteration=1;
            }

            // To restart loop from 0 if we reach ends
            if(curr_x==size)
            {
                curr_x = 0;
            }
            if(curr_y==size)
            {
                curr_y = 0;
            }
            if(curr_y<0)
            {
                curr_y = size + curr_y ;
                // printf("--%d %d %d\n",curr_x, curr_y, i+1);
            }
            if(curr_x<0)
            {
                curr_x = size + curr_x;
                // printf("--%d %d %d\n",curr_x, curr_y, i+1);

            }
        }
        arr[curr_x][curr_y] = i+1;
        printf("x=%d, y=%d, value=%d, iteration=%d\n",curr_x, curr_y, i+1, iteration);
    }
    print_matrix(arr, size);
}

void print_matrix(int ** arr, int size)
{
    for(int i=0; i<size; i++)
    {
        for(int j=0; j<size; j++)
        {
            printf("%d, ",arr[i][j]);
        }
        printf("\n");
    }
}

int main(void)
{
    int size;
    printf("Enter size of the magic tree: ");
    scanf("%d",&size);
    int x,y;
    printf("Enter the begining position of element 1 {x,y}: ");
    scanf("%d %d", &x, &y);
    make_magic_square(size, x, y);

    return 0;
}