#include<iostream>
using namespace std;


int piv(int array[], int begin,int last )
{
    int i=begin,j=last;
  bool temp=false;
  int pivot=last;

while (i<j)
{
    if (temp==false)
    {
        if (array[i]>array[pivot])
        {


           int tempo=array[i];
           array[i]=array[pivot];
           array[pivot]=tempo;

           pivot=i;
           temp=true;
        }
        else 
        {
               i++;
        }
           
    }
    else
    {
        if (array[j]<array[pivot])
        {
            
            int tempo=array[j];
           array[j]=array[pivot];
           array[pivot]=tempo;
            pivot=j;
            temp=false;
        }
        else {
              j--;
        }
             
    }
   


}
return pivot;
}
void quicksort(int array[],int begin,int last)
{
    if (begin >=last)
    {
        return;
    }
    
    int pi=piv(array,begin,last);
quicksort(array,begin,pi-1);
quicksort(array,pi+1,last);

}


int main()
{
    int arr[10]={5,4,3,2,1,0,-1,-2,-3,-4};
    quicksort(arr,0,9);
    for (int i = 0; i < 10; i++)
    {
        cout<<arr[i]<<' ';
    }
    return 0;
    
}
