// fc.c: z = a + b, numpy arrays from cython

#include "fc.h"
#include <stdio.h>

int fc( int N, const double a[], const double b[], double z[] )
{
    printf( "fc: N=%d a[0]=%f b[0]=%f \n", N, a[0], b[0] );
    int j;
    for(j = 0;  j < N;  j ++ )
    {
        z[j] = a[j] + b[j];
    }
    return N;
}
