#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define REZ(...) rez( (3, ##__VA_ARGS__) )

int rez(int a);

#define SUM(a,...) sum( a, (5, ##__VA_ARGS__) )

int sum (a, b)
  int a;
  int b;
{
  return a + b;
}

int main(int argc, char *argv[]) {
	printf("Hello World !\n");
	
	printf("3 + 7 = %d\n", SUM( 3, 7 ) );
	printf("3 + 5 = %d\n", SUM( 3 ) );
	
	printf("sqr (3) = %i\n",REZ());
	printf("sqr (5) = %i\n",REZ(5));
	
	return 0;
}

int rez(int a)
{
	return a*a;
}

/*
	clear && gcc -o macroses macroses.c && ./macroses
	
	Hello World !
	3 + 7 = 10
	3 + 5 = 8
	sqr (3) = 9
	sqr (5) = 25
 */
