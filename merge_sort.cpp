#include<iostream>
using namespace std;

void merge(int array[],int  begin,int  mid,int  end)
{
   int* leftarray= new int[mid+1-begin];
   int f=0;
   for (int i = begin; i <= mid; i++)
   {
     leftarray[f++]=array[i];
   }
   for (int i = 0; i < mid+1-begin; i++)
    {
       cout<<leftarray[i]<<" ";
    }
    cout<<endl;
   int* rightarray= new int[end-mid];
   int g=0;
   for (int i = mid+1 ; i <= end; i++)
   {
    rightarray[g++]=array[i];
   }
   for (int i = 0; i < end-mid; i++)
    {
       cout<<rightarray[i]<<" ";
    }
    cout<<endl;
    int i=0,j=0,c=begin;
    while ( i<mid-begin+1  && j<end - mid)
    {
        if(leftarray[i]<rightarray[j])
        {
            array[c]=leftarray[i];
            i++;
        }
        else{
            array[c]=rightarray[j];
            j++;
        }
        c++;
    }
    
    while (i<mid-begin+1 || j<end-mid)
    {
        if (i<mid-begin+1)
        {
            array[c]=leftarray[i];
            i++;
        }
        else if (j<end-begin)
        {
            array[c]=rightarray[j];
            j++;
        }
        c++;
    }
   delete[] leftarray;
   delete[] rightarray;
}

void mergeSort(int array[], int begin, int  end)
{
    cout<<"subarray ["<<begin<<","<<end<<"] "<<endl;
    if (begin >= end)
        return;

    int mid = (begin + end)/ 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin,mid, end);
}

int main()
{
    int size;
    cout<<"enter size of array"<<endl;
    cin>>size;
    int array[size];
    cout<<"enter elements of array"<<endl;
    for (int i = 0; i < size; i++)
    {
       cin>>array[i];
    }
    mergeSort(array,0,size-1);
    for (int i = 0; i < size; i++)
    {
       cout<<array[i]<<" ";
    }
    return 0;
}