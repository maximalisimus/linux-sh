#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{

	int i = 0;
	FILE *fp = fopen("output.txt","w"); 
	// Return if could not open file
	if (fp == NULL)
		return 0; 
	char string[] = "good bye", received_string[20];
	for (i = 0; string[i]!='\0'; i++) 
		// Input string into the file
		// single character at a time
		fputc(string[i], fp); 
	fclose(fp);
	fp = fopen("output.txt","r"); 
	// Reading the string from file
	fgets(received_string,20,fp);
	printf("%s", received_string); 
	fclose(fp);

	return 0;
}
/*
	clear && gcc -o fputc-fgetc fputc-fgetc.c && ./fputc-fgetc

	good bye
 */
