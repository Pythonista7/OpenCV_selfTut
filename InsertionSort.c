//Insertion sort - good for a small sample set 



#include<stdio.h>

void in_sort(int arr[],int n)
{   
    int i,j,key;
    //Sorting starts at one because we assume that the 1st element is in sorted position.
    for(i=1;i<n;i++)
    {   
        key=arr[i];
        j=i-1;

        /*The subarray from 0 to j is ofent called the invarient.
          i.e - All the elements of the subarray are always in a sorted order. 
        */
        
        //Here we shift all the elements of subarray until the appropriate position to inset the key arrives.
        while(j>=0 && arr[j]>key)
        {
            arr[j+1]=arr[j];
            j--;
        } 
        arr[j+1]=key;
        
    }    

    //Displaying sorted array
    printf("Sorted array elements:\n\t");
    for(i=0;i<n;i++)
    printf("\t%d",arr[i]);

    return;
}




int main()
{
    int n;
    
    printf("\t\t\tInsertion Sort\n");
    
    printf("\t\tEnter no of elements to sort:\n");
    scanf("%d",&n);
    
    int arr[n];
    printf("\t\t Enter %d elements:\n",n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);   

    }

    printf("\n\t\tSorting.............\n");

    in_sort(arr,n);

    printf("\nEnd\n");
    
    return(0);
}

