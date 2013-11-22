'''
helper functions
'''

def conv_to_cstr(formula):
	"""
	convert sympy expression to c-code

	"""
	# import re

	# # replace A**B by pow(A,B)
	# pattern_pow = r"(\([a-zA-Z0-9.]+\)?)(\*\*)+([a-zA-Z0-9]+)"
	# re_comp = re.compile(pattern_pow)

	# formula_c = []
	# for i in range(len(formula[:])):
	# 	eqn = str(formula[i])
	# 	eqn = re_comp.sub("pow(\g<1>,\g<3>)", eqn)
	# 	formula_c.append(eqn)

	import sympy
	
	formula_c = []
	for i in range(len(formula[:])):
		formula_c.append(sympy.ccode(formula[i]))

	return formula_c