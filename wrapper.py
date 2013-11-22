

import numpy as np

def ode(t,x,p):
	"""
	returns the ode rhs calculated by the cython module
	"""
	import ode_eval
	dxdt = np.zeros_like(x)*np.nan
	ode_eval.f(t,x,p,dxdt)
	return dxdt


def jac(t,x,p):
	"""
	returns the jacobian rhs calculated by the cython module
	"""
	import jac_eval
	dfdx = np.zeros([len(x),len(x)])
	jac_eval.f(t,x,p,dfdx)
	return dfdx