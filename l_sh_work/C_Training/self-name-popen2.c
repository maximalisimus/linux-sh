#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *cmd(char *command, int length, int wsize);

int main (int argc, char *argv [])
{
	char pgrep_kill[2][1000] = {"pgrep", "kill"};
	char *programm = argv[0];
	char input_command[4][100] = {"-SIGUSR1", "-TERM", "echo", "| rev | cut -d '/' -f1 | rev | xargs"};
	char output_command[4][1000];   
	int id_programm = 1084;

	//snprintf(output_command[0],sizeof(output_command[0]),"%s %s",pgrep_kill[0],programm);
	//snprintf(output_command[1],sizeof(output_command[1]),"%s %s %i",pgrep_kill[1],input_command[0],id_programm);
	//snprintf(output_command[2],sizeof(output_command[2]),"%s %s %i",pgrep_kill[1],input_command[1],id_programm);
	
	snprintf(output_command[3],sizeof(output_command[3]),"%s \"%s\" %s",input_command[2],argv[0],input_command[3]);
	char *icmd = cmd(output_command[3],50,50);
	printf("%s\n%i\n",icmd,sizeof(icmd));
	free(icmd);
	
	return 0;
}

char *cmd(char *command, int length, int wsize)
{
	FILE *fp;
	char path[length];
	
	char *str_out;
	//rez = (char *)malloc(sizeof(char *)*1035);
	//rez = (char *)malloc(wsize);
	str_out = (char *)malloc(wsize);
	
	/* Open the command for reading. */
	fp = popen(command, "r");
	if (fp == NULL) {
		printf("Failed to run command\n" );
		exit(1);
	}

	/* Read the output a line at a time - output it. */
	while (fgets(path, length, fp) != NULL) {
		//snprintf(rez,sizeof(path),"%s",path);
		strcpy(str_out,path);
		//printf("%s", path);
	}

	/* close */
	pclose(fp);
	
	//str_out[strlen(str_out) - 1] = 0;
	char *pos = strrchr(str_out, '\n');
	if (pos)
	{
		str_out[pos-str_out] = 0;
	}
	
	return str_out;
}
/*
	clear && gcc -o self-name-popen2 self-name-popen2.c && ./self-name-popen2
	
	self-name-popen2
	8
 */
