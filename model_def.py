'''
Model definition script for cvode_with_sympy
'''

def EpoEpoR():
	'''
	EpoR model (Becker et al. 2010)
	'''

	# define x names
	x_names = ['Epo','EpoR','EpoEpoR', 'EpoEpoRi', 'dEpoi', 'dEpoe']
	# define p names
	p_names = ['kon', 'koff', 'kex', 'kt', 'ke', 'kdi', 'kde', 'EpoR0']
	# define t name
	t_name = 't'

	# define rhs of ODEs
	dxdt = []

	dxdt.append('- kon * Epo * EpoR + koff * EpoEpoR + kex * EpoEpoRi')
	dxdt.append('- kon * Epo * EpoR + koff * EpoEpoR + kt * EpoR0 - kt * EpoR + kex * EpoEpoRi')
	dxdt.append('kon * Epo * EpoR - koff * EpoEpoR - ke * EpoEpoR')
	dxdt.append('ke * EpoEpoR - kex * EpoEpoRi - kdi * EpoEpoRi - kde * EpoEpoRi')
	dxdt.append('kdi * EpoEpoRi')
	dxdt.append('kde * EpoEpoRi')

	return (t_name, x_names, p_names, dxdt)

def ToyModel():
	'''
	Toy model
	'''
	# define x names
	x_names = ['A','B','C']
	# define p names
	p_names = ['k1', 'k2', 'k3', 'k4']
	# define t name
	t_name = 't'

	# define rhs of ODEs
	dxdt = []

	dxdt.append('- k1 * A + k2 * B - k3 * A * B + k4 * C')
	dxdt.append('+ k1 * A - k2 * B - k3 * A * B + k4 * C')
	dxdt.append('+ k3 * A * B - k4 * C')

	return (t_name, x_names, p_names, dxdt)

def ToyModel2():
	'''
	Toy model
	'''
	# define x names
	x_names = ['A','B','C']
	# define p names
	p_names = ['k1', 'k2', 'k3', 'k4']
	# define t name
	t_name = 't'

	# define rhs of ODEs
	dxdt = []

	dxdt.append('- k1 * log ( A ) + k2 * B ** k3 * log ( A * B ) + C**k4')
	dxdt.append('+ k1 * A - k2 * B - k3 * A * B + k4 * C')
	dxdt.append('+ k3 * A * B - k4 * C')

	return (t_name, x_names, p_names, dxdt)

def MAPK():
	'''
	Model of the MAPK pathway by Kholodenko 2000
	'''

	# define x names
	x_names = ['MKKK','MKKKp','MKK','MKKp','MKKpp','MAPK','MAPKp','MAPKpp']
	# define p names
	p_names = ['k1', 'k2', 'k3', 'k4','k5','k6','k7','k8','k9','k10',
			  'KK1', 'KK2', 'KK3', 'KK4','KK5','KK6','KK7','KK8','KK9','KK10',
			  'Ki','n']
	# define t name
	t_name = 't'

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

	return (t_name, x_names, p_names, dxdt)
