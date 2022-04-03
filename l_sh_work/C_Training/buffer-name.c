#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main( int argc, char * argv [] )
{
    //system("cls");
    
    char pgrep_kill[2][1000] = {"pgrep", "kill"};
    char *programm = "sxhkd";
    char input_command[2][30] = {"-SIGUSR1", "-TERM"};
    char output_command[3][1000];   
    int id_programm = 1084;
    
    //int j = snprintf(outcommand[0],sizeof(outcommand[0]),"%s %s",pgrep_kill[0],programm);
    snprintf(output_command[0],sizeof(output_command[0]),"%s %s",pgrep_kill[0],programm);
    snprintf(output_command[1],sizeof(output_command[1]),"%s %s %i",pgrep_kill[1],input_command[0],id_programm);
    snprintf(output_command[2],sizeof(output_command[2]),"%s %s %i",pgrep_kill[1],input_command[1],id_programm);
    
    printf("%s\n%s\n%s\n",output_command[0],output_command[1],output_command[2]);
    
    strcpy(output_command[0],"");
    strcpy(pgrep_kill[0],"");
    char *str2 = "/usr/bin/pgrep";
    snprintf(pgrep_kill[0],sizeof(pgrep_kill[0]),"%s",str2);
    snprintf(output_command[0],sizeof(output_command[0]),"%s %s",pgrep_kill[0],programm);
    
    strcpy(output_command[1],"");
    strcpy(output_command[2],"");
    strcpy(pgrep_kill[1],"");
    char *str = "/bin/kill";
    snprintf(pgrep_kill[1],sizeof(pgrep_kill[1]),"%s",str);
    snprintf(output_command[1],sizeof(output_command[1]),"%s %s %i",pgrep_kill[1],input_command[0],id_programm);
    snprintf(output_command[2],sizeof(output_command[2]),"%s %s %i",pgrep_kill[1],input_command[1],id_programm);
        
    printf("\n%s\n%s\n%s\n",output_command[0],output_command[1],output_command[2]);
        
    //system("pause");
    return 0;
}
/*
    gcc -o buffer-name buffer-name.c && ./buffer-name
    
    pgrep sxhkd
    kill -SIGUSR1 1084
    kill -TERM 1084
 */
