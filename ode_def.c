#include "ode_def.h"
#include <stdio.h>

#include <math.h>

int ode_def( double t, const double x[], const double p[], double dxdt[] )
{
	double k1 =  p[0];
	double k2 =  p[1];
	double k3 =  p[2];
	double k4 =  p[3];
	double k5 =  p[4];
	double k6 =  p[5];
	double k7 =  p[6];
	double k8 =  p[7];
	double k9 =  p[8];
	double k10 =  p[9];
	double KK1 =  p[10];
	double KK2 =  p[11];
	double KK3 =  p[12];
	double KK4 =  p[13];
	double KK5 =  p[14];
	double KK6 =  p[15];
	double KK7 =  p[16];
	double KK8 =  p[17];
	double KK9 =  p[18];
	double KK10 =  p[19];
	double Ki =  p[20];
	double n =  p[21];

	double MKKK =  x[0];
	double MKKKp =  x[1];
	double MKK =  x[2];
	double MKKp =  x[3];
	double MKKpp =  x[4];
	double MAPK =  x[5];
	double MAPKp =  x[6];
	double MAPKpp =  x[7];

	dxdt[0] = -MKKK*k1/((KK1 + MKKK)*(pow(MAPKpp/Ki, n) + 1)) + MKKKp*k2/(KK2 + MKKKp);
	dxdt[1] = MKKK*k1/((KK1 + MKKK)*(pow(MAPKpp/Ki, n) + 1)) - MKKKp*k2/(KK2 + MKKKp);
	dxdt[2] = -MKK*MKKKp*k3/(KK3 + MKK) + MKKp*k6/(KK6 + MKKp);
	dxdt[3] = MKK*MKKKp*k3/(KK3 + MKK) - MKKKp*MKKp*k4/(KK4 + MKKp) - MKKp*k6/(KK6 + MKKp) + MKKpp*k5/(KK5 + MKKpp);
	dxdt[4] = MKKKp*MKKp*k4/(KK4 + MKKp) - MKKpp*k5/(KK5 + MKKpp);
	dxdt[5] = -MAPK*MKKpp*k7/(KK7 + MAPK) + MAPKp*k10/(KK10 + MAPKp);
	dxdt[6] = MAPK*MKKpp*k7/(KK7 + MAPK) - MAPKp*MKKpp*k8/(KK8 + MAPKp) - MAPKp*k10/(KK10 + MAPKp) + MAPKpp*k9/(KK9 + MAPKpp);
	dxdt[7] = MAPKp*MKKpp*k8/(KK8 + MAPKp) - MAPKpp*k9/(KK9 + MAPKpp);

	return 1;
}
