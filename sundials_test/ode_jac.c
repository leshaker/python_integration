static int Jac(long int N, realtype t,
               N_Vector x, N_Vector fx, DlsMat J, void *user_data,
               N_Vector tmp1, N_Vector tmp2, N_Vector tmp3)
{
  realtype x1, x2, x3;

  x1 = Ith(x,1); 
  x2 = Ith(x,2); 
  x3 = Ith(x,3);

  IJth(J,1,1) = RCONST(-0.04);
  IJth(J,1,2) = RCONST(1.0e4)*x3;
  IJth(J,1,3) = RCONST(1.0e4)*x2;
  IJth(J,2,1) = RCONST(0.04); 
  IJth(J,2,2) = RCONST(-1.0e4)*x3-RCONST(6.0e7)*x2;
  IJth(J,2,3) = RCONST(-1.0e4)*x2;
  IJth(J,3,2) = RCONST(6.0e7)*x2;

  return(0);
}