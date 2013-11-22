# f.pyx: numpy arrays -> extern from "fc.h"
# 3 steps:
# cython f.pyx  -> f.c
# link: python f-setup.py build_ext --inplace  -> f.so, a dynamic library
# py test-f.py: import f gets f.so, f.fpy below calls fc()

import numpy as np
cimport numpy as np

cdef extern from "ode_def.h": 
    int ode_def( double t, double* x, double* p, double* dxdt )

def f( T,
    np.ndarray[np.double_t,ndim=1] X,
    np.ndarray[np.double_t,ndim=1] P,
    np.ndarray[np.double_t,ndim=1] DXDT ):
    """ wrap np arrays to ode_def( x.data ... ) """
    fret = ode_def( T, <double*> X.data, <double*> P.data, <double*> DXDT.data )
        # fcret = fc( N, A.data, B.data, Z.data )  grr char*
    return fret

