#include<iostream>
#include<vector>
using namespace std;



vector< vector< vector<int> > > v(3, vector< vector<int> >(3 , vector<int>(3)));


void print_cube(vector< vector< vector<int> > > v, int m, int n, int l)
{
    cout<<"Content of 3D Vector: "<<endl;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            for(int k=0;k<l;++k){
                cout<<v[i][j][k]<<' ';
            }
            cout<<endl;
        }    
        cout<<endl;
    }
}

void make_cube(vector< vector< vector<int> > > v, int m, int n, int l)
{
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            for(int k=0;k<l;++k){
                v[i][j][k] = 2+i+j*3+4*k;
            }
        }    
    }
}


int main(){
    
    
    int m =3, n=3, l=3;    
    make_cube(v, n,m,l);
    print_cube(v, n,m,l);
    
    
    
    return 0;
}