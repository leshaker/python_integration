

import numpy as np
cimport numpy as np

cdef extern from "jac_def.h": 
    int jac_def( double t, double* x, double* p, double* dfdx )

def f( T,
    np.ndarray[np.double_t,ndim=1] X,
    np.ndarray[np.double_t,ndim=1] P,
    np.ndarray[np.double_t,ndim=2] DFDX ):
    """ wrap np arrays to jac_def( x.data ... ) """
    fret = jac_def( T, <double*> X.data, <double*> P.data, <double*> DFDX.data )
    return fret

