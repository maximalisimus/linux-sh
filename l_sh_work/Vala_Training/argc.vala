
// valac argc.vala

int main (string[] args) {
	stdout.printf("Привет, Мир!\n");
	stdout.printf("argc length = %i\n",args.length);
	int a = int.parse(args[2]);
	string s = @"$(a*2)";
	bool b = bool.parse("false");
	stdout.printf("args[0] = %s\nargs[1] = %s\nargs[2]*2 = %s\nargs[3] = %s\n",args[0],args[1],s,args[3]);
	stdout.printf("b = %s\na = %s\n",b.to_string(),a.to_string());
	// $ ./argc skldjf 23 dsf
	// Result: 
	// Привет, Мир!
	//argc length = 4
	// args[0] = ./argc
	// args[1] = skldjf
	// args[2]*2 = 46
	// args[3] = dsf
	// b = false
	// a = 23
	return 0;
}
