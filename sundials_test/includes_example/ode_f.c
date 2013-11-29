static int f(realtype t, N_Vector x, N_Vector xdot, void *user_data)
{
  realtype x1, x2, x3, xd1, xd3;

  x1 = Ith(x,1); 
  x2 = Ith(x,2); 
  x3 = Ith(x,3);

  xd1 = Ith(xdot,1) = RCONST(-0.04)*x1 + RCONST(1.0e4)*x2*x3;
  xd3 = Ith(xdot,3) = RCONST(3.0e7)*x2*x2;
        Ith(xdot,2) = -xd1 - xd3;

  return(0);
}