#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h> 

int main( int argc, char *argv[] )
{

    char *comm1 = "clear";
    char *comm2 = "/bin/ls /home/";

     char *comm3 = "/usr/bin/ls";
     char *comm4 = "/home/";

    system("clear");

    FILE *fp;
    char path[1035];

    /* Open the command for reading. */
    fp = popen(comm2, "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        exit(1);
    }

    /* Read the output a line at a time - output it. */
    while (fgets(path, sizeof(path), fp) != NULL) {
        printf("%s", path);
    }

    /* close */
    pclose(fp);

    printf("\n");
    execl(comm3,comm3,comm4,NULL);
    

    return 0;
}
