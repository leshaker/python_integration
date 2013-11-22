// fc.c: z = a + b, numpy arrays from cython

#include "ode_def.h"
#include <stdio.h>

int ode_def( double t, const double x[], const double p[], double dxdt[] )
{
    dxdt[0] = -x[0]*p[0]+x[1]*p[1];
    dxdt[1] = x[0]*p[0] -x[1]*p[1];
    
    return 1;
}
