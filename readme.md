# HPC for Numerical Methods and Data Science

## Running parallel Python code
In this repo we are using `mpi4py`. Use the command:
```bash
mpirun -n 4 python script.py
```
wehre `4` is the number of cores to be used and `script.py` the name of the script to be run.