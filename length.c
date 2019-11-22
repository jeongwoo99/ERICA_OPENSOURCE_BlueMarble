#include <stdio.h>
size_t strlen(const char *s){
	int cnt = 0;
	while(*s != '\0'){
		cnt ++;
	}
	return cnt;
}
void main(int argc, char * argv[]){
	printf("%ld\n", strlen(argv[1]) );
}
