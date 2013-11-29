void PrintResults(realtype t, N_Vector x)
{
	printf("t = %4.2f;\tx1 = %4.2f;\tx1 = %4.2f;\tx1 = %4.2f\n",t,Ith(x,1),Ith(x,2),Ith(x,3));
	return;
}