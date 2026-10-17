#include<stdio.h>


int main(){
    int sum=0,num;
    int i=0;
    printf("enter your number: ");
    scanf("%d",&num);

    while(i<=num){
        if(i==3){
            i++;
            continue;
        }
        sum+=i;
        i++;
        
        printf("%d\n",sum);
    }

    

    return 0;

}