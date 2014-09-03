#!/usr/bin/env python

'''
Setup script for ode_with_sympy. Loads the model definition and calls
the methods to parse, write, integrate and plot the model.
'''

from cvode_with_sympy import *
import model_def
import os
import time

tstart = time.time()

writeModel = False


# load model
(tName, xNames, pNames, dxdt) = model_def.MAPK()

if writeModel==True:
	# parse model
	(xs,ps,fs,dfdx) = parse_sym(tName, xNames, pNames, dxdt)

	write_ode_c(xs,ps,fs,dfdx)
	os.system("python ode_setup.py build_ext --inplace")
	write_jac_c(xs,ps,fs,dfdx)
	os.system("python jac_setup.py build_ext --inplace")

# set initial parameters
p0 = np.array([2.5, 0.25, 0.025, 0.025, 0.75, 0.75, 0.025, 0.025, 0.5, 0.5,
	  		   10., 8., 15., 15., 15., 15., 15., 15., 15., 15.,
	  		   9., 1.], 
	  		   dtype=np.float64)

# set initial concentrations
x0 = np.zeros([len(xNames)],dtype=np.float64) +0.1
x0[0] = 100
x0[2] = 300
x0[5] = 300 

# set integration time
t = np.linspace(0, 150*60, 1000)

# integrate model
[t, x] = integrate(p0, x0, t, 'vode')

#  print elapsed time
elapsed = time.time() - tstart
print elapsed

# plot model variables
plot_vars(t, x[:,[5,7]], [xNames[5],xNames[7]])
