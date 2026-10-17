#include<stdio.h>
void checkLeap(int year){
    if((year%400==0)||(year%4==0 && year%100!=0)){
        printf("its a leap year");
    }else{
        printf("its not a leap year");
    }
}
int main(){
    int year;
    printf("enter the year: ");
    scanf("%d",&year);
    checkLeap(year);
    return 0;
}