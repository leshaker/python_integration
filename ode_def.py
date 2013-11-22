'''
Automatically created module containing 
ode and jacobian for numerical integration
'''

import numpy as np
from math import log

def f(t, x, p):

	kon =  p[0]
	koff =  p[1]
	kex =  p[2]
	kt =  p[3]
	ke =  p[4]
	kdi =  p[5]
	kde =  p[6]
	Bmax =  p[7]

	Epo =  x[0]
	EpoR =  x[1]
	EpoEpoR =  x[2]
	EpoEpoRi =  x[3]
	dEpoi =  x[4]
	dEpoe =  x[5]

	dxdt = np.zeros([6])

	dxdt[0] = -Epo*EpoR*kon + EpoEpoR*koff + EpoEpoRi*kex
	dxdt[1] = Bmax*kt - Epo*EpoR*kon + EpoEpoR*koff + EpoEpoRi*kex - EpoR*kt
	dxdt[2] = Epo*EpoR*kon - EpoEpoR*ke - EpoEpoR*koff
	dxdt[3] = EpoEpoR*ke - EpoEpoRi*kde - EpoEpoRi*kdi - EpoEpoRi*kex
	dxdt[4] = EpoEpoRi*kdi
	dxdt[5] = EpoEpoRi*kde


	return dxdt

def jac(t, x, p):

	kon =  p[0]
	koff =  p[1]
	kex =  p[2]
	kt =  p[3]
	ke =  p[4]
	kdi =  p[5]
	kde =  p[6]
	Bmax =  p[7]

	Epo =  x[0]
	EpoR =  x[1]
	EpoEpoR =  x[2]
	EpoEpoRi =  x[3]
	dEpoi =  x[4]
	dEpoe =  x[5]

	dfdx = np.zeros([6,6])

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