
// valac int-parse.vala

int main (string[] args) {
	stdout.printf("argc length = %i;\n",args.length);
	int a = int.parse(args[1]);
	stdout.printf("args[1] = %s;\nparse = %i;\n",args[1],a);
	/*
	$ ./int-parse 234sef23
	argc length = 2;
	args[1] = 234sef23;
	parse = 234;
	*/
	return 0;
}
