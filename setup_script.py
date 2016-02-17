#!/usr/bin/env python

'''
Setup script for cvode_with_sympy. Loads the model definition and calls
the methods to parse, write, integrate and plot the model.
'''

from cvode_with_sympy import *
import model_def
import time
import sys


# # EpoEpoR model
# (t_name, x_names, p_names, dxdt) = model_def.EpoEpoR()
# x0 = [80, 100, 0, 0, 0, 0]
# p0 = [1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 1e-3, 100]
# model_dict = convToDict('EpoEpoR model', x_names, p_names, dxdt, x0, p0)

# # Toy model
# (t_name, x_names, p_names, dxdt) = model_def.ToyModel()
# model_dict = convToDict('Toy model', x_names, p_names, dxdt)

# # Toy model 2
# (t_name, x_names, p_names, dxdt) = model_def.ToyModel2()
# model_dict = convToDict('Toy model 2', x_names, p_names, dxdt)

# MAPK model
(t_name, x_names, p_names, dxdt) = model_def.MAPK()
p0 = np.array([2.5, 0.25, 0.025, 0.025, 0.75, 0.75, 0.025, 0.025, 0.5, 0.5,
	  		   10., 8., 15., 15., 15., 15., 15., 15., 15., 15.,
	  		   9., 1.], 
	  		   dtype=np.float64)
x0 = np.zeros([len(x_names)],dtype=np.float64) +0.1
x0[0] = 100
x0[2] = 300
x0[5] = 300 
model_dict = convToDict('MAPK model', x_names, p_names, dxdt, x0, p0)

writeModelFiles(model_dict,force=True)

# set integration time
t = np.linspace(0,300,300)

# simulate
t,x = integrateSundials(model_dict,tSim=t)

# plot model variables
plotVars(t, x, model_dict)

# convert to D2D format
convertToD2D(model_dict)
