  /* Initialize x */

  Ith(x,1) = X1;
  Ith(x,2) = X2;
  Ith(x,3) = X3;

  /* Set the scalar relative tolerance */
  reltol = RTOL;
  /* Set the vector absolute tolerance */
  Ith(abstol,1) = ATOL1;
  Ith(abstol,2) = ATOL2;
  Ith(abstol,3) = ATOL3;