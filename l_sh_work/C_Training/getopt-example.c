// Программа для иллюстрации getopt ()
// функция в C

#include <stdio.h> 
#include <unistd.h> 

int main(int argc, char *argv[])
{
    int opt;
    
	// положить ':' в начало
	// строка, чтобы программа могла
	//различать '?' и ':'

	while((opt = getopt(argc, argv, ":if:lrx")) != -1) 
	{
		switch(opt)
		{
            case 'i':
            case 'l':
			case 'r':
				printf("option: %c\n", opt);
				break;
			case 'f':
				printf("filename: %s\n", optarg);
				break;
			case ':':
				printf("option needs a value\n"); 
				break;
			case '?':
				printf("unknown option: %c\n", optopt);
				break;
		}
	}

    // optind для дополнительных аргументов
    // которые не анализируются
	for(; optind < argc; optind++){
		printf("extra arguments: %s\n", argv[optind]); 
	}
	return 0;
}

/* 
	gcc -o getopt-example getopt-example.c
	./getopt-example -i -f file.txt -lr -x 'hero'

	option: i
	filename: file.txt
	option: l
	option: r
	extra arguments: hero
 */
