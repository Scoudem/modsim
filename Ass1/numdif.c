/**
 * File: numdif.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */
#include <stdio.h>
#include <math.h>
#define M_PI (3.14159265358979323846264338327950288)

double
derivative_righthand(double (*f)(double), double x, double h)
{
    return (f(x + h) - f(x)) / h;
}

double
derivative_central(double (*f)(double), double x, double h)
{
    return (f(x + h) - f(x - h)) / (2*h);
}

/*
Experiment with the value of h to find the most accurate result in 
each case: create a table and/or a graph showing the error as a function of h for each value of x.


Bonus: write a routine that gives a better result for a larger h by using samples at x − 2h, x − h, x + h
and x + 2h. How much better is that routine, and under what conditions? */

void
test_sinus_derivative(double x, char* stringrep)
{
    double h, real, righthand, central;
    printf("\n==========Derivative sin(%s)==========\n", stringrep);
    printf("h\t\treal\t\trighthand\terror * h\tcentral\t\terror * h\n");

    real = cos(x);
    for (h = 0.5; h > 0.0001; h /= 10) {
        righthand = derivative_righthand(sin, x, h);
        central = derivative_central(sin, x, h);

        printf("%lf\t", h);
        printf("%lf\t", real);

        printf("%lf\t", righthand);
        printf("%lf\t", fabs(real - righthand) * real);
        printf("%lf\t", central);
        printf("%lf\t", fabs(real - central) * real);

        //TODO: show the error as function of h
        printf("\n");
    }
}

void
test_derivatives()
{
    test_sinus_derivative(M_PI / 3, "π/3");
    test_sinus_derivative((100 + 1/3) * M_PI, "100π +π/3");
    test_sinus_derivative((pow(10, 12) + 1/3) * M_PI, "10^12π +π/3");
}

int
main(int argc, char* argv[])
{
    test_derivatives();
}