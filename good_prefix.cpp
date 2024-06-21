#include<iostream>
#include <bits/stdc++.h>

using namespace std;

int prefix(vector<int>& array)
{
    long long  sum=0;
    int max=array[0];
    int integer=0;
 for (int i = 0; i < array.size() ; i++)
 {
    if (max<=array[i])
    {
        max=array[i];
    }
    
    sum =sum+array[i];
    if ((sum-max)==max )
    {
       integer++;
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
       int size;
       cin>>size;
       int a;
       vector<int> number;

       for(int i=0 ; i<size ; i++)
       {
           cin>>a;
           number.push_back(a);
       }
       int result= prefix(number);
       cout<<result<<endl;
       testcase--;
    }
    
    return 0;
    
}