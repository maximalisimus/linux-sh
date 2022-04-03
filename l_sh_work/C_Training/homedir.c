#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <pwd.h>

int main(int argc, char *argv[]) {
    const char *homedir;
    if ((homedir = getenv("HOME")) == NULL) {
        homedir = getpwuid(getuid())->pw_dir;
    }
    printf("%s\n",homedir);
    return 0;
}

/*
    clear && gcc -o homedir homedir.c && ./homedir

    /home/utv
 */
