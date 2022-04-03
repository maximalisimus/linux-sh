PROJECT=main
CC=c++
SOURCES=$(PROJECT).cpp
HEADERS=webview.h
TARGET=webview-example
OBJECTS=$(SOURCES:.cpp=.o)
FLAGS=$(shell pkg-config --cflags gtk+-3.0 webkit2gtk-4.0)
CFLAGS=-Wall -o2 -s -DNDEBUG
#CFLAGS=-Wall -o0 -g
CLIBS=$(shell pkg-config --libs gtk+-3.0 webkit2gtk-4.0)

.PHONY: all clean

all:
	$(CC) $(SOURCES) $(HEADERS) $(FLAGS) -c $(OBJECTS)
	$(CC) $(OBJECTS) $(CFLAGS) $(CLIBS) -o $(TARGET)

clean:
	rm -rf *.o $(TARGET)
