#include<stdio.h>

void getName(char name[]){
    printf("Enter your name:  ");
    fgets(name,sizeof(name),stdin);
}
int main(){
    char name[50];

    getName(name);

    printf("hi ,%s",name);

    return 0;
}