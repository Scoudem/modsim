/**
 * File: newrap.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <stdio.h>
#include <math.h>
#define MAX_CYCLES 1000
#define TOLERANCE pow(10, -7)

/**
 * Newton-Raphson method find root of function f given
 * derivative of f f_prime.
 */
void 
binsearch_root(float (*f)(float), float (*f_prime)(float))
{
    int steps = 0;
    float x0 = 1, x1, y, y_prime;

    while(++steps < MAX_CYCLES)
    {
        y = f(x0);
        y_prime = f_prime(x0);
        x1 = x0 - y / y_prime;

        if(fabs(x1 - x0) / fabs(x1) < TOLERANCE)
        {
            break;
        }

        x0 = x1;
    }

    printf("After %d steps: found root %g (x0^2=%g)\n", steps, x0, pow(x0, 2));
}

float
f(float x)
{
    return pow(x, 2) - 2;
}

float
f_prime(float x)
{
    return 2 * x;
}

int
main()
{
    printf("=====Finding roots using Newton-Raphson======\n");
    binsearch_root(&f, &f_prime);    
}