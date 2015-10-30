/**
 * File: floatrep.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <float.h>
#include <stdio.h>
#include "add.h"

void
float_lookup()
{
    fprintf(stdout, "==========Ranges defined by float.h==========\n");
    fprintf(stdout, "Float range:    %g - %g\n", FLT_MIN, FLT_MAX);
    fprintf(stdout, "Double range:   %g - %g\n", DBL_MIN, DBL_MAX);
    fprintf(stdout, "LDouble range:  %Lg - %Lg\n", LDBL_MIN, LDBL_MAX);
}

float
KahanSummation(int from, int to)
{
	int i;
	float y, t;

    float sum = 0.0;
    float c = 0.0;
    for (i = from; i <= to; i++)
    {
    	y = (1.0 / (float) i) - c;
    	t = sum + y;
    	c = (t - sum) - y;
    	sum = t;
    }
    return sum;
}

void
summation(int from, int to)
{
    int i;
    int j;
    double sum[7];

    if (from < 1) from = 1;
    if (to < from) to = from + 100;

    printf("==========Summation==========\n");
    printf("The sum of the series 1/i, with i running from %d to %d is\n",
            from, to);
    printf("Forward summation with floats: %g\n",
           sum[0] =addForward(from, to));
    printf("Reverse summation with floats: %g\n",
           sum[1] =addReverse(from, to));
    printf("Recursive summation with floats: %g\n",
           sum[2] =addRecursive(from, to));
    printf("Forward summation with doubles: %g\n",
           sum[3] =addForwardDouble(from, to));
    printf("Reverse summation with doubles: %g\n",
           sum[4] =addReverseDouble(from, to));
    printf("Recursive summation with doubles: %g\n",
           sum[5] =addRecursiveDouble(from, to));
    printf("Kahan summation with floats: %g\n",
           sum[6] =KahanSummation(from, to));
    printf("Differences between results in a matrix:\n");
    for (i = 0; i< 7; i++)
    {
        for (j = 0; j< 7; j++)
        {
            printf("%12.5g\t", sum[i] - sum[j]);
        }
        printf("\n");
    }
}

int
main(int argc, char* argv[])
{
    float_lookup();
    summation(1, 100000000);
    summation(1, 200000000);
}