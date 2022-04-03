
// valac --disable-warnings args-types-convert-math.vala

int main (string[] args) {
	stdout.printf("Привет, Мир!\n");
	stdout.printf("argc length = %i\n",args.length);
	
	int arr_size;
	if (args[args.length] == null) {
		arr_size = args.length -1;
	} else { arr_size = args.length; }
	
	int a = args.length; // int.parse(args[2]); int.parse("-52");
	int d = args.length*2;
	string s = @"$(a*2)";
	bool b = bool.parse("false");
	bool c = true;
	
	for (int i=0; i <= arr_size; i++) { 
		stdout.printf("args[%i] = %s\n",i,args[i]); 
	}
	stdout.printf("\nb = %s\na = args.length *2 = %i = %s\nc = %s\n\n",b.to_string(),d,s,c.to_string());
	// stdin.read_line();
	stdout.printf("print float e.g. 3141.59265358 view 3.3 = %.3f\n\n",3141.59265358);
	
	stdout.printf ("Please enter the radius of a circle: ");
	double radius = double.parse (stdin.read_line ());
	stdout.printf ("Circumference: %g\n", 2 * Math.PI * radius);
	stdout.printf ("sin(pi/2) = %g\n\n", Math.sin (Math.PI / 2));
	
	var rand = Random.int_range (1, 100);
	stdout.printf ("Random i at 1 to 100 = %i\n",rand);
	
	/*
	$ ./args-types-convert-math asdf 23 asds
	Привет, Мир!
	argc length = 4
	args[0] = ./args-types-convert
	args[1] = asdf
	args[2] = 23
	args[3] = asds

	b = false
	a = args.length *2 = 8 = 8
	c = true

	print float e.g. 3141.59265358 view 3.3 = 3141.593

	Please enter the radius of a circle: 11
	Circumference: 69.115
	sin(pi/2) = 1
	 
	Random i at 1 to 100 = 15
	
	%с	Символ типа char
	%d	Десятичное число целого типа со знаком
	%i	Десятичное число целого типа со знаком
	%е	Научная нотация (е нижнего регистра)
	%Е	Научная нотация (Е верхнего регистра)
	%f	Десятичное число с плавающей точкой
	%g	Использует код %е или %f — тот из них, который короче (при использовании %g используется е нижнего регистра)
	%G	Использует код %Е или %f — тот из них, который короче (при использовании %G используется Е верхнего регистра)
	%о	Восьмеричное целое число без знака
	%s	Строка символов
	%u	Десятичное число целого типа без знака
	%х	Шестнадцатиричное целое число без знака (буквы нижнего регистра)
	%Х	Шестнадцатиричное целое число без знака (буквы верхнего регистра)
	%р	Выводит на экран значение указателя
	%n	Ассоциированный аргумент — это указатель на переменную целого типа, в которую помещено количество символов, записанных на данный момент
	%%	Выводит символ %
	*/
	
	return 0;
}
