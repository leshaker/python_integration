
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [Extension(name="ode_eval",
                         sources=["ode_eval.pyx", "ode_def.c"],
                         include_dirs = [numpy.get_include()],
                         language="c")]

setup(name = 'ode_eval',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules)


