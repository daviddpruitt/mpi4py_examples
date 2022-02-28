from mpi4py import MPI

# simple example to show sending and receiving messages

# get the world communicator
comm = MPI.COMM_WORLD

# get our rank (process #)
rank = comm.Get_rank()

# get the size of the communicator in # processes
size = comm.Get_size()

# the global list
globalListOfDocs = ['doc0.txt', 'doc1.txt', 'doc2.txt',
                    'doc3.txt', 'doc4.txt', 'doc5.txt']

# the local list for this process
localList = []

# thread 0 distributes the work
if rank is 0:
    print('Thread 0 distributing')

    docsPerThread = len(globalListOfDocs) / size

    # first setup thread 0s slice of the list
    localList = globalListOfDocs[:int( docsPerThread )]

    for process in range(1, size):
        #start and end of slice we're sending
        startOfSlice = int( docsPerThread * process )
        endOfSlice = int( docsPerThread * (process + 1) )

        sliceToSend = globalListOfDocs[startOfSlice:endOfSlice]
        comm.send(sliceToSend, dest=process, tag=0)
#everyone else receives that message
else:
    # receive a message from thread 0 with tag of 0
    localList = comm.recv(source=0, tag=0)
    
print(f'Thread {rank} has {localList}')
    
