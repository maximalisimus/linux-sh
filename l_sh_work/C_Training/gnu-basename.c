#include <libgen.h>       // for dirname
#include <stdio.h>        // for snprintf
#include <stdlib.h>
#include <string.h>       // for basename
#include <unistd.h>

char *gnu_basename(char *path)
{
	char *base = strrchr(path, '/');
	return base ? base+1 : path;
}

int main (int argc, char *argv [])
{
	printf("Hello World !\n");
	
	
	char *self_name = gnu_basename(argv[0]);
	printf("%s\n",self_name);
	
	return 0;
}

/*
	clear && gcc -D_GNU_SOURCE -o gnu-basename gnu-basename.c && ./gnu-basename
	clear && gcc -o gnu-basename gnu-basename.c && ./gnu-basename
	
	Hello World !
	main
 */
