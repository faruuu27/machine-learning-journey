#include<stdio.h>


int main(){
    int choice;

    do{
        printf("Calculator Menu: \n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d",&choice);
        int a,b;
        if(choice<=4 && choice>=1){
            
            printf("enter your first number: ");
            scanf("%d",&a);
            printf("enter your second number: ");
            scanf("%d",&b);
        }

        switch(choice){
            case 1:
                printf("Result : %d \n",a+b);
                break;
            case 2:
                printf("Result : %d \n",a-b);
                break;
            case 3:
                printf("Result : %d \n",a*b);
                break;
            case 4:
                if (b!=0){
                    printf("Result : %d \n",a/b);
                }else{
                    printf("Division by zero is not possbile");
                }
                break;
            default:
                printf("Invalid choice\n");

        }


    }while(choice!=5);
    return 0;

}