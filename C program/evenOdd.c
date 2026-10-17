#include<stdio.h>
void checkOddEven(int n){
     (n%2==0)? printf("its an even number"): printf("its an odd number"); 
}
int main(){
    int num;
    printf("enter your number: ");
    scanf("%d",&num);
    checkOddEven(num);
    return 0;
}