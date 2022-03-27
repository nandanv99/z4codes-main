#include <conio.h>
#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i,j,k,a=4,b=1,l=1;
    for(i=1;i<=4;i++)
    {
     for(j=1;j<=a;j++)
        printf(" ");
      a--;
      for(k=1;k<=b;k++)
     {
         printf("%d ",l);
         l++;
     }
     b++;
     printf("\n");
    }
    getch();
}