/**
 * File: newrap.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */

#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#define MAX_CYCLES 10000
#define TOLERANCE pow(10, -7)
#define EPSILON pow(10, -14)


/**
 * Given an array of pairs [a, b] where a * x ^ b is a part of a polynomial
 * and the array forms this polynomial, this function ouputs the next
 * derivative of [a, b].
 */
float**
first_derivative(float input[][2], size_t size)
{
    unsigned int i;

    float **output = (float **) malloc(size * sizeof(float *));
    for(i = 0; i < 10; i++)
    {
        output[i] = (float *) malloc(2 * sizeof(float));
    }
    for(i = 0; i < size; i++)
    {
        output[i][0] = input[i][0] * input[i][1];
        output[i][1] = input[i][1] - 1;
    }

    return output;
}

/**
 * Get the f value for x
 */
float
get_f(float x, float f[][2], size_t size)
{
    float result = 0.0;

    unsigned int i;
    for(i = 0; i < size; i++)
    {
        result += f[i][0] * pow(x, f[i][1]);
    }

    return result;
}

/**
 * Get the f_prime value for x
 */
float
get_f_prime(float x, float** f, size_t size)
{
    float result = 0.0;

    unsigned int i;
    for(i = 0; i < size; i++)
    {
        result += f[i][0] * pow(x, f[i][1]);
    }

    return result;
}


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
    }
    else
    {
        printf("After %d steps: found no root\n", steps);
    }

    if(loop) newrap_root(f, f_prime, -x0, 0);
}


/**
 * Newton-Raphson method find root of function f given
 * derivative of f f_prime. Where f and f_prime are arrays.
 */
void 
newrap_root_array(float f[][2], float** f_p, size_t size, float x0, char loop)
{
    int steps = 0;
    float x1, y, y_prime;

    printf("Starting from %g:\n", x0);

    while(++steps < MAX_CYCLES)
    {
        y = get_f(x0, f, size);
        y_prime = get_f_prime(x0, f_p, size);

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
    }
    else
    {
        printf("After %d steps: found no root\n", steps);
    }

    if(loop) newrap_root_array(f, f_p, size, -x0, 0);
}


/**
 * Predefined f
 */
float
f(float x)
{
    return pow(x, 3) + 3 * pow(x, 2) -4 ;
}


/**
 * Predefined f_prime
 */
float
f_prime(float x)
{
    return 3 * pow(x, 2) + 6 * x;
}


int
main()
{   
    printf("===========Finding roots using Newton-Raphson============\n");
    newrap_root(&f, &f_prime, 2, 1);

    printf("================Finding first derivative=================\n");
    float f[3][2] = {{1.0, 3.0}, {3.0, 2.0}, {-4.0, 0.0}};
    float** f_p = first_derivative(f, 3);

    printf("====Finding roots using Newton-Raphson (own derivative)==\n");
    newrap_root_array(f, f_p, 3, 2, 1);
}