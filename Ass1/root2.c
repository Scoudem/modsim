/**
 * File: root2.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <stdio.h>
#include <math.h>
#define MAX_CYCLES 1000
#define TOLERANCE pow(10, -7)
#define CLOSE(a, b) (fabs(a - b) < TOLERANCE)
#define sign(x) ((x > 0) - (x < 0))

/*
 * Binary search using to find root of function f given
 * lower bound a, upper bound b.
 * stores amount of steps and the root in given *steps, *root.
 * returns whether it found root.
 */
int 
binsearch_root(double a, double b, double (*f)(double), int *steps, double *root)
{   
    double c;

    printf("Step\t|f(x)|\n");

    *steps = 0;
    while(++*steps < MAX_CYCLES)
    {
        c = (a + b) / 2;
        *root = f(c);

        printf("%d\t%.17g\n", *steps, *root);

        if(CLOSE(*root, 0) || (b - a) / 2 < TOLERANCE)
        {   
            return 1;
        }

        if(sign(c) == sign(a)) {
            a = c;
        }  else {
            b = c;
        }
    }

    return 0;
}

double
f(double x)
{
    return pow(x, 2) - 2;
}

int
main()
{
    printf("======Finding roots using binary search======\n");
    int steps, lower = 0, upper = 4;
    double root;

    int result = binsearch_root(lower, upper, &f, &steps, &root);
    if(!result) {
        printf("No root found after reaching MAX_CYCLES (%d)\n", MAX_CYCLES);
    } else {
        printf("Found root (%g) in %d steps (lower: %d, upper: %d)\n", root, steps, lower, upper);
    }
}