#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int      N   = 0;
    long int X[2500];
    int      i   = 0;
    float    sum = 0;
      
    // Sanity check: 10 <= N <= 2500
    scanf("%d\n", &N);
    if (N<10 || N>2500)
    	return -1;

    for (i=0; i<N; i++){
        scanf("%ld", &(X[i]));
	sum += X[i];		 
    }
    printf("Mean = %f\n", sum/N);

    // Sorting array, bubble method
    int tmp, j;
    for (i = 0; i<N; i++){
    	int f = 0;
    	for (j=0; j<N-i-1; j++)
	    if (X[j] > X[j+1]){
	    	tmp  = X[j];
		X[j] = X[j+1];
		X[j+1] = tmp;
		f = 1;
	    } // for j
	if (f == 0)
	    break;
    } // for i

    // Median
    float median = 0;
    if (N % 2 == 0){ // even elements, average of two middle elements required
    	int x1 = X[(int)((N/2 -1))];
	int x2 = X[(int) (N/2)];
    	median = ( x1 + x2 ) / 2.0;
    	printf("Median = %f\n", median);
    } else { // odd, select middle element
    	median = X[N/2];
    	printf("Median = %d\n", (int)median);
    }

    // Mode

    
    return 0;
}
