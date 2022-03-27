#include <stdio.h>

struct book
{
  int pages;
  char author[10];
  float price;
} a;

void main ()
{
    struct book *p;
    printf("Input data :\n");
    scanf("%d %s %f",&a.pages,a.author,&a.price);
    p=&a;
    printf("Display the record :\n");
    printf("%d %s %f",p->pages,p->author,p->price);
}
