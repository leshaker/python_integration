#!/usr/bin/env python
# test-f.py


import os
os.system("python ode_setup.py build_ext --inplace")

import numpy as np
import ode_eval

time = np.linspace(0,5,100)
x = np.array([0,10], dtype=np.float64 )
p = np.ones(2, dtype=np.float64 )*2
dxdt = np.ones(2, dtype=np.float64 ) * np.NaN

print x, p
# print dxdt
for t in time:
	print "t = %2.2f" % t
	fret = ode_eval.f(t,x,p,dxdt)
	print fret
	print dxdt,'\n'

