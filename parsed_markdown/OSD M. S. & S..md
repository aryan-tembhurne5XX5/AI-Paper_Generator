
MARKING SCHEME
Total No. of Questions - [4]                      Total No. of Printed Pages: 01
G.R. No.                                             P118-132(T1)
OCTOBER 2018 / IN - SEM (T1)
F. Y. M. TECH. (COMPUTER ENGINEERING) (SEMESTER -I)
COURSE NAME: OPERATING SYSTEM DESIGN
COURSE CODE: CSPA11182
(PATTERN 2018)

# Q.1) 3-4 difference between sharing the resource and multiplexing a resource?

a. mask off the system call concept [2] and program error [4]

b. interrupts [2] OR [6]

# Q.2) Discussion on both programs.

a. Various control registers in user mode [4]

b. [6]

# Q.3) Explain variable argc. And why it cannot be 0

a. [4]

b. Pipes [2] and variable sized messages [2]

# Q.4) OR [6]

a. Signaling [2], rendezvous [2] and the producer-consumer patterns [2]

b. Mutual exclusion IPC pattern.




---



# SOLUTION

Total No. of Questions - [4]

Total No. of Printed Pages: 1

OCTOBER 2018 / IN - SEM (T1)

F. Y. M. TECH. (COMPUTER ENGINEERING) (SEMESTER -I)

COURSE NAME: OPERATING SYSTEM DESIGN

COURSE CODE: CSPA11182 (PATTERN 2018)

# Q.1

melfo nother compu ypically lal ntw mpexiTpially h eurc har mle etw users. This can take the form of time-multiplexing, where the users take turns (e.g., the procssor resource) o space-multiplexing, where eac user gets a part o the resource (e.g., a disk drive). [6]

b. mask off the system call: standard interrupt-masking techniques in the system cannot ignore. It typically occurs to signal attention for non-recoverable hardware errors and program error interrupts: An interrupt is a signal from a device attached to a computer or from a program within the computer that requires the operating system to stop and figure out what to do next. OR [4]

# Q.2

a. Discuss both the programs from time complexity and space complexity point of view [6]

b. Discuss control registers like CRO, CR1 in user mode [4]

# Q.3

A. In C++ argument passing here is a variable argc. The name of the variable arge stands for "argument count"; arge contains the number of arguments passed to the program. The name of the variable argy stands for "argument vector". A vector is a one-dimensional array, and argv is a one-dimensional array of strings. [6]

b. Pipe is one-way communication only i.e we can use a pipe such that One process write to the pipe, and the other process reads from the pipe. It opens a pipe, which is an area of main memory that is treated as a "virtual file". [4]

# Q.4

a. The relationship between signaling: Signals are a limited form of inter-process communication (IPC), typically used in Unix, Unix-like, and other POSIX-compliant operating systems. A signal is an asynchronous notification sent to a process or to a specific thread within the same process in order to notify it of an event that occurred, rendezvous: A rendezvous occurs when two processes synchronize and subsequently exchange messages. Rendezvous is symmetric, in that processes that wish to communicate both use the same primitive; and processes invoke Rendezvous with class designations, not procedure names [6]

b. mutual exclusion IPC pattern: In computer science, mutual exclusion is a property of concurrency control, which is instituted for the purpose of preventing race conditions; it is the requirement that one thread of execution never enter its critical section at the same time that another concurrent thread of execution enters its own critical section. [4]

