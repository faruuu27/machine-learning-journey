#include<stdio.h>
void rev(int arr[],int size){
    int start=0;
    int end=size-1;
    while(start<end){
        int temp=arr[start];
        arr[start]=arr[end];
        arr[end]=temp;
        start++;
        end--;

    }
}
int main(){
    int arr[]={3,4,5,6,7};
    int size=5;
    rev(arr,size);
    for(int i=0;i<5;i++){
        printf("%d ",arr[i]);
    }
    return 0;
}