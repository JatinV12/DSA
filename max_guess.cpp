#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int maxguess(vector<int>& nums)
{ 
  int max=0,temp=0; 
  for (int i = 0; i < nums.size()-1; i++)
  {
    if (nums[i]>nums[i+1])
    {
         max=nums[i];
    }
    else
    {
         max=nums[i+1];
    }
    
    
    if (max<temp || i==0)
    {
        temp=max;
    }
    
    
  }
  return temp;
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
       vector<int> array;

       for(int i=0 ; i<size ; i++)
       {
           cin>>a;
           array.push_back(a);
       }
        int res= maxguess(array);
        cout<<res-1<<endl;
        testcase--;
    }
    return 0;
    
}