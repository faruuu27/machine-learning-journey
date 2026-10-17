#include<stdio.h>


float sum(float a,float b){
    return a+b;
}
int main(){
    float a=4; float b=6;
    printf("%.2f",sum(a,b));
    return 0;
}