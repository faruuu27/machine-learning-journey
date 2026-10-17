#include<stdio.h>

int factorial(int n){
    if(n==1||n==0){
        return 1;
    }
    return n* factorial(n-1);
}
int main(){
    int num;
    scanf("%d",&num);
    printf("%d\n",factorial(num));
    int n=3; float x=7.3;
    printf("%.2f",n+x);
    return 0;
}