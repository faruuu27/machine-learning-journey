
#include<stdio.h>

void merge(int arr1[],int arr2[],int size1,int size2,int arr3[]){
        for(int i=0;i<size1;i++){
            arr3[i]=arr1[i];
        }
        for(int i=0;i<size2;i++){
            arr3[i+size1]=arr2[i];
        }
}
int main(){
    int arr1[]={1,2,3,4};
    int arr2[]={5,6,7,8};
    int size1=sizeof(arr1)/sizeof(arr1[0]);
    int size2=sizeof(arr2)/sizeof(arr2[0]);
    int arr3[size1+size2];
    merge(arr1,arr2,size1,size2,arr3);
    for(int i=0;i<size1+size2;i++){
        printf("%d\n",arr3[i]);
    }
    return 0;
}