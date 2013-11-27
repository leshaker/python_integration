#include "jac_def.h"
#include <stdio.h>

#include <math.h>

int jac_def( double t, const double x[], const double p[], double dfdx[] )
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

	dfdx[0] = MKKK*k1/(pow(KK1 + MKKK, 2)*(pow(MAPKpp/Ki, n) + 1)) - k1/((KK1 + MKKK)*(pow(MAPKpp/Ki, n) + 1));
	dfdx[1] = -MKKKp*k2/pow(KK2 + MKKKp, 2) + k2/(KK2 + MKKKp);
	dfdx[7] = MKKK*k1*n*pow(MAPKpp/Ki, n)/(MAPKpp*(KK1 + MKKK)*pow(pow(MAPKpp/Ki, n) + 1, 2));
	dfdx[8] = -MKKK*k1/(pow(KK1 + MKKK, 2)*(pow(MAPKpp/Ki, n) + 1)) + k1/((KK1 + MKKK)*(pow(MAPKpp/Ki, n) + 1));
	dfdx[9] = MKKKp*k2/pow(KK2 + MKKKp, 2) - k2/(KK2 + MKKKp);
	dfdx[15] = -MKKK*k1*n*pow(MAPKpp/Ki, n)/(MAPKpp*(KK1 + MKKK)*pow(pow(MAPKpp/Ki, n) + 1, 2));
	dfdx[17] = -MKK*k3/(KK3 + MKK);
	dfdx[18] = MKK*MKKKp*k3/pow(KK3 + MKK, 2) - MKKKp*k3/(KK3 + MKK);
	dfdx[19] = -MKKp*k6/pow(KK6 + MKKp, 2) + k6/(KK6 + MKKp);
	dfdx[25] = MKK*k3/(KK3 + MKK) - MKKp*k4/(KK4 + MKKp);
	dfdx[26] = -MKK*MKKKp*k3/pow(KK3 + MKK, 2) + MKKKp*k3/(KK3 + MKK);
	dfdx[27] = MKKKp*MKKp*k4/pow(KK4 + MKKp, 2) - MKKKp*k4/(KK4 + MKKp) + MKKp*k6/pow(KK6 + MKKp, 2) - k6/(KK6 + MKKp);
	dfdx[28] = -MKKpp*k5/pow(KK5 + MKKpp, 2) + k5/(KK5 + MKKpp);
	dfdx[33] = MKKp*k4/(KK4 + MKKp);
	dfdx[35] = -MKKKp*MKKp*k4/pow(KK4 + MKKp, 2) + MKKKp*k4/(KK4 + MKKp);
	dfdx[36] = MKKpp*k5/pow(KK5 + MKKpp, 2) - k5/(KK5 + MKKpp);
	dfdx[44] = -MAPK*k7/(KK7 + MAPK);
	dfdx[45] = MAPK*MKKpp*k7/pow(KK7 + MAPK, 2) - MKKpp*k7/(KK7 + MAPK);
	dfdx[46] = -MAPKp*k10/pow(KK10 + MAPKp, 2) + k10/(KK10 + MAPKp);
	dfdx[52] = MAPK*k7/(KK7 + MAPK) - MAPKp*k8/(KK8 + MAPKp);
	dfdx[53] = -MAPK*MKKpp*k7/pow(KK7 + MAPK, 2) + MKKpp*k7/(KK7 + MAPK);
	dfdx[54] = MAPKp*MKKpp*k8/pow(KK8 + MAPKp, 2) + MAPKp*k10/pow(KK10 + MAPKp, 2) - MKKpp*k8/(KK8 + MAPKp) - k10/(KK10 + MAPKp);
	dfdx[55] = -MAPKpp*k9/pow(KK9 + MAPKpp, 2) + k9/(KK9 + MAPKpp);
	dfdx[60] = MAPKp*k8/(KK8 + MAPKp);
	dfdx[62] = -MAPKp*MKKpp*k8/pow(KK8 + MAPKp, 2) + MKKpp*k8/(KK8 + MAPKp);
	dfdx[63] = MAPKpp*k9/pow(KK9 + MAPKpp, 2) - k9/(KK9 + MAPKpp);

	return 1;
}
