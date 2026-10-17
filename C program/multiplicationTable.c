#include<stdio.h>
//print
int main(){
    int num,ans;
    printf("enter your number: ");
    scanf("%d",&num);

    for(int i=0;i<=10;i++){
        ans=num*i;
        printf("%d x %d = %d\n", i,num,ans);
    }
    return 0;
}