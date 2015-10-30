/**
 * File: floatrep.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <float.h>
#include <stdio.h>
#include <math.h>
#include "add.h"

void
float_lookup()
{
    printf("\n==========Ranges defined by float.h==========\n");
    printf("Float range:    %g - %g\n", FLT_MIN, FLT_MAX);
    printf("Double range:   %g - %g\n", DBL_MIN, DBL_MAX);
    printf("LDouble range:  %Lg - %Lg\n", LDBL_MIN, LDBL_MAX);
}

void
invalid_operations()
{
    printf("\n=========Invalid operations behaviour========\n");
    printf("INFINITY + (-INFINITY):           %g\n", INFINITY + -INFINITY);
    printf("0 * INFINITY:                     %g\n", 0 * INFINITY);
    printf("INFINITY / INFINITY:              %g\n", INFINITY / INFINITY);
    printf("sqrt(-1):                         %g\n", sqrt(-1));
    printf("sqrt(INFINITY):                   %g\n", sqrt(INFINITY));
    printf("sqrt(-INFINITY):                  %g\n", sqrt(-INFINITY));
    printf("(-3) / (-INFINITY):               %g\n", (-3) / (-INFINITY));
    printf("4 - INFINITY:                     %g\n", 4 - INFINITY);

    float x = 3 * pow(10, 70),
          y = 4 * pow(10, 70);

    printf("(3*10^70)^2:                      %g\n", pow(x, 2));
    printf("(4*10^70)^2:                      %g\n", pow(y, 2));
    printf("(3*10^70)^2 + (4*10^70)^2:        %g\n", pow(x, 2) + pow(y, 2));
    printf("sqrt((3*10^70)^2 + (4*10^70)^2):  %g\n", sqrt(pow(x, 2) + pow(y, 2)));
}

float
KahanSummation(int from, int to)
{
    int i;
    float y, t;

    float sum = 1.0 / (float)from;
    float c = 0.0;
    for (i = from + 1; i <= to; i++)
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

    printf("\n==========Summation==========\n");
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
    invalid_operations();

    summation(1, 100000000);
    summation(1, 200000000);
}