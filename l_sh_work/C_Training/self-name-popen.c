#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

//char *cmd(char *command, int wsize);
//char *cmd(char *command, char *str);
char *cmd(char *command, char *str, int length);

int main (int argc, char *argv [])
{
	char pgrep_kill[2][1000] = {"pgrep", "kill"};
	char *programm = argv[0];
	char input_command[4][100] = {"-SIGUSR1", "-TERM", "echo", "| rev | cut -d '/' -f1 | rev"};
	char output_command[4][1000];   
	int id_programm = 1084;

	//snprintf(output_command[0],sizeof(output_command[0]),"%s %s",pgrep_kill[0],programm);
	//snprintf(output_command[1],sizeof(output_command[1]),"%s %s %i",pgrep_kill[1],input_command[0],id_programm);
	//snprintf(output_command[2],sizeof(output_command[2]),"%s %s %i",pgrep_kill[1],input_command[1],id_programm);
	
	snprintf(output_command[3],sizeof(output_command[3]),"%s \"%s\" %s",input_command[2],argv[0],input_command[3]);
	//char *icmd = cmd(output_command[3],100);
	//char *icmd = cmd(output_command[3],programm);
	char *icmd = cmd(output_command[3],programm,100);
	printf("%s\n",icmd);
	free(icmd);
	return 0;
}
//char *cmd(char *command, int wsize)
//char *cmd(char *command, char *str)
char *cmd(char *command, char *str, int length)
{
	FILE *fp;
	//char path[1035];
	//char path[wsize];
	char path[length];
	
	//char rez[1035];
	char *rez;
	//rez = (char *)malloc(sizeof(char *)*1035);
	//rez = (char *)malloc(wsize);
	rez = (char *)malloc(strlen(str)+1);
	
	/* Open the command for reading. */
	fp = popen(command, "r");
	if (fp == NULL) {
		printf("Failed to run command\n" );
		exit(1);
	}

	/* Read the output a line at a time - output it. */
	while (fgets(path, sizeof(path), fp) != NULL) {
		//snprintf(rez,sizeof(path),"%s",path);
		strcpy(rez,path);
		//printf("%s", path);
	}

	/* close */
	pclose(fp);
	//printf("%s\n",rez);
	return rez;
}
/*
	clear && gcc -o self-name-popen self-name-popen.c && ./self-name-popen
	
	self-name-popen
 */
