#include<iostream>
using namespace std;

int main()
{
    int tes,n,a[100000],ss=0,dn=0,i,j,t;
    cin>>tes;
    for(t=0;t<tes;t++)
    {
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
        }
        for(i=0;i<n;i++)
        {
            cout<<a[i]<<"\t";
        }
    }
return 0;
}