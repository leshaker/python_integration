static int g(realtype t, N_Vector x, realtype *gout, void *user_data)
{
  realtype x1, x3;

  x1 = Ith(x,1); 
  x3 = Ith(x,3);

  gout[0] = x1 - RCONST(0.0001);
  gout[1] = x3 - RCONST(0.01);

  return(0);
}