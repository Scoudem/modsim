/**
 * File: floatrep.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <float.h>
#include <stdio.h>
#include <math.h>

// #undef FLT_RADIX
// #undef FLT_MANT_DIG
// #undef FLT_MIN_EXP
// #define FLT_RADIX 10
// #define FLT_MANT_DIG 3
// #define FLT_MIN_EXP -98

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

int
main(int argc, char* argv[])
{
    float_lookup();
    invalid_operations();
}