#include<iostream>
using namespace std;
int main()
{
    int array1[10]={1,2,3,4,5,6,7,8,9,10};
    int array2[4]={1,2,3,4};
    int array3[14];
    int i=0,j=0,c=0;
    while ( i<10 && j<4)
    {
        if(array1[i]<array2[j])
        {
            array3[c]=array1[i];
            i++;
        }
        else{
            array3[c]=array2[j];
            j++;
        }
        c++;
    }
    while (i<10 || j<4)
    {
        if (i<10)
        {
            array3[c]=array1[i];
            i++;
        }
        else if (j<4)
        {
            array3[c]=array2[j];
            j++;
        }
        c++;
    }
    for (int i = 0; i < 14; i++)
    {
        cout<<array3[i]<<' ';
    }
    cout<<'finished'<<endl;
    
    
    return 0;
    
}