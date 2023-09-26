from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

m = size  # In order to use scatter, the num of rows must be equal to num of ranks
n = 5  # This value can be changed

b = np.ones(n) * 2.0

if rank == 0:
    A = np.random.rand(m, n)
else:
    A = None

data = comm.scatter(A, root=0)
res = np.dot(b, data)
result = comm.gather(res, root=0)

if rank == 0:
    print("Final result:", result)
    print("Expected result:", A @ b)
