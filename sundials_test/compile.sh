# !/usr/bin bash

rm -rf integrate_ode
gcc integrate_ode_src.c -lsundials_cvode -lsundials_nvecserial -o integrate_ode

./integrate_ode