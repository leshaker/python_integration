
import numpy
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [Extension(name="jac_eval",
                         sources=["jac_eval.pyx", "jac_def.c"],
                         include_dirs = [numpy.get_include()],
                         language="c")]

setup(name = 'jac_eval',
      cmdclass = {'build_ext': build_ext},
      ext_modules = ext_modules)


