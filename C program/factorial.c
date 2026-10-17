#include<stdio.h>

int fact(int num){
    int fact=1;
    if(num!=0||num!=1){
        for(int i=1;i<=num;i++){
            fact=fact*i;
        }
    }
    return fact;
}
int main(){
    int num;
    scanf("%d",&num);
    printf("%d",fact(num));
}