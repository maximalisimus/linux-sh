CC=gcc
CFLAGS=-Wall -o2 -s -DNDEBUG -Werror=implicit-function-declaration
SOURCE=gtkentry.c
EXECUTABLE=gtk
PACKAGE_FLAGS=$(shell pkg-config --cflags gtk+-3.0)
PACKAGE_LIBS=$(shell pkg-config --libs gtk+-3.0)
OBJECTS=$(SOURCE:.c=.o)

all: c.o
	$(CC) $(OBJECTS) $(CFLAGS) -o $(EXECUTABLE) $(PACKAGE_LIBS)

c.o:
	$(CC) $(SOURCE) $(PACKAGE_FLAGS) -c $(OBJECTS)

clear:
	rm -rf *.o $(EXECUTABLE)
