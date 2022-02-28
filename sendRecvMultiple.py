from mpi4py import MPI

# simple example to show sending and receiving messages

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

recvd_msg = 'empty message'

# thread 0 sends the message
if rank is 0:
    print('Thread 0 sending message')
    # send message to thread 1, with tag of 42
    # tag doesn't matter so much
    for process in range(1, size):
        msg = f'Hello process {process} from 0'
        comm.send(msg, dest=process, tag=42)
#everyone else receives that message
else:
    # receive a message from thread 0 with tag of 42
    recvd_msg = comm.recv(source=0, tag=42)
    
print(f'Thread {rank} has message {recvd_msg}')
    
