#include<stdio.h>

void printarr(int arr[],int size){
    for(int i=0;i<size;i++){
        printf("%d\n",arr[i]);
    }
}

int SumOfArray(int arr[],int size){
    int sum=0;
    for(int i=0;i<size;i++){
        sum+=arr[i];
    }
    return sum;
}

int smallest(int arr[],int size){
    int min=arr[0];
    for(int i=1;i<size;i++){
        if(arr[i]<min){
            min=arr[i];
        }
    }
    return min;
}

int numofeven(int arr[],int size){
    int count=0;
    for(int i=0;i<size;i++){
        if(arr[i]%2==0){
            count++;
        }
    }
    return count;
}

int main(){
    int arr[]={55,23,31,4,6};
    int size=sizeof(arr)/sizeof(arr[0]);
    printarr(arr,size);
    printf("sum of the array is %d\n",SumOfArray(arr,size));
    printf("smallest element in the array is %d\n",smallest(arr,size));
    printf("Number of even number is %d\n",numofeven(arr,size));
    return 0;
}