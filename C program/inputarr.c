#include<stdio.h>


int main(){
    int num;
    printf("enter the number of elemts: ");
    scanf("%d",&num);
    int arr[num];

    for(int i=0;i<num;i++){
        printf("enter your %d number: ",i);
        scanf("%d",&arr[i]);
    }
    for(int i=0;i<num;i++){
        printf("%d \n",arr[i]);
    }
    return 0;
}