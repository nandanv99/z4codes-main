#include<conio.h>
#include<string.h>
#include<stdio.h>
void main(){
    //length of string 
    char s[] = "Northern India Engineering College";
    int i,j;
    for (i = 0; s[i] != '\0'; ++i);
    printf("String length is : %d \n", i);

    //Reverse a string in c
    for(j = i - 1; j >= 0; j--) {
        printf("Reversed string is :%c", s[j]);
    }
}