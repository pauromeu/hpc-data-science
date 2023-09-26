from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {"a": 7, "b": 3.14}
    print("From process: ", rank, "\n data sent:", data, "\n")
    comm.isend(data, dest=1, tag=11)
elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print("From process: ", rank, "\n data received:", data, "\n")
elif rank == 2:
    data = np.array([1, 1, 1, 1, 1])
    print("From process: ", rank, "\n data sent:", data, "\n")
    comm.isend(data, dest=3, tag=66)
else:
    req = comm.irecv(source=2, tag=66)
    data = req.wait()
    print("From process: ", rank, "\n data received:", data, "\n")
