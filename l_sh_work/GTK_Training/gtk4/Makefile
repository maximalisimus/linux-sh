CC=gcc
CFLAGS=-Wall -o2 -s -DNDEBUG -Werror=implicit-function-declaration
SOURCE=builder.c
EXECUTABLE=gtk
PACKAGE_FLAGS=$(shell pkg-config --cflags gtk4)
PACKAGE_LIBS=$(shell pkg-config --libs gtk4)
OBJECTS=$(SOURCE:.c=.o)

all: c.o
	$(CC) $(OBJECTS) -o $(EXECUTABLE) $(PACKAGE_LIBS)

c.o:
	$(CC) $(SOURCE) $(PACKAGE_FLAGS) -c $(OBJECTS)

clear:
	rm -rf *.o $(EXECUTABLE)
