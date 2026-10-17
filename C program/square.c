#include<stdio.h>
#include<stdbool.h>
int square(int num){
    return num*num;
}
int largest(int a,int b){
    return (a>b)? a:  b;
}
int main(){
    printf("%d\n",square(8));
    printf("%d",largest(9,19));
    return 0;
}