
#define NEQ   3                		/* number of equations */
#define X1    RCONST(1.0)	      	/* initial x components */
#define X2    RCONST(0.0)	
#define X3    RCONST(0.0)	
#define RTOL  RCONST(1.0e-4)	   	/* scalar relative tolerance */
#define ATOL1 RCONST(1.0e-8)	   	/* vector absolute tolerance components */
#define ATOL2 RCONST(1.0e-14)	
#define ATOL3 RCONST(1.0e-6)	
#define T0    RCONST(0.0)      		/* initial time */
#define T1    RCONST(10.0)     		/* last output time */
#define NOUT  300              		/* maximum number of output times */
#define DT 	  RCONST((T1-T0)/NOUT)  /* output time increment */