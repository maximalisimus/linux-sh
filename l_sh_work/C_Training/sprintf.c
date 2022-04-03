/* itoa example */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main ()
{
    int i;
    char buffer [33];
    printf ("Enter a number: ");
    scanf ("%d",&i);
    sprintf(buffer,"%d",i);
    printf ("decimal: %s\n",buffer);
    // memset(buffer,0,33);
    // memset(buffer,0,sizeof(buffer));
    strcpy(buffer,"");
    printf ("buffer =%s\n",buffer);
    return 0;
}
/*
    Enter a number: 1750
    decimal: 1750
    buffer = 
 */
