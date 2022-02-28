from mpi4py import MPI

# simple example to show how parallelism and distributed memory work

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

# the message to send
msg = "Hello thread 1!"

value = 0
print(f'There are {size} processes')

for i in range(10000):
    value = value + i * rank

print(f'The result from {rank} is {value}')
