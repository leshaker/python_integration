

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
    return fret

