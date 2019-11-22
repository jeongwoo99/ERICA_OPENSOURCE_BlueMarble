#include <stdio.h>
void swap(int *, int *);
void bubble(int[], int);

int main(){
	int a[] = {7, 3, 66, 3, -5, 22, 77, 2};
	bubble(a, 8);
	for(int i = 0; i < 8; i ++)
		printf("[%d]", a[i]);
	return 0;
}
void bubble(int a[], int n)
{
	int num;
	for(int i = 0; i < n-1; i ++){
		for(int j = i; j < n-i; j++){
			if(a[j] > a[j+1]){
				num = a[j];
				a[j] = a[j+1];
				a[j+1] = num;
			}
		}
	}
}
