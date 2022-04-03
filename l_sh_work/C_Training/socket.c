#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <errno.h>
#include <string.h>
#include <sys/poll.h>
#include <unistd.h>

extern int errno;

#define SOCKET_NAME "THERE_ARE_SUPER_PUPER_SOCKET_HERE"
#ifndef UNIX_PATH_MAX
	#define UNIX_PATH_MAX (108)
#endif
#define MIN(A,B) A<B?A:B

char message[] = "Hello there!\n";
char buf[sizeof(message)];

int main (int argc, char ** argv) {
	struct sockaddr_un SockAddr;
	int AddrLen;
	int Socket = socket (PF_UNIX, SOCK_STREAM, 0);
	if (Socket == -1) {
		printf ("Unable to open communication socket because of %s, quitting the Application\n", strerror (errno));
		return errno;
	} else {
		SockAddr.sun_family = AF_UNIX;
		memset (&SockAddr.sun_path, 0, UNIX_PATH_MAX);
		memcpy (&SockAddr.sun_path [1], SOCKET_NAME, MIN (strlen (SOCKET_NAME), UNIX_PATH_MAX));
		AddrLen = sizeof (SockAddr);
		if (bind (Socket, (struct sockaddr *) &SockAddr, AddrLen)) {
			printf ("Unable to bind socket because of %s, quitting the Application\n", strerror (errno));
			return errno;
		}
	}
	
	// any other stuff here
	sleep(10);

	close(Socket);
	return 0;
}

/*
	gcc -o socket socket.c
 */
