#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
	if(argc != 2)
	return 1;
	puts((char*)crypt(argv[1], "$1$"));
}

