#include<iostream>
#include<bits/stdc++.h>
using namespace std;
 
int multisum(int n)
{
    
    int temp=2;
    int integer=2;
    for(int x= 2; x <= n; x++)
    {
        int sum=2;
        for(int j = 1; j*x<= n; j++)
        {
            sum= (j*x) + sum;
        }
        if (sum>temp)
        {
            temp=sum;
            integer=x;
        }
        
        
    }
    return integer;
 
}
int main()
{
    int testcase;
    cin>>testcase;
    while (testcase!=0)
    {
       int number;
       cin>>number;
       int res=multisum(number);
       cout<<res<<endl;
       testcase--;
    }
    return 0;
}