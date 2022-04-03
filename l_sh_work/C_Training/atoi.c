#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main()
{
	int val;
	char strn1[] = "12546";
 
	val = atoi(strn1);
	printf("String value = %s\n", strn1);
	printf("Integer value = %d\n", val);
 
	char strn2[] = "GeeksforGeeks";
	val = atoi(strn2);
	printf("String value = %s\n", strn2);
	printf("Integer value = %d\n", val);
 
	return (0);
}
/*
	String value = 12546
	Integer value = 12546
	String value = GeeksforGeeks
	Integer value = 0
 */
