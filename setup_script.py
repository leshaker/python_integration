#!/usr/bin/env python

'''
Setup script for cvode_with_sympy. Loads the model definition and calls
the methods to parse, write, integrate and plot the model.
'''

from cvode_with_sympy import *
import model_def

import time
import sys

# EpoEpoR model
(t_name, x_names, p_names, dxdt) = model_def.EpoEpoR()
model_dict = convToDict('EpoEpoR model', x_names, p_names, dxdt)

# # Toy model
# (t_name, x_names, p_names, dxdt) = model_def.ToyModel()
# model_dict = convToDict('Toy model', x_names, p_names, dxdt)

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


# import WCM_SBML
# modelfile = '../WCM/sbml_models/Kholodenko2000_Ultra.xml'
# model_dict = WCM_SBML.sbmlImportToDict(modelfile)
# WCM_SBML.writePythonModule(model_dict)

# import CellCycle
# model_dict = CellCycle.CellCycle()

# import MET_TCA_mitochondrion
# model_dict = MET_TCA_mitochondrion.MET_TCA_mitochondrion()

# import MET_glycolysis_cyto
# model_dict = MET_glycolysis_cyto.MET_glycolysis_cyto()

writeModelFiles(model_dict)

# set integration time
t = np.linspace(0,3000,500)

# start counting the time
tstart = time.time()
# integrate model
t,x = integrateSundials(model_dict,tSim=t)

#  print elapsed time
elapsed = time.time() - tstart
print "elapsed time: %f" % elapsed

# plot model variables
plotVars(t, x, model_dict)


# ########
# import Kholodenko2000_Ultra
# model_dict2 = Kholodenko2000_Ultra.Kholodenko2000_Ultra()

# writeModelFiles(model_dict2)
# # integrate model
# t,x = integrateSundials(model_dict2,tSim=t)

# #  print elapsed time
# elapsed = time.time() - tstart
# print "elapsed time: %f" % elapsed

# # plot model variables
# plotVars(t, x, model_dict2)

