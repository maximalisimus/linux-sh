#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <pwd.h>
#include <unistd.h>

int main()
{
	const char *homedir;
	if ((homedir = getenv("HOME")) == NULL) {
		homedir = getpwuid(getuid())->pw_dir;
	}
	int hsize = strlen(homedir) + 15;
	char pid_file[hsize];
	sprintf(pid_file,"%s/sxhkd.pid",homedir);
	printf("%s\n",pid_file);
	
	
	
	return 0;
}
/*
	clear && gcc -o loockfile loockfile.c && ./loockfile

	
 */
