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

def MAPK():
	'''
	Model of the MAPK pathway by Kholodenko 2000
	'''

	# define x names
	xNames = ['MKKK','MKKKp','MKK','MKKp','MKKpp','MAPK','MAPKp','MAPKpp']
	# define p names
	pNames = ['k1', 'k2', 'k3', 'k4','k5','k6','k7','k8','k9','k10',
			  'KK1', 'KK2', 'KK3', 'KK4','KK5','KK6','KK7','KK8','KK9','KK10',
			  'Ki','n']
	# define t name
	tName = 't'

	# define reaction fluxes
	v = ["", # flux v[0] = ""
		 "k1*MKKK/((1+pow((MAPKpp/Ki),n))*(KK1+MKKK))",
		 "k2*MKKKp/(KK2+MKKKp)",
		 "k3*MKKKp*MKK/(KK3+MKK)",
		 "k4*MKKKp*MKKp/(KK4+MKKp)",
		 "k5*MKKpp/(KK5+MKKpp)",
		 "k6*MKKp/(KK6+MKKp)",
		 "k7*MKKpp*MAPK/(KK7+MAPK)",
		 "k8*MKKpp*MAPKp/(KK8+MAPKp)",
		 "k9*MAPKpp/(KK9+MAPKpp)",
		 "k10*MAPKp/(KK10+MAPKp)"]

	# define rhs of ODEs
	dxdt = [v[2]+"-"+v[1], 						# MKKK
			v[1]+"-"+v[2], 						# MKKKp
			v[6]+"-"+v[3],						# MKK
			v[3]+"+"+v[5]+"-"+v[4]+"-"+v[6],	# MKKp
			v[4]+"-"+v[5],						# MKKpp
			v[10]+"-"+v[7],						# MAPK
			v[7]+"+"+v[9]+"-"+v[8]+"-"+v[10],	# MAPKp
			v[8]+"-"+v[9]]						# MAPKpp

	return (tName, xNames, pNames, dxdt)
