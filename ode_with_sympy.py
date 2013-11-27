import numpy as np
from scipy.integrate import ode
from scipy.integrate import odeint
# import scipy.optimize as opt
from matplotlib import pyplot
from helper_funs import *

def parse_sym(tName, xNames, pNames, dxdt):	
	'''
	parse model variables and parameters to symbolic variables
	and calculate derivatives
	'''
	
	import sympy as sym
	from sympy import log

	# define symbolic variables for x and p
	for obj in xNames:
		exec("%s = sym.symbols('%s')" % (obj, obj))
	for obj in pNames:
		exec("%s = sym.symbols('%s')" % (obj, obj))
	exec("%s = sym.symbols('%s')" % (tName, tName))

	# group ODEs
	dxdt_sym = sym.zeros([len(xNames), 1])
	fstr = ''
	for i, f in enumerate(dxdt):
		fstr = 'dxdt_sym[%d] = %s' % (i, f)
		# print fstr
		exec(fstr)

	# dxdp = sym.symarray('dxdp',(len(xNames), len(pNames)))

	# check for mass conservation
	mass_cons = sum(dxdt_sym) == 0
	print '\nmass conservation = %s' % mass_cons

	# calculate derivatives
	print "\ninitializing symbolic variables..."
	fs = sym.Matrix(dxdt_sym)
	xs = sym.Matrix(xNames)
	ps = sym.Matrix(pNames)
	print "\ncalculating dfdx..."
	dfdx = fs.jacobian(xs)
	# print "\ncalculating dfdp..."
	# dfdp = fs.jacobian(ps)
	# dxdp = sym.Matrix(dxdp)
	# dxpdt = dfdx*dxdp + dfdp

	print "\nmodel successfully parsed!\n"
	# return (xs,ps,fs,dfdx,dxdp,dxpdt)
	return (xs,ps,fs,dfdx)



def write_ode(xs, ps, fs, dfdx):
	'''
	write ODEs and jacobian to file
	'''

	fid = open('ode_def.py', 'w')
	

	# write header
	header = "'''\nAutomatically created module containing \node and jacobian for numerical integration\n'''\n\n"
	header = header+'import numpy as np\n'
	header = header+'from math import log\n\n'
	header = header+'def f(t, x, p):\n\n'
	fid.write(header)

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\t%s =  p[%d]\n' % (p, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\t%s =  x[%d]\n' % (x, i)
		fid.write(tmp_str)
	fid.write('\n')

	# # write variables definitions
	# for i, dxp in enumerate(dxdp):
	# 	tmp_str = '\t%s =  x[%d+%d]\n' % (dxp, len(xs), i)
	# 	fid.write(tmp_str)
	# fid.write('\n')

	# write ODEs
	# tmp_str = '\tdxdt = np.zeros([%d+%d])\n' % (len(xs),(len(xs)*len(ps)))
	tmp_str = '\tdxdt = np.zeros([%d])\n' % len(xs)
	fid.write(tmp_str)
	fid.write('\n')
	for i, f in enumerate(fs):
		if f!=0:
			tmp_str = '\tdxdt[%d] = %s\n' % (i, f)
			fid.write(tmp_str)
	fid.write('\n')

	# # write sensitivities
	# fid.write('\n')
	# for i, eqn in enumerate(dxpdt):
	# 	tmp_str = '\tdxdt[%d] = %s\n' % (i+len(xs), eqn)
	# 	fid.write(tmp_str)	

	# write footer
	fid.write('\n')
	footer = '\treturn dxdt\n'
	fid.write(footer)
	fid.write('\n')

	# write header
	header = 'def jac(t, x, p):\n'
	fid.write(header)
	fid.write('\n')

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\t%s =  p[%d]\n' % (p, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\t%s =  x[%d]\n' % (x, i)
		fid.write(tmp_str)
		i += 1	
	fid.write('\n')

	# write jacobian
	tmp_str = '\tdfdx = np.zeros([%d,%d])\n' % (len(fs), len(xs))
	fid.write(tmp_str)
	fid.write('\n')
	for i in range(dfdx.shape[0]):
		for j in range(dfdx.shape[1]):
			if dfdx[i,j]!=0:
				tmp_str = '\tdfdx[%d,%d] = %s\n' % (i, j, dfdx[i,j])
				fid.write(tmp_str)

	# write footer	
	fid.write('\n')
	footer = '\treturn dfdx'
	fid.write(footer)
	fid.close()

	print "\nmodel file successfully written!\n"
	return 1

def write_ode_pyx(xs, ps, fs, dfdx):
	'''
	write ODEs and jacobian to file
	'''

	fid = open('ode_def.pyx', 'w')

	# write header
	header = "'''\nAutomatically created module containing \node and jacobian for numerical integration\n'''\n\n"
	header = header+'import numpy as np\n'
	header = header+'cimport numpy as np\n'
	header = header+'DTYPE = np.float64\n'
	header = header+'ctypedef np.float64_t DTYPE_t\n'
	header = header+'from math import log\n\n'
	header = header+'def f(float t, np.ndarray[DTYPE_t, ndim=1] x, np.ndarray[DTYPE_t, ndim=1] p):\n\n'
	fid.write(header)

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\tcdef DTYPE_t %s =  p[%d]\n' % (p, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\tcdef DTYPE_t %s =  x[%d]\n' % (x, i)
		fid.write(tmp_str)
	fid.write('\n')

	# # write variables definitions
	# for i, dxp in enumerate(dxdp):
	# 	tmp_str = '\t%s =  x[%d+%d]\n' % (dxp, len(xs), i)
	# 	fid.write(tmp_str)
	# fid.write('\n')

	# write ODEs
	# tmp_str = '\tdxdt = np.zeros([%d+%d])\n' % (len(xs),(len(xs)*len(ps)))
	tmp_str = '\tcdef np.ndarray[DTYPE_t, ndim=1] dxdt = np.zeros([%d])\n' % len(xs)
	fid.write(tmp_str)
	fid.write('\n')
	for i, f in enumerate(fs):
		if f!=0:
			tmp_str = '\tdxdt[%d] = %s\n' % (i, f)
			fid.write(tmp_str)
	fid.write('\n')

	# # write sensitivities
	# fid.write('\n')
	# for i, eqn in enumerate(dxpdt):
	# 	tmp_str = '\tdxdt[%d] = %s\n' % (i+len(xs), eqn)
	# 	fid.write(tmp_str)	

	# write footer
	fid.write('\n')
	footer = '\treturn dxdt\n'
	fid.write(footer)
	fid.write('\n')

	# write header
	header = 'def jac(float t, np.ndarray[DTYPE_t, ndim=1] x, np.ndarray[DTYPE_t, ndim=1] p):\n'
	fid.write(header)
	fid.write('\n')

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\tcdef DTYPE_t %s =  p[%d]\n' % (p, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\tcdef DTYPE_t %s =  x[%d]\n' % (x, i)
		fid.write(tmp_str)
		i += 1	
	fid.write('\n')

	# write jacobian
	tmp_str = '\tcdef np.ndarray[DTYPE_t, ndim=2] dfdx = np.zeros([%d,%d])\n' % (len(fs), len(xs))
	fid.write(tmp_str)
	fid.write('\n')
	for i in range(dfdx.shape[0]):
		for j in range(dfdx.shape[1]):
			if dfdx[i,j]!=0:
				tmp_str = '\tdfdx[%d,%d] = %s\n' % (i, j, dfdx[i,j])
				fid.write(tmp_str)

	# write footer	
	fid.write('\n')
	footer = '\treturn dfdx'
	fid.write(footer)
	fid.close()

	print "\nmodel file successfully written!\n"
	return 1


def write_ode_c(xs, ps, fs, dfdx):
	'''
	write ODEs to c-file
	'''

	# convert formula to c-style
	fs_c = conv_to_cstr(fs)

	fid = open('ode_def.c', 'w')
	
	# write header
	header = "#include \"ode_def.h\"\n"
	header = header+"#include <stdio.h>\n\n"
	header = header+"#include <math.h>\n\n"
	header = header+"int ode_def( double t, const double x[], const double p[], double dxdt[] )\n{\n"
	fid.write(header)

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\tdouble %s =  p[%d];\n' % (p, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\tdouble %s =  x[%d];\n' % (x, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write odes
	for i, f in enumerate(fs_c):
		if f!=0:
			tmp_str = '\tdxdt[%d] = %s;\n' % (i, f)
			fid.write(tmp_str)
	fid.write('\n')
	
	# write footer	
	footer = '\treturn 1;\n}\n'
	fid.write(footer)
	fid.close()

	print "\node file successfully written!\n"
	return 1

def write_jac_c(xs, ps, fs, dfdx):
	'''
	write jac to c-file
	'''

	# convert formula to c-style
	dfdx_c = conv_to_cstr(dfdx)

	fid = open('jac_def.c', 'w')
	
	# write header
	header = "#include \"jac_def.h\"\n"
	header = header+"#include <stdio.h>\n\n"
	header = header+"#include <math.h>\n\n"
	header = header+"int jac_def( double t, const double x[], const double p[], double dfdx[] )\n{\n"
	fid.write(header)

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\tdouble %s =  p[%d];\n' % (p, i)
		fid.write(tmp_str)
	fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\tdouble %s =  x[%d];\n' % (x, i)
		fid.write(tmp_str)
	fid.write('\n')
	
	# write jacobian
	for i in range(len(dfdx_c)):
		if dfdx[i]!=0:
			tmp_str = '\tdfdx[%d] = %s;\n' % (i, dfdx_c[i])
			fid.write(tmp_str)
	fid.write('\n')

	# write footer	
	footer = '\treturn 1;\n}\n'
	fid.write(footer)
	fid.close()

	print "\njac file successfully written!\n"
	return 1


def integrate(p, x0, tSim, solver='vode'):
	'''
	simulate ode system
	'''
	import wrapper
	
	t0 = tSim[0]
	t1 = tSim[-1]
	dt = np.diff(tSim)

	if solver == 'vode':
		res	= ode(wrapper.ode,wrapper.jac).set_integrator('vode', 
											method='bdf', 
											order=15, 
											nsteps=1000, 
											with_jacobian=True,
											atol=1e-8,
											rtol=1e-8
											)	
	else:
		raise(Exception("Chosen integrator not yet implemented!"))

			
	res.set_initial_value(x0,t0)
	res.set_f_params(p)
	res.set_jac_params(p)
	
	t = np.zeros([len(tSim)])
	x = np.zeros([len(tSim),len(x0)])
	
	i = 0
	while res.successful() and res.t < t1:
	    # print "\nintegrating for t=%f" % res.t
	    res.integrate(res.t+dt[i])
	    t[i+1] = res.t
	    x[i+1] = res.y.flatten()
	    i+=1

	t[0] = t0
	x[0] = x0.flatten()


	return t, x

def plot_vars(t, x, xNames):
	'''
	plot trajectories
	'''

	pyplot.plot(t, x)
	pyplot.legend(xNames)
	pyplot.show()



