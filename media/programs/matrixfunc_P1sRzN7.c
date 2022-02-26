#include<stdio.h>
#include <string.h>
void matrixadd();
void matrixsub();
void matrixmulti();
void matrixtranspose(int z);
int mat1[20][20],mat2[20][20],sum[100][100],sub[100][100],result[100][100],transpose[100][100],row1,row2,col1,col2,i,j,temp,tr;
void main(){
    
    // char rerun,rerunprog,result1='Y';
    printf("Enter the row & column for matrix :");
    printf("\nRow :");
    scanf("%d",&row1);
    printf("Column :");
    scanf("%d",&col1);
    
    
// ===============================================================================================================================================================================
    // matrix 1 input :
    printf("\nEnter matrix 1 values : \n");
    for(i=0;i<row1;i++){
        for(j=0;j<col1;j++){
            printf("enter : %d,%d :" ,i+1,j+1);
            scanf("%d",&mat1[i][j]);
        }
    }
    printf("\nEntered matrix is (1) : \n");
    for(i=0;i<row1;i++){
        for(j=0;j<col1;j++){
            printf("%d \t",mat1[i][j]);
        }
        printf("\n");
    }

// ===============================================================================================================================================================================
    // matrix 2 input :
    printf("\nEnter matrix 2 values : \n");
    for(i=0;i<row1;i++){
        for(j=0;j<col1;j++){
            printf("enter : %d,%d :" ,i+1,j+1);
            scanf("%d",&mat2[i][j]);
        }
    }
    printf("\nEntered matrix is (2) : \n");
    for(i=0;i<row1;i++){
        for(j=0;j<col1;j++){
            printf("%d \t",mat2[i][j]);
        }
        printf("\n");
    }

// ===============================================================================================================================================================================

    printf("These are the main functions which you can perform :  \n\n");
    printf("Enter __ 1 __ to add two matrix \n");
    printf("Enter __ 2 __ to substract two matrix  \n");
    printf("Enter __ 3 __ to multiply two matrix  \n");
    printf("Enter __ 4 __ to check wether its transpose or not  \n");
    printf("note : At one time only one function will run.  \n\n");
    printf("enter here :");
    scanf("%d",&temp);
    if(temp==1){
        printf("1 is working lets add ___ ");
        matrixadd();
    }else if(temp==2){
        printf("2 is working lets sub ___ ");
        matrixsub();
    }else if(temp==3){
        printf("3 is working lets multiply ___ ");
        matrixmulti();
    }else if(temp==4){
        printf("4 is working lets check is this transpose or not ___ \n");
        printf("which matrix you want to transpose: ");
        scanf("%d",&tr);
        matrixtranspose(tr);
    }
    
    
}

void matrixadd(){
    for (i = 0; i < row1; ++i)
    for (j = 0; j < col1; ++j) {
      sum[i][j] = mat1[i][j] + mat2[i][j];
    }
    
    printf("\nSum of two matrices: \n");
    for (i = 0; i < row1; ++i)
    for (j = 0; j < col1; ++j) {
      printf("%d   ", sum[i][j]);
      if (j == col1 - 1) {
        printf("\n");
      }
    }
}

void matrixsub(){
    for (i = 0; i < row1; ++i)
    for (j = 0; j < col1; ++j) {
      sum[i][j] = mat1[i][j] - mat2[i][j];
    }
    
    printf("\nSub of two matrices: \n");
    for (i = 0; i < row1; ++i)
    for (j = 0; j < col1; ++j) {
      printf("%d   ", sub[i][j]);
      if (j == col1 - 1) {
        printf("\n");
      }
    }
}
void matrixmulti(){
    for(int i=0; i < 3; i++)
        {
        for(int j=0; j < 3; j++)
        {
          result[i][j] = 0; // assign 0
          // find product
          for (int k = 0; k < 3; k++)
          result[i][j] += mat1[i][k] * mat2[k][j];
        }
    }
    printf("\nMultiplication of two matrices: \n");
    for(i=0;i<row1;i++){
        for(j=0;j<col1;j++){
            printf("%d \t",result[i][j]);
        }
        printf("\n");
    }
}
void matrixtranspose(int z){
    if(z==1){
        for (int i = 0; i < row1; ++i)
        for (int j = 0; j < col1; ++j) {
            transpose[i][j] = mat1[j][i];
        }
        
        printf("\ntranspose of 1 martix is :\n");
        for(i=0;i<row1;i++){
            for(j=0;j<col1;j++){
                printf("%d \t",transpose[i][j]);
            }
            printf("\n");
        }
    }else if(z==2){
        for (int i = 0; i < row1; ++i)
        for (int j = 0; j < col1; ++j) {
            transpose[i][j] = mat2[j][i];
        } 
        
        printf("\ntranspose of 2 martix is :\n");
        for(i=0;i<row1;i++){
            for(j=0;j<col1;j++){
                printf("%d \t",transpose[i][j]);
            }
            printf("\n");
        }
    }
}