#include<iostream>
#include<vector>
#include<map>
using namespace std;


bool check_linearity(int x1, int y1, int z1, int x2, int y2, int z2, int x3, int y3, int z3)
{
    double x = x2-x1;
    double y = y2-y1;
    double z = z2-z1;
    
    double x_ = x3-x1;
    double y_ = y3-y1;
    double z_ = z3-z1;

    if(x*y_== y*x_&&z*x_==x*z_)
    {
        return true;
    }
    return false;
}
