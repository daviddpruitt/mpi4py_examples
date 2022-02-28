from mpi4py import MPI

# simple example to show sending and receiving messages

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

numberCount = {'first':1, 'second':1, 'third':1}

# first setup unique dicts for each process
for word, count in numberCount.items():
    numberCount[word] = count * rank

print(f'Process {rank} counts are:')
print(numberCount)

# thread 0 gathers the counts
if rank is 0:
    print('Thread 0 gathering')

    #thread 0 already has one so leave it alone
    print(f'Thread 0 counts:')
    print(numberCount)

    # loop through and receive messages from everyone
    for process in range(1, size):
        recvd_count = comm.recv(source=process, tag=0)
        print(f'Thread 0 recieved from {process}')
        print(recvd_count)
        
#everyone else sends that message
else:
    print(f'Process {rank} is sending')
    comm.send(numberCount, dest=0, tag=0)
