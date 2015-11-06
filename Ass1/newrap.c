/**
 * File: newrap.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <stdio.h>
#include <math.h>
#define MAX_CYCLES 10000
#define TOLERANCE pow(10, -7)
#define EPSILON pow(10, -14)

/**
 * Newton-Raphson method find root of function f given
 * derivative of f f_prime.
 */
void 
newrap_root(float (*f)(float), float (*f_prime)(float), float x0, char loop)
{
    int steps = 0;
    float x1, y, y_prime;

    printf("Starting from %g:\n", x0);

    while(++steps < MAX_CYCLES)
    {
        y = f(x0);
        y_prime = f_prime(x0);

        if(fabs(y_prime) < EPSILON)
        {
            break;
        }

        x1 = x0 - y / y_prime;

        if(fabs(x1 - x0) / fabs(x1) < TOLERANCE)
        {
            break;
        }

        x0 = x1;
    }

    if(!isnan(x1))
    {
        printf("  After %d steps: found root %g\n", steps, x0);
        if(loop) newrap_root(f, f_prime, -x0, 0);
    }
    else
    {
        printf("After %d steps: found no root\n", steps);
        if(loop) newrap_root(f, f_prime, -x0, 0);
    }
}

float
f(float x)
{
    return pow(x, 3) + 3 * pow(x, 2) -4 ;
}

float
f_prime(float x)
{
    return 3 * pow(x, 2) + 6 * x;
}

int
main()
{
    printf("=====Finding roots using Newton-Raphson======\n");
    newrap_root(&f, &f_prime, 2, 1);    
}