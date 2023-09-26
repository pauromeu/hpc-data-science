from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    vector = np.array([16, 62, 97, 25])
else:
    vector = None

data1 = comm.bcast(vector, root=0)
data2 = comm.scatter(vector, root=0)

print("rank: ", rank, " data1: ", data1, " data2: ", data2)
