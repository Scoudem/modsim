/**
 * File: numdif.c
 * Authors: Sjoerd Wenker - 10617558
 *          Tristan van Vaalen - 10551832
 * Comments: 
 */
#include <stdio.h>
#include <math.h>
#define M_PI (3.14159265358979323846264338327950288)

/*
 * Function will calculate the righthand derivative for a given function f at a given point x with delta h
 */
double
derivative_righthand(double (*f)(double), double x, double h)
{
    return (f(x + h) - f(x)) / h;
}

/*
 * Function will calculate the central derivative for a given function f at a given point x with delta h
 */
double
derivative_central(double (*f)(double), double x, double h)
{
    return (f(x + h) - f(x - h)) / (2*h);
}

/*
 * Test the sinus derivatives for a given value x (stringrep is for the exact representation in the commandline)
 */
void
test_sinus_derivative(double x, char* stringrep)
{
    double h, real, righthand, central;
    printf("\n==========Derivative sin(%s)==========\n", stringrep);
    printf("\th\t\treal\t\t\trighthand\t\terror * h\t\tcentral\t\t\terror * h\n");

    real = cos(x);
    for (h = 0.5; h > 0.0001; h /= 4) {
        righthand = derivative_righthand(sin, x, h);
        central = derivative_central(sin, x, h);

        printf("%17.17g\t", h);
        printf("%17.17g\t", real);

        printf("%17.17g\t", righthand);
        printf("%17.17g\t", fabs(real - righthand) * real);
        printf("%17.17g\t", central);
        printf("%17.17g\t", fabs(real - central) * real);

        printf("\n");
    }
}

int
main(int argc, char* argv[])
{
    test_sinus_derivative(M_PI / 3, "π/3");
    test_sinus_derivative((100 + 1/3) * M_PI, "100π +π/3");
    test_sinus_derivative((pow(10, 12) + 1/3) * M_PI, "10^12π +π/3");
}