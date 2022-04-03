#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int main( int argc, char * argv [] )
{
	system("clear");
	int wsize=0;
	for (int i=1; i<argc; i++)
	{
		if (strlen(argv[i]) > wsize)
		{
			wsize = strlen(argv[i]);
		}
	}
	printf("argc = %i\n",argc);
	printf("maxsize = %i\n",wsize);
	char tmp[argc-1][wsize];
	for (int i=1; i<argc; i++)
	{
		//wsize=strlen(argv[i]);
		strcpy(tmp[i-1],argv[i]);
		//strncpy(tmp[i-1],argv[i],wsize);
	}
	printf("argc = %i, argv = ", argc);
	for (int i=0; i<argc-1; i++)
	{
		printf(" %s",tmp[i]);
	}
	printf("\n");
	//free(tmp);
	//free(wsize);
	return 0;
}
