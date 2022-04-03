
Универсальный вариант, работающий для любых языков/библиотек:
Открыть специальный файл с атрибутами O_RDWR|O_CREAT (как правило, /var/run/program_name.pid).
Попытаться залочить его в экслюзивном режиме (LOCK_EX|LOCK_NB).
Удалось - пишем в него свой PID и считаем, что запустились впервые. При завершении программы залочка снимается, а сам файл можно и не удалять.
Не удалось - читаем из него PID запущенного экземпляра.


lockfile = "/tmp/some_name.lock";
fd = open(lockfile, O_CREAT);
flock(fd, LOCK_EX);

do_something();

unlink(lockfile);
flock(fd, LOCK_UN);


int pid_file = open(zsearch::LOCK_FILE.c_str(), O_CREAT | O_RDWR, 0666);
int rc = flock(pid_file, LOCK_EX | LOCK_NB);
if (rc)
{
	if (EWOULDBLOCK == errno)
	{
		std::cerr << "Only one instance of zsearch is allowed!" << std::endl;
		return -1;
	}
}



#include <sys/file.h>
// acquire shared lock
if (flock(fd, LOCK_SH) == -1) {
	exit(1);
}
// non-atomically upgrade to exclusive lock
// do it in non-blocking mode, i.e. fail if can't upgrade immediately
if (flock(fd, LOCK_EX | LOCK_NB) == -1) {
	exit(1);
}
// release lock
// lock is also released automatically when close() is called or process exits
if (flock(fd, LOCK_UN) == -1) {
	exit(1);
}	





#include <string.h>
#include <errno.h>

extern int errno;  

if(read(fd, buf, 1)==-1) {
    printf("Oh dear, something went wrong with read()! %s\n", strerror(errno));
}



https://www.opennet.ru/cgi-bin/opennet/man.cgi?topic=strerror&category=3
#include <string.h>
char *strerror(int errnum);
int strerror_r(int errnum, char *buf, size_t n);


https://www.opennet.ru/man.shtml?topic=errno&category=3&russian=0
#include <errno.h>
extern int errno;


https://www.opennet.ru/cgi-bin/opennet/man.cgi?topic=close&category=2
#include <unistd.h>
int close(int fd);


https://www.opennet.ru/man.shtml?category=2&topic=open
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
int creat(const char *pathname, mode_t mode);


https://www.opennet.ru/man.shtml?topic=write&category=2&russian=0
#include <unistd.h>
ssize_t write(int fd, const void *buf, size_t count);  


https://www.opennet.ru/cgi-bin/opennet/man.cgi?topic=read&category=2
#include <unistd.h>
ssize_t read(int fd, void *buf, size_t count);


https://www.opennet.ru/man.shtml?topic=unlink&category=2&russian=0
#include <unistd.h>
int unlink(const char *pathname);  


https://www.opennet.ru/man.shtml?topic=flock&category=2&russian=0
#include <sys/file.h>
int flock(int fd, int operation);  






