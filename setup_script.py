#!/usr/bin/env python

'''
Setup script for ode_with_sympy. Loads the model definition and calls
the methods to parse, write, integrate and plot the model.
'''

from ode_with_sympy import *
import model_def
import os
import time

tstart = time.time()


writeModel = False
# writeModel = True
flag = 'pyx'

# load model
# (tName, xNames, pNames, dxdt) = model_def.WCM_Met()
(tName, xNames, pNames, dxdt) = model_def.EpoEpoR()
# (tName, xNames, pNames, dxdt) = model_def.ToyModel()

if writeModel==True:
	# parse model
	(xs,ps,fs,dfdx) = parse_sym(tName, xNames, pNames, dxdt)

	if flag == 'py':
		# write odes
		write_ode(xs,ps,fs,dfdx)
	elif flag == 'pyx':
		# write odes
		write_ode_pyx(xs,ps,fs,dfdx)
		# compile ode using cython
		os.system("python compile_ode.py build_ext --inplace")


# set initial parameters
p0 = np.ones([len(pNames)],dtype=np.float64)*1e-1

# set initial concentrations
# dxp0 = np.zeros([np.prod(dxdp.shape),1])
# x0 = np.zeros([len(xNames)+len(dxp0),1]) # TODO: set initial conditions for dxdp
x0 = np.ones([len(xNames)],dtype=np.float64) 
# x0[0] = 100
# x0[1] = 100

# set integration time
t = np.linspace(0, 50, 300)

# import ode function
import ode_def

# integrate model
[t, dxp] = integrate(ode_def,p0, x0, t)

x = dxp[:,:len(xNames)]
# dxdp = dxp[:,len(xNames):]


#  print elapsed time
elapsed = time.time() - tstart
print elapsed

# plot model variables
# plot_vars(t, x, xNames)


# parameter estimation

#tExp 	= linspace(0, 100, 12)
#yExp = array([[10.1051432, 100.44291417, 1.8304438],
#			  [6.54350107, 18.99087671, 86.96441918],
#			  [3.48250214, 18.99531035, 90.31465106],
#			  [3.28275329, 19.16144338, 91.20604695],
#			  [2.55355241, 18.42029304, 91.21180237],
#			  [2.15214567, 18.70008297, 91.44016474],
#			  [1.94104535, 18.9200897, 91.36469575],
#			  [1.90559248, 18.43943968, 91.88813547],
#			  [2.02737772, 18.50889859, 91.66163781],
#			  [2.11162656, 18.72768131, 91.07069469],
#			  [2.31029542, 18.26955074, 91.93600141],
#			  [2.02282523, 18.24119028, 91.12278703]])
#
#
#def obj_fun(log_theta, n, m, tExp, yExp):
#	theta_sim = 10**log_theta
#	p_sim = theta_sim[:n]
#	x0_sim = theta_sim[-m:]
#
#	[tmp, y] = integrate(p_sim, x0_sim, tExp)
#	chi2 = sum((y-yExp)**2)
#
#	return chi2
#
#theta = concatenate((p0, x0))
#log_theta0 = -ones(len(p0)+len(x0))
#
#print '\nchi2 = '+str(obj_fun(log_theta0, len(p0), len(x0), tExp, yExp))+'\n'
#
#bound = zeros([len(log_theta0), 2])
#bound[:, 0] = -5
#bound[:, 1] = 5
#
##log_theta_opt = optimize.fmin_cg(obj_fun,log_theta0,fprime=None,args=[len(p0),len(x0)])
#result = optimize.fmin_l_bfgs_b(obj_fun, log_theta0, fprime=None, args=[len(p0), len(x0), tExp, yExp], approx_grad=1, bounds=bound)
##[log_theta_global,tmp] = optimize.anneal(obj_fun,log_theta0,args=[len(p0),len(x0)])
#
##chi2_global = obj_fun(log_theta_global,len(p0),len(x0))
#
#theta_opt = 10**(result[0])
#
#print '\nchi2_opt = '+str(result[1])+'\n'
##print '\nchi2_opt = '+str(chi2_global)+'\n'
#p_opt = theta_opt[:len(p0)]
#x0_opt = theta_opt[len(p0):]
#[t, x_sim] = integrate(p0, x0, t)
#[t, x_opt] = integrate(p_opt, x0_opt, t)
#plot(t, x_sim, '--')
#for i in range(len(x0)):
#	scatter(tExp, yExp[:, i])
#	plot(t, x_opt[:, i])
#show()
#