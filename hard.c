#include <stdio.h>
int sum(int a[][2][3]){
	int sum = 0;
	for(int i = 0; i <2; i ++){
		for(int j = 0; j < 2; j ++){
			for(int k = 0; k < 3; k ++){
				sum += a[i][j][k];
			}
		}
	}
	return sum;
}
void main(int argc, char*argv[]){
	int a[2][2][3] = {{{1,1}, {2}}, {{3}, {4,4}}};
	printf("sum: %d\n", sum(a));
}
