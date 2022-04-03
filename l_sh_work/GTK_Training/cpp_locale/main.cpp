#include <string>
#include <clocale>

using namespace std;

int main( int argc, char * argv [] )
{
	setlocale(LC_ALL,"");
	std::string str;
	str=argv[0] + argv[1] + argv[2];
	printf("argc = %i, argv = %s%s%s", argc, str);
	return 0;
}
