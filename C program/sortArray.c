#include<stdio.h>

void sortArr(int arr[],int size){
    for(int i=0;i<size-1;i++){
        for(int j=i+1;j<size;j++){
            if(arr[i]>arr[j]){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }    
}
int main(){
    int arr[]={4,6,3,2,1};
    sortArr(arr,5);
    for(int i=0;i<5;i++){
        printf("%d-",arr[i]);
    }
    return 0;
}