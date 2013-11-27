

import numpy as np

def ode(t,x,p):
	"""
	returns the ode rhs calculated by the cython module
	"""
	import ode_eval
	x = np.array(x)
	p = np.array(p)
	dxdt = np.zeros([len(x)])
	ode_eval.f(t,x,p,dxdt)
	return dxdt


def jac(t,x,p):
	"""
	returns the jacobian rhs calculated by the cython module
	"""
	import jac_eval
	x = np.array(x)
	p = np.array(p)
	dfdx = np.zeros([len(x),len(x)])
	jac_eval.f(t,x,p,dfdx)
	return dfdx