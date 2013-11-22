'''
Model definition script for ode_with_sympy
'''

def EpoEpoR():
	'''
	EpoR model (Becker et al. 2010)
	'''

	# define x names
	xNames = ['Epo','EpoR','EpoEpoR', 'EpoEpoRi', 'dEpoi', 'dEpoe']
	# define p names
	pNames = ['kon', 'koff', 'kex', 'kt', 'ke', 'kdi', 'kde', 'Bmax']
	# define t name
	tName = 't'

	# define rhs of ODEs
	dxdt = []

	dxdt.append('- kon * Epo * EpoR + koff * EpoEpoR + kex * EpoEpoRi')
	dxdt.append('- kon * Epo * EpoR + koff * EpoEpoR + kt * Bmax - kt * EpoR + kex * EpoEpoRi')
	dxdt.append('kon * Epo * EpoR - koff * EpoEpoR - ke * EpoEpoR')
	dxdt.append('ke * EpoEpoR - kex * EpoEpoRi - kdi * EpoEpoRi - kde * EpoEpoRi')
	dxdt.append('kdi * EpoEpoRi')
	dxdt.append('kde * EpoEpoRi')

	return (tName, xNames, pNames, dxdt)

def ToyModel():
	'''
	Toy model
	'''
	# define x names
	xNames = ['A','B','C']
	# define p names
	pNames = ['k1', 'k2', 'k3', 'k4']
	# define t name
	tName = 't'

	# define rhs of ODEs
	dxdt = []

	dxdt.append('- k1 * A + k2 * B - k3 * A * B + k4 * C')
	dxdt.append('+ k1 * A - k2 * B - k3 * A * B + k4 * C')
	dxdt.append('+ k3 * A * B - k4 * C')

	return (tName, xNames, pNames, dxdt)

def WCM_Met():
	'''
	Toy model
	'''

	import Stanford_Lubitz2013

	model_dict = Stanford_Lubitz2013.Met()
	# define x names
	xNames = model_dict['vars']
	# define p names
	pNames = model_dict['pars']
	# define t name
	tName = 't'

	# define rhs of ODEs
	dxdt = []
	for x in xNames:
		dxdt.append(model_dict['odes'][x])

	print "\nmodel successfully loaded!\n"
	return (tName, xNames, pNames, dxdt)

def ToyModel2():
	'''
	Toy model
	'''
	# define x names
	xNames = ['A','B','C']
	# define p names
	pNames = ['k1', 'k2', 'k3', 'k4']
	# define t name
	tName = 't'

	# define rhs of ODEs
	dxdt = []

	dxdt.append('- k1 * log ( A ) + k2 * B ** k3 * log ( A * B ) + C**k4')
	dxdt.append('+ k1 * A - k2 * B - k3 * A * B + k4 * C')
	dxdt.append('+ k3 * A * B - k4 * C')

	return (tName, xNames, pNames, dxdt)