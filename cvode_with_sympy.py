import numpy as np
import os

from helper_funs import *

def parseSym(model_dict):   
	'''
	parse model variables and parameters to symbolic variables
	and calculate derivatives
	'''

	import sympy as sym

	# import functions that are needed in the model
	from sympy.functions import sin,cos,tan,tanh,exp,log,sqrt,Min,Max

	# get model name
	model_name = cleanModelName(model_dict)
	
	# define x names
	ode_species = [species for species in model_dict['odes']]
	ode_alg_species = model_dict['vars']

	# read algebraic equations
	if 'alg_eqs' in model_dict:
		alg_eqs_species = [species for species in model_dict['alg_eqs']]
		# define rhs of alg. eqs
		alg_eqs = [model_dict['alg_eqs'][species] for species in alg_eqs_species]
	else:
		alg_eqs_species = []
		alg_eqs = []

	# define p names
	parameters = model_dict['pars']
	
	# define t name
	t_name = 't'

	# define rhs of ODEs
	dxdt = []
	for species in ode_alg_species:
		if species in model_dict['odes']:
			dxdt.append(model_dict['odes'][species])
		elif 'alg_eqs' in model_dict.keys():
			if species in model_dict['alg_eqs']:
				dxdt.append('0')

	# define symbolic variables for ode_species
	for species in ode_species:
		exec("%s = sym.symbols('%s')" % (species, species))
	# define symbolic variables for alg_eqs_species
	for species in alg_eqs_species:
		exec("%s = sym.symbols('%s')" % (species, species))
	# define symbolic variables for parameters
	for parameter in parameters:
		exec("%s = sym.symbols('%s')" % (parameter, parameter))
	# define symbolic variables for time
	exec("%s = sym.symbols('%s')" % (t_name, t_name))

	# group ODEs
	dxdt_sym = sym.zeros(len(ode_alg_species), 1)
	fstr = ''
	for i, f in enumerate(dxdt):
		# rename max and min function names for sympy
		f = findAndReplace('max', f, 'Max') 
		f = findAndReplace('min', f, 'Min') 
		fstr = 'dxdt_sym[%d] = %s' % (i, f)
		exec(fstr)

	alg_eqs_sym = sym.zeros(len(alg_eqs_species), 1)
	fstr = ''
	for i, f in enumerate(alg_eqs):
		fstr = 'alg_eqs_sym[%d] = %s' % (i, f)
		exec(fstr)

	# dxdp = sym.symarray('dxdp',(len(ode_species), len(parameters)))

	# # check for mass conservation
	# mass_cons = sum(dxdt_sym) == 0
	# print 'checking for mass conservation... %s' % mass_cons

	# calculate derivatives
	fs = sym.Matrix(np.array(dxdt_sym))
	gs = sym.Matrix(np.array(alg_eqs_sym))
	xs = sym.Matrix(np.array(ode_alg_species))
	xs_alg = sym.Matrix(np.array(alg_eqs_species))
	ps = sym.Matrix(np.array(parameters))
	dfdx = fs.jacobian(xs)
	# print "\ncalculating dfdp..."
	# dfdp = fs.jacobian(ps)
	# dxdp = sym.Matrix(dxdp)
	# dxpdt = dfdx*dxdp + dfdp

	# return (xs,ps,fs,dfdx,dxdp,dxpdt)
	return (xs,ps,fs,xs_alg,gs,dfdx)


def writeInitSundials(model_dict,xs,ps,fs,xs_alg,gs,atol=1e-6,rtol=1e-6,hmin=0.0,hmax=0.0,mxsteps=0.0):
	"""
	Write initialization file for sundials solver
	"""

	model_name = cleanModelName(model_dict)

	if not os.path.exists('includes'):
		os.mkdir('./includes')

	fname_def = model_name+'_define.c'
	fid = open('./includes/'+fname_def, 'w')
	define_str = "#define NPARS %d\t\t/* number of parameters */\n" % (len(ps))
	define_str = define_str+"#define NEQ %d\t\t/* number of equations */\n" % len(fs)
	fid.write(define_str)
	fid.close()
	
	fname_init = model_name+'_initialize.c'
	fid = open('./includes/'+fname_init, 'w')
	if (type(atol)!=list):
		atol = [atol for x in range(len(fs))]

	init_str = "hmin = RCONST(%e);\t\t/* minimal stepsize */\n" % hmin
	init_str = init_str + "hmax = RCONST(%e);\t\t/* maximal stepsize */\n" % hmax
	init_str = init_str + "mxsteps = RCONST(%e);\t\t/* maximal number of steps */\n" % mxsteps
	init_str = init_str + "reltol = RCONST(%e);\t\t/* scalar relative tolerance */\n" % rtol
	for i in range(len(fs)):
		init_str = init_str + "Ith(abstol,%d) = RCONST(%e);\t\t/* vector absolute tolerance components */\n" % (i+1, atol[i])
	fid.write(init_str)
	fid.close()

	return 1

	
def writeOdeSundials(model_dict,xs,ps,fs,xs_alg,gs,checknegative):
	'''
	write ODEs to c-file for sundials
	'''

	if checknegative:
		checknegative_c = "TRUE"
	else:
		checknegative_c = "FALSE"
	# get model name
	model_name = cleanModelName(model_dict)

	# convert formula to c-style
	fs_c = convToCstr(fs)
	gs_c = convToCstr(gs)

	alg_dict = dict(zip(xs_alg,gs_c))
	fname_ode = model_name+'_ode_f.c'
	fid = open('./includes/'+fname_ode, 'w')

	# write header
	header = "static int f(realtype t, N_Vector x, N_Vector xdot, void *user_data)\n"
	header = header+"{\n\n"
	header = header+"\tint i;"
	header = header+"\tUserData data;\n"
	header = header+"\tbooleantype check_negative = %s;\n" % (checknegative_c)
	fid.write(header)

	# write parameter definitions
	par_def = "\t/* Extract needed constants from data */\n"
	par_def = par_def+"\tdata = (UserData) user_data;\n"
	par_def = par_def+"\tdouble p[NPARS];\n"
	par_def = par_def+"\tfor (i=0; i<NPARS; i++) p[i] = data->p[i];\n\n"
	fid.write(par_def)

	for i, p in enumerate(ps):
		tmp_str = '\trealtype %s =  p[%d];\n' % (p, i)
		fid.write(tmp_str)
		fid.write('\n')

		# tmp_str = "\tprintf(\"\\n\\n\");\n"
		# fid.write(tmp_str)

	# write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\trealtype %s =  Ith(x,%d);\n' % (x, i+1)
		fid.write(tmp_str)
		# tmp_str = "\tprintf(\"%%f\\n\", %s);\n" % (x)
		# fid.write(tmp_str)
		fid.write('\n')


	# write alg eqs definitions
	for alg in alg_dict:
		tmp_str = '\t%s =  %s;\n' % (alg,alg_dict[alg])
		fid.write(tmp_str)
		# tmp_str = "\tprintf(\"%%f\\n\", %s);\n" % (alg)
		# fid.write(tmp_str)
		fid.write('\n')

	# tmp_str = "\tprintf(\"\\n\\n\");\n"
	# fid.write(tmp_str)

	# # check for neg species # FIXME!
	# non_neg_spec = [sp.origins[model.name] for sp in model.sp_obj if not sp.type == 'thermodynamic']
	# non_neg_spec_cond = ["%s<-1e-5" % (spec) for spec in non_neg_spec]

	# fid.write("\t%s%s%s" % ("if (check_negative && (", " || ".join(non_neg_spec_cond),")) {\n"))
	# # fid.write("\t\tprintf(\"%s\\n\", \"At least one species turned negative!\");\n")
	# fid.write("\t\treturn(1);\n")
	# fid.write("\t}\n")

	# write odes
	for i, f in enumerate(fs_c):
		if not (f=='0' or f=='0.0' or f==0):
			tmp_str = '\tIth(xdot,%d) = %s;\n' % (i+1, f)
			fid.write(tmp_str)
			fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		if x in xs_alg:
			tmp_str = '\tIth(x,%d) = %s;\n' % (i+1, x)
			fid.write(tmp_str)
			# tmp_str = "\tprintf(\"%%f\\n\", %s);\n" % (x)
			# fid.write(tmp_str)
			fid.write('\n')

	# write footer  
	footer = '\treturn(0);\n}\n'
	fid.write(footer)
	fid.close()

	return 1

def writeJacSundials(model_dict,xs,ps,fs,xs_alg,gs,dfdx):
	'''
	write jacobian to c-file for sundials
	'''
	# get model name
	model_name = cleanModelName(model_dict)

	# convert formula to c-style
	gs_c = convToCstr(gs)
	alg_dict = dict(zip(xs_alg,gs_c))

	fname_jac = model_name+'_ode_jac.c'
	fid = open('./includes/'+fname_jac, 'w')

	# write header
	header = "static int Jac(long int N, realtype t, N_Vector x, N_Vector fx, DlsMat J, void *user_data,\nN_Vector tmp1, N_Vector tmp2, N_Vector tmp3)\n"
	header = header+"{\n\n"
	header = header+"\tint i, j;\n"
	header = header+"\tUserData data;\n"
	fid.write(header)

	# write parameter definitions
	par_def = "\t/* Extract needed constants from data */\n"
	par_def = par_def+"\tdata = (UserData) user_data;\n"
	par_def = par_def+"\tdouble p[NPARS];\n"
	par_def = par_def+"\tfor (i=0; i<NPARS; i++) p[i] = data->p[i];\n\n"
	fid.write(par_def)

	# write parameter definitions
	for i, p in enumerate(ps):
		tmp_str = '\trealtype %s =  p[%d];\n' % (p, i)
		fid.write(tmp_str)
		fid.write('\n')   

	#write variables definitions
	for i, x in enumerate(xs):
		tmp_str = '\trealtype %s =  Ith(x,%d);\n' % (x, i+1)
		fid.write(tmp_str)
		fid.write('\n')

	#write alg eqs
	for alg in alg_dict:
		tmp_str = '\t%s =  %s;\n' % (alg,alg_dict[alg])
		fid.write(tmp_str)
		fid.write('\n')

	# write jacobian
	for i in range(dfdx.shape[0]):
		for j in range(dfdx.shape[1]):
			if not dfdx[i,j]==0:
				# convert formula to c-style
				dfdx_c = convToCstr([dfdx[i,j]])
				tmp_str = '\tIJth(J,%d,%d) = %s;\n' % (i+1,j+1, dfdx_c[0])
				fid.write(tmp_str)
				fid.write('\n')

	# write variables definitions
	for i, x in enumerate(xs):
		if x in xs_alg: 
			tmp_str = '\tIth(x,%d) = %s;\n' % (i+1, x)
			fid.write(tmp_str)
			fid.write('\n')

	# write footer  
	footer = '\treturn(0);\n}\n'
	fid.write(footer)
	fid.close()

	return 1


def compileModel(model_dict):
	'''
	compile c files for CVODE
	'''
	import subprocess
	workdir = os.getcwd()

	model_name = cleanModelName(model_dict)

	fid = open(os.path.join(workdir,'src/integrate_cvode.c'),'r')
	integrate_src = fid.readlines()
	fid.close()

	integrate_src = [line.replace('define.c', model_name+'_define.c') for line in integrate_src]
	integrate_src = [line.replace('initialize.c', model_name+'_initialize.c') for line in integrate_src]
	integrate_src = [line.replace('ode_f.c', model_name+'_ode_f.c') for line in integrate_src]
	integrate_src = [line.replace('ode_jac.c', model_name+'_ode_jac.c') for line in integrate_src]

	# create model checksum
	checksum = modelHash(model_dict)

	fid = open(os.path.join(workdir,'src/%s_src.c' % model_name), 'w')
	fid.writelines(integrate_src)
	fid.close()

	model_compiled = "%s_%s" % (model_name,checksum)
	flist = os.listdir("./bin")
	if model_compiled in flist:
		rm_cmd = "rm -rf %s" % model_compiled
		os.system(rm_cmd)
	compile_cmd = ["gcc", "./src/%s_src.c" % model_name, "-lsundials_cvode", "-lm","-lsundials_nvecserial", 
	"-o%s%s" % ("./bin/",model_compiled)]
	process = subprocess.Popen(compile_cmd, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	if stderr:
		print stderr, '\n' 

	return


def integrateSundials(model_dict, species_values=[], parameter_values=[], tSim=[]):
	'''
	Simulate ODE system using Sundials CVODE
	'''
	import subprocess

	model_name = cleanModelName(model_dict)

	if tSim == []:
		raise("no integration times defined!")
	else:
		t0 = tSim[0]
		t1 = tSim[-1]
		dt = np.diff(tSim).mean()

	# set initial concentrations
	# ode_species = [species for species in model_dict['vars'] if species in model_dict['odes']]
	ode_species = model_dict['vars']

	if 'alg_eqs' in model_dict.keys():
		alg_eqs_species = [species for species in model_dict['vars'] if species in model_dict['alg_eqs']]
	else:
		alg_eqs_species = []

	# ode_species = model_dict['vars']
	if species_values == []:
		x0 = [model_dict['initvars'][species] for species in ode_species]
	else:
		x0 = [species_values[species] for species in ode_species]

	# set parameters
	parameters = model_dict['pars']
	if parameter_values == []:
		p0 = [model_dict['initpars'][par] for par in parameters]
	else:
		p0 = [parameter_values[par] for par in parameters]

	# # set values of alg_eqs
	# if species_values == []:
	#     p_alg = [model_dict['initvars'][species] for species in alg_eqs_species]
	# else:
	#     p_alg = [species_values[species] for species in alg_eqs_species]

	args = []
	args.extend(x0)
	args.extend(p0)
	# args.extend(p_alg)
	args.extend([t0, t1, dt])

	# convert argument list to string without brackets
	args_str = " ".join([str(arg) for arg in args])

	# generate checksum to locate binary
	checksum = modelHash(model_dict)
	model_compiled = "%s%s_%s" % ('./bin/',model_name,checksum)

	# run solver binary
	solver_cmd =  "./%s %s" % (model_compiled, args_str)
	# print solver_cmd

	process = subprocess.Popen(solver_cmd.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE) 

	# read stdout of solver and convert it to array
	tx_out = [line.replace('\n', '') for line in process.stdout.readlines()] # get rid of newlines
	tx_out = [[float(x) for x in line.split('; ') if x != ''] for line in tx_out] # split and convert from string to float

	# read stderr
	stderr = " ".join([line.replace('\n', '') for line in process.stderr.readlines()])

	# print stderr
	if stderr:
		print stderr

	# append initial values and timepoint
	tx0 = x0
	tx0.insert(0,t0)
	tx_out.insert(0,tx0)
	tx_out = np.array(tx_out)

	# separate into t and x array
	t = tx_out[:,0]
	x = tx_out[:,1:]

	return t, x

def writeModelFiles(model_dict,force=False,atol=1e-6,rtol=1e-6,hmin=0.0,hmax=0.0,mxsteps=0.0,checknegative=True):
	"""
	Checks if model_dict has changed. 
	Writes all c-files needed for simulation with sundials CVODE.

	"""

	model_name = cleanModelName(model_dict)

	# get solver options from model_dict
	if 'solveropts' in model_dict:
		solveropts = model_dict['solveropts']
		if 'atol' in solveropts: atol = solveropts['atol']
		if 'rtol' in solveropts: rtol = solveropts['rtol']
		if 'hmin' in solveropts: hmin = solveropts['hmin']
		if 'hmax' in solveropts: hmax = solveropts['hmax']
		if 'mxsteps' in solveropts: mxsteps = solveropts['mxsteps']

	# check if bin directory exists
	if not os.path.exists('bin'):
		os.mkdir('./bin')

	# check if module exists and if checksum has changed
	flist = os.listdir("./bin")
	bin_files = [f for f in flist if model_name in f]
	checksum = modelHash(model_dict)
	bin = [x for x in bin_files if str(checksum) in x]
	bin_exists = [str(checksum) in b for b in bin]

	if force or (len(bin_exists) != 1 or bin_exists[0]==False):
		# remove old bin files
		for bin in bin_files:
			rm_cmd = "rm -rf %s" % os.path.join('./bin/',bin)
			os.system(rm_cmd)
		# parse model
		(xs,ps,fs,xs_alg,gs,dfdx) = parseSym(model_dict)
		# write define.c and initialize.c
		writeInitSundials(model_dict,xs,ps,fs,xs_alg,gs,atol,rtol,hmin,hmax,mxsteps)
		# write ode_f.c
		writeOdeSundials(model_dict,xs,ps,fs,xs_alg,gs,checknegative)
		# write ode_jac.c
		writeJacSundials(model_dict,xs,ps,fs,xs_alg,gs,dfdx)
		# compile model
		compileModel(model_dict)

	return 1


def objectiveFunction(model_dict,initvars,initpars,data,tExp):

	model_dict['initpars'] = initpars
	model_dict['initvars'] = initvars

	t,x = integrateSundials(model_dict,tSim=tExp)
	chi2 = np.sum((x-data['x'])**2/data['sd']**2)

	return chi2


def convertToD2D(model_dict,savepath='./D2D'):

	if not os.path.exists(savepath):
		os.mkdir(savepath)

	# get model name
	model_name = cleanModelName(model_dict)

	# define x names
	ode_species = [species for species in model_dict['odes']]
	ode_species.sort()

	# read algebraic equations
	if 'alg_eqs' in model_dict:
		alg_eqs_species = [species for species in model_dict['alg_eqs']]
		alg_eqs_species.sort()
		# define rhs of alg. eqs
	else:
		alg_eqs_species = []

	# create subfolders
	model_path = os.path.join(savepath,'Models')
	data_path = os.path.join(savepath,'Data')
	if not os.path.exists(model_path):
		os.mkdir(model_path)
	if not os.path.exists(data_path):
		os.mkdir(data_path)

	# open new model file
	fid = open(os.path.join(model_path,model_name+'.def'),'w')

	# write DESCRIPTION block
	if 'description' in model_dict:
		desc = model_dict['description']
	else:
		desc = model_dict['name']

	tmp_str = '%s\n\"%s\"\n\n' % ('DESCRIPTION',desc)
	fid.write(tmp_str)

	# write PREDICTOR block
	tmp_str = '%s\n%s\t\t%s\t%s\t\t%s\t\t%d\t%d\n\n' % ('PREDICTOR', 't', 'T','min','time',0,3000)
	fid.write(tmp_str)

	# define compartments
	if 'compartments' in model_dict:
		compartments = model_dict['compartments']
	else:
		compartments = {'cyt':{'volume':1,'units':'fl'}}

	# write COMPARTMENTS block
	tmp_str = '%s\n%s\n\n' % ('COMPARTMENTS','')
	fid.write(tmp_str)
	
	# define units
	if 'units' in model_dict:
		units = model_dict['units']
	else:
		units = {var:'pM' for var in model_dict['vars']}

	# write STATES block
	tmp_str = '%s\n' % ('STATES')
	fid.write(tmp_str)

	for x in ode_species:
		tmp_str = '%s\t\t%s\t%s\t%s\t%d\n' % (x, 'C', units[x], 'conc.', 1)
		fid.write(tmp_str)
	for alg in alg_eqs_species:
		tmp_str = '%s\t\t%s\t%s\t%s\t%d\n' % (alg, 'C', units[alg], 'conc.', 1)
		fid.write(tmp_str)
	fid.write('\n\n')

	# write INPUTS block
	tmp_str = '%s\n%s\n\n' % ('INPUTS','')
	fid.write(tmp_str)

	# write ODES block
	tmp_str = '%s\n' % ('ODES')
	fid.write(tmp_str)

	for x in ode_species:
		ode = mathToMatlab(model_dict['odes'][x])
		tmp_str = '\"%s\"\n' % (ode)
		fid.write(tmp_str)
	for alg in alg_eqs_species:
		tmp_str = '\"0\"\n'
		fid.write(tmp_str)
	fid.write('\n\n')

	# write DERIVED block
	tmp_str = '%s\n%s\n\n' % ('DERIVED','')
	fid.write(tmp_str)

	# write CONDITIONS block
	tmp_str = '%s\n' % ('CONDITIONS')
	fid.write(tmp_str)

	for alg in alg_eqs_species:
		tmp_str = '%s\t\t\"%s\"\n' % (alg, mathToMatlab(model_dict['alg_eqs'][alg]))
		fid.write(tmp_str)
	fid.write('\n\n')

	# write PARAMETERS block
	tmp_str = '%s\n' % ('PARAMETERS')
	fid.write(tmp_str)
	
	for p in model_dict['initpars']:
		if model_dict['initpars'][p] > 0:
			tmp_str = '%s\t\t%f\t%d\t%d\t%d\t%d\n' % (p, np.log10(model_dict['initpars'][p]),1,1,-3,5)
		else:
			tmp_str = '%s\t\t%f\t%d\t%d\t%d\t%d\n' % (p, model_dict['initpars'][p],1,0,0,1000)
		fid.write(tmp_str)	
	for x0 in model_dict['initvars']:
		if model_dict['initvars'][x0] > 0:
			tmp_str = 'init_%s\t\t%f\t%d\t%d\t%d\t%d\n' % (x0, np.log10(model_dict['initvars'][x0]),1,1,-3,5)
		else:
			tmp_str = 'init_%s\t\t%f\t%d\t%d\t%d\t%d\n' % (x0, model_dict['initvars'][x0],1,0,0,1000)
		fid.write(tmp_str)
	fid.write('\n\n')	

	# close file
	fid.close()

	fid = open(os.path.join('./D2D','Setup.m'),'w')

	tmp_str = "arInit;\n\narLoadModel('%s');\n\narCompileAll;\n\narPlot;" % (model_name)
	fid.write(tmp_str)

	# close file
	fid.close()

	return 1

# def calculateDerivative(model_dict,initvars,initpars,data,tExp):
# 	import ad

# 	chi2 = objectiveFunction(model_dict,initvars,initpars,data,tExp)
# 	dxdp = ad.jacobian(chi2,initpars.values())

# 	return dxdp

