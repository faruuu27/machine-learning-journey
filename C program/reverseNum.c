#include<stdio.h>
int rev(int num){
    int reverse=0;
    while(num!=0){
      int digit=num%10;
      reverse=reverse * 10+digit;

      num=num/10;

    }
    return reverse;
}
int main(){
    int n;
    scanf("%d",&n);
    printf("Reverse number: %d",rev(n));
    return 0;
}