//Example1.c
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define START int main(){
#define END }
#define INTEGER int
#define PRINT(A,B) printf(A,B)


START

    INTEGER n=5;
   
    PRINT("Value of n is %d\n",n);

END

/*
	clear && gcc -o macros2 macros2.c && ./macros2
	
	Value of n is 5
 */
