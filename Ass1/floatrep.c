/**
 * File: floatrep.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <float.h>
#include <stdio.h>

int
main(int argc, char* argv[])
{
    fprintf(stdout, "==========Ranges defined by float.h==========\n");
    fprintf(stdout, "Float range:    %g - %g\n", FLT_MIN, FLT_MAX);
    fprintf(stdout, "Double range:   %g - %g\n", DBL_MIN, DBL_MAX);
    fprintf(stdout, "LDouble range:  %Lg - %Lg\n", LDBL_MIN, LDBL_MAX);
}