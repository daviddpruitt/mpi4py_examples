# mpi4py_examples
Some simple examples to show how mpi4py works

All these programs need to be run with `mpirun -n <# process> python3 <name of
program>

* helloWorldMPI.py - a simple hello world program

* parallelism.py - an example that shows the program is always running in parallel

* sendRecv.py - a basic program that shows how send and recv work

* sendRecvMultiple.py - a program that demonstrates how to send messages to
  more than one process

* distributeList.py - shows how to distribute pieces of a list rather than the
  whole list

* gatherDict.py - shows how to gather seperate dictionaries from processes to
  a single process

* deadlock.py - a program that deadlocks due to misordered send and recvs

* bcaseExample - a program that shows how broadcasts work

