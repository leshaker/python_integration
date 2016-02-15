/*
 * -----------------------------------------------------------------
 * $Date: 2016/02/15$
 * -----------------------------------------------------------------
 * Programmer: Max Schelker
 * -----------------------------------------------------------------
 * 
 * -----------------------------------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* Header files with a description of contents used */

#include <cvode/cvode.h>             /* prototypes for CVODE fcts., consts. */
#include <cvode/cvode_dense.h>       /* prototype for CVDense */
#include <nvector/nvector_serial.h>  /* serial N_Vector types, fcts., macros */
#include <sundials/sundials_dense.h> /* definitions DlsMat DENSE_ELEM */
#include <sundials/sundials_types.h> /* definition of type realtype */
#include <sundials/sundials_math.h>  /* definition of ABS and EXP */

/* User-defined vector and matrix accessor macros: Ith, IJth */

/* These macros are defined in order to write code which exactly matches
   the mathematical problem description given above.

   Ith(v,i) references the ith component of the vector v, where i is in
   the range [1..NEQ] and NEQ is defined below. The Ith macro is defined
   using the N_VIth macro in nvector.h. N_VIth numbers the components of
   a vector starting from 0.

   IJth(A,i,j) references the (i,j)th element of the dense matrix A, where
   i and j are in the range [1..NEQ]. The IJth macro is defined using the
   DENSE_ELEM macro in dense.h. DENSE_ELEM numbers rows and columns of a
   dense matrix starting from 0. */

#define Ith(v,i)    NV_Ith_S(v,i-1)       /* Ith numbers components 1..NEQ */
#define IJth(A,i,j) DENSE_ELEM(A,i-1,j-1) /* IJth numbers rows,cols 1..NEQ */

/* Problem Constants */
#include "../includes/define.c"

/* Type : UserData (contains grid constants) */
typedef struct {
  double p[NPARS];
} *UserData;

/* Functions Called by the Solver */

static int f(realtype t, N_Vector x, N_Vector xdot, void *user_data);

static int Jac(long int N, realtype t,
               N_Vector x, N_Vector fx, DlsMat J, void *user_data,
               N_Vector tmp1, N_Vector tmp2, N_Vector tmp3);

/* Private function to check function return values */

static int check_flag(void *flagvalue, char *funcname, int opt);

/* Heaviside function */
static float Heaviside(float x);

/* Max function */
static float Max(float x, float y);

/* Min function */
static float Min(float x, float y);

/*
 *-------------------------------
 * Main Program
 *-------------------------------
 */

int main(int argc, char *argv[])
{
  realtype reltol, hmin, hmax, mxsteps, t, tout;
  N_Vector x, abstol;
  UserData data;
  void *cvode_mem;
  int flag, flagr, iout, i, j;

  if (argc != NPARS+NEQ+4) {
    printf("%s\n", "not enough input arguments!");
    return(1);
  } 

  /* Get initial values, parameters and time settings */
  double x0[NEQ];       /* initial values */
  double p[NPARS];      /* parameters */
  double times[3];      /* times = [t0,t1,dt] */
  
  for ( i = 0; i < NEQ; i++ ) {
    x0[i] = atof(argv[i+1]);
  }

  for ( i = 0; i < NPARS; i++ ) {
    p[i] = atof(argv[i+1+NEQ]);
  }

  for ( i = 0; i < 3; i++ ) {
    times[i] = atof(argv[i+1+NEQ+NPARS]);
  }

  x = abstol = NULL;
  data = NULL;
  cvode_mem = NULL;

  /* Allocate data memory */
  data = (UserData) malloc(sizeof *data);
  if(check_flag((void *)data, "malloc", 2)) return(1);
  
  /* Attach user data */
  for (i=0; i<NPARS; i++) {
    data->p[i] = p[i];
  }
  

  /* Create serial vector of length NEQ for I.C. and abstol */
  x = N_VNew_Serial(NEQ);
  if (check_flag((void *)x, "N_VNew_Serial", 0)) return(1);
  abstol = N_VNew_Serial(NEQ); 
  if (check_flag((void *)abstol, "N_VNew_Serial", 0)) return(1);

  /* Initialize */
  #include "../includes/initialize.c"

  /* Initialize x */
  for (i = 0; i < NEQ; i++) {
    Ith(x,i+1) = x0[i];
  }

  /* Call CVodeCreate to create the solver memory and specify the 
   * Backward Differentiation Formula and the use of a Newton iteration */
  cvode_mem = CVodeCreate(CV_BDF, CV_NEWTON); /* for stiff systems */
  //cvode_mem = CVodeCreate(CV_ADAMS, CV_FUNCTIONAL); /* for non-stiff systems */
  if (check_flag((void *)cvode_mem, "CVodeCreate", 0)) return(1);
  
  /* Call CVodeInit to initialize the integrator memory and specify the
   * user's right hand side function in x'=f(t,y), the inital time times[0], and
   * the initial dependent variable vector x. */
  flag = CVodeInit(cvode_mem, f, times[0], x);
  if (check_flag(&flag, "CVodeInit", 1)) return(1);

  /* Call CVodeSVtolerances to specify the scalar relative tolerance
   * and vector absolute tolerances */
  flag = CVodeSVtolerances(cvode_mem, reltol, abstol);
  if (check_flag(&flag, "CVodeSVtolerances", 1)) return(1);
  
  /* Call CVodeSetMinStep to specify the minimal stepsize */
  flag = CVodeSetMinStep(cvode_mem, hmin);
  if (check_flag(&flag, "CVodeSetMinStep", 1)) return(1);

  /* Call CVodeSetMinStep to specify the maximal stepsize */
  flag = CVodeSetMaxStep(cvode_mem, hmax);
  if (check_flag(&flag, "CVodeSetMaxStep", 1)) return(1);

  /* Call CVodeSetMinStep to specify the minimal stepsize */
  flag = CVodeSetMaxNumSteps(cvode_mem, mxsteps);
  if (check_flag(&flag, "CVodeSetMaxNumSteps", 1)) return(1);

  /* Set the pointer to user-defined data */
  flag = CVodeSetUserData(cvode_mem, data);
  if(check_flag(&flag, "CVodeSetUserData", 1)) return(1);

  /* Call CVDense to specify the CVDENSE dense linear solver */
  flag = CVDense(cvode_mem, NEQ);
  if (check_flag(&flag, "CVDense", 1)) return(1);

  /* Set the Jacobian routine to Jac (user-supplied) */
  flag = CVDlsSetDenseJacFn(cvode_mem, Jac);
  if (check_flag(&flag, "CVDlsSetDenseJacFn", 1)) return(1);

  /* In loop, call CVode, print results, and test for error.
     Break out of loop when nout preset output times have been reached.  */
  iout = 0;  tout = times[0]+times[2];
  while(tout <= times[1]) {
    flag = CVode(cvode_mem, tout, x, &t, CV_NORMAL);

    fprintf(stdout,"%f; ",t);
    for (i=0; i<NEQ; i++) fprintf(stdout,"%f; ",Ith(x,i+1));
    fprintf(stdout,"\n");
    
    if (check_flag(&flag, "CVode", 1)) break;
    if (flag == CV_SUCCESS) {
      iout++;
      tout += times[2];
    }
  }

  /* Free x and abstol vectors */
  N_VDestroy_Serial(x);
  N_VDestroy_Serial(abstol);

  /* Free integrator memory */
  CVodeFree(&cvode_mem);
  /* Free the user data */
  free(data);

  return(0);
}


/*
 *-------------------------------
 * Functions called by the solver
 *-------------------------------
 */

/*
 * f routine. Compute function f(t,x). 
 */
#include "../includes/ode_f.c"


/*
 * Jacobian routine. Compute J(t,x) = df/dx. *
 */
#include "../includes/ode_jac.c"

/* Heaviside function */
static float Heaviside(float x) 
{
  float fval;
  if(x < 0.0) {
    fval = 0.0;
  }
  else if(x == 0) {
    fval = 0.5;
  }
  else if(x > 0) {
    fval = 1.0;
  }
  return fval;
}

/* Max function */
static float Max(float x, float y) {return(fmax(x,y));}

/* Min function */
static float Min(float x, float y) {return(fmin(x,y));}

/*
 * Check function return value...
 *   opt == 0 means SUNDIALS function allocates memory so check if
 *            returned NULL pointer
 *   opt == 1 means SUNDIALS function returns a flag so check if
 *            flag >= 0
 *   opt == 2 means function allocates memory so check if returned
 *            NULL pointer 
 */

static int check_flag(void *flagvalue, char *funcname, int opt)
{
  int *errflag;

  /* Check if SUNDIALS function returned NULL pointer - no memory allocated */
  if (opt == 0 && flagvalue == NULL) {
    fprintf(stderr, "\nSUNDIALS_ERROR: %s() failed - returned NULL pointer\n\n",
	    funcname);
    return(1); }

  /* Check if flag < 0 */
  else if (opt == 1) {
    errflag = (int *) flagvalue;
    if (*errflag < 0) {
      fprintf(stderr, "\nSUNDIALS_ERROR: %s() failed with flag = %d\n\n",
	      funcname, *errflag);
      return(1); }}

  /* Check if function returned NULL pointer - no memory allocated */
  else if (opt == 2 && flagvalue == NULL) {
    fprintf(stderr, "\nMEMORY_ERROR: %s() failed - returned NULL pointer\n\n",
	    funcname);
    return(1); }

  return(0);
}
