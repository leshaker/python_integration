#include "jac_def.h"
#include <stdio.h>

#include <math.h>

int jac_def( double t, const double x[], const double p[], double dfdx[] )
{
	double kon =  p[0];
	double koff =  p[1];
	double kex =  p[2];
	double kt =  p[3];
	double ke =  p[4];
	double kdi =  p[5];
	double kde =  p[6];
	double Bmax =  p[7];

	double Epo =  x[0];
	double EpoR =  x[1];
	double EpoEpoR =  x[2];
	double EpoEpoRi =  x[3];
	double dEpoi =  x[4];
	double dEpoe =  x[5];

	dfdx[0] = -EpoR*kon;
	dfdx[1] = -Epo*kon;
	dfdx[2] = koff;
	dfdx[3] = kex;
	dfdx[6] = -EpoR*kon;
	dfdx[7] = -Epo*kon - kt;
	dfdx[8] = koff;
	dfdx[9] = kex;
	dfdx[12] = EpoR*kon;
	dfdx[13] = Epo*kon;
	dfdx[14] = -ke - koff;
	dfdx[20] = ke;
	dfdx[21] = -kde - kdi - kex;
	dfdx[27] = kdi;
	dfdx[33] = kde;

	return 1;
}
