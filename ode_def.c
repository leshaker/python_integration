#include "ode_def.h"
#include <stdio.h>

#include <math.h>

int ode_def( double t, const double x[], const double p[], double dxdt[] )
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

	dxdt[0] = -Epo*EpoR*kon + EpoEpoR*koff + EpoEpoRi*kex;
	dxdt[1] = Bmax*kt - Epo*EpoR*kon + EpoEpoR*koff + EpoEpoRi*kex - EpoR*kt;
	dxdt[2] = Epo*EpoR*kon - EpoEpoR*ke - EpoEpoR*koff;
	dxdt[3] = EpoEpoR*ke - EpoEpoRi*kde - EpoEpoRi*kdi - EpoEpoRi*kex;
	dxdt[4] = EpoEpoRi*kdi;
	dxdt[5] = EpoEpoRi*kde;

	return 1;
}
