'''
Automatically created module containing 
ode and jacobian for numerical integration
'''

import numpy as np
cimport numpy as np
DTYPE = np.float64
ctypedef np.float64_t DTYPE_t
from math import log

def f(float t, np.ndarray[DTYPE_t, ndim=1] x, np.ndarray[DTYPE_t, ndim=1] p):

	cdef DTYPE_t kon =  p[0]
	cdef DTYPE_t koff =  p[1]
	cdef DTYPE_t kex =  p[2]
	cdef DTYPE_t kt =  p[3]
	cdef DTYPE_t ke =  p[4]
	cdef DTYPE_t kdi =  p[5]
	cdef DTYPE_t kde =  p[6]
	cdef DTYPE_t Bmax =  p[7]

	cdef DTYPE_t Epo =  x[0]
	cdef DTYPE_t EpoR =  x[1]
	cdef DTYPE_t EpoEpoR =  x[2]
	cdef DTYPE_t EpoEpoRi =  x[3]
	cdef DTYPE_t dEpoi =  x[4]
	cdef DTYPE_t dEpoe =  x[5]

	cdef np.ndarray[DTYPE_t, ndim=1] dxdt = np.zeros([6])

	dxdt[0] = -Epo*EpoR*kon + EpoEpoR*koff + EpoEpoRi*kex
	dxdt[1] = Bmax*kt - Epo*EpoR*kon + EpoEpoR*koff + EpoEpoRi*kex - EpoR*kt
	dxdt[2] = Epo*EpoR*kon - EpoEpoR*ke - EpoEpoR*koff
	dxdt[3] = EpoEpoR*ke - EpoEpoRi*kde - EpoEpoRi*kdi - EpoEpoRi*kex
	dxdt[4] = EpoEpoRi*kdi
	dxdt[5] = EpoEpoRi*kde


	return dxdt

def jac(float t, np.ndarray[DTYPE_t, ndim=1] x, np.ndarray[DTYPE_t, ndim=1] p):

	cdef DTYPE_t kon =  p[0]
	cdef DTYPE_t koff =  p[1]
	cdef DTYPE_t kex =  p[2]
	cdef DTYPE_t kt =  p[3]
	cdef DTYPE_t ke =  p[4]
	cdef DTYPE_t kdi =  p[5]
	cdef DTYPE_t kde =  p[6]
	cdef DTYPE_t Bmax =  p[7]

	cdef DTYPE_t Epo =  x[0]
	cdef DTYPE_t EpoR =  x[1]
	cdef DTYPE_t EpoEpoR =  x[2]
	cdef DTYPE_t EpoEpoRi =  x[3]
	cdef DTYPE_t dEpoi =  x[4]
	cdef DTYPE_t dEpoe =  x[5]

	cdef np.ndarray[DTYPE_t, ndim=2] dfdx = np.zeros([6,6])

	dfdx[0,0] = -EpoR*kon
	dfdx[0,1] = -Epo*kon
	dfdx[0,2] = koff
	dfdx[0,3] = kex
	dfdx[1,0] = -EpoR*kon
	dfdx[1,1] = -Epo*kon - kt
	dfdx[1,2] = koff
	dfdx[1,3] = kex
	dfdx[2,0] = EpoR*kon
	dfdx[2,1] = Epo*kon
	dfdx[2,2] = -ke - koff
	dfdx[3,2] = ke
	dfdx[3,3] = -kde - kdi - kex
	dfdx[4,3] = kdi
	dfdx[5,3] = kde

	return dfdx