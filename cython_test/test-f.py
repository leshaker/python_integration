#!/usr/bin/env python
# test-f.py

import os
os.system("python f-setup.py build_ext --inplace")

import numpy as np
import f  # loads f.so from cc-lib: f.pyx -> f.c + fc.o -> f.so


N = 3
a = np.ones(N, dtype=np.float64)*10
b = np.arange( N, dtype=np.float64 )*2
z = np.ones( N, dtype=np.float64 ) * np.NaN

print a, b

print a+b

fret = f.fpy( N, a, b, z )
print z

