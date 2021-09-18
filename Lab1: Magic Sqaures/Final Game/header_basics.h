#include<iostream>
#include<vector>
#include<map>
using namespace std;
#include<math.h>
bool check_linearity(int x1, int y1, int z1, int x2, int y2, int z2, int x3, int y3, int z3);

bool check_linearity(int x1, int y1, int z1, int x2, int y2, int z2, int x3, int y3, int z3)
{
    double ax = x2-x1;
    double ay = y2-y1;
    double az = z2-z1;
    
    double bx = x3-x1;
    double by = y3-y1;
    double bz = z3-z1;


    double cx = x3-x2;
    double cy = y3-y2;
    double cz = z3-z2;

    double a = sqrt(ax*ax+ay*ay+az*az);
    double b = sqrt(bx*bx+by*by+bz*bz);
    double c = sqrt(cx*cx+cy*cy+cz*cz);

    if(a+b>c&&b+c>a&&a+c>b)
    {
        return false;
    }

    
    return true;
}
