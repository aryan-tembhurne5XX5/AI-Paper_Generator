
[3663] - 251

# T.E. (IT) (Semester - I) Examination, 2009

# OPERATING SYSTEMS

# (2003 Course)

Time : 3 Hours

Max. Marks : 100

# Instructions :

1. Answer any three questions from each Section
2. Answers to the two Sections should be written in separate books.
3. Neat diagrams must be drawn wherever necessary.
4. Black figures to the right indicate full marks.
5. Assume suitable data, if necessary.

# SECTION - I

1. a) State and explain different services provided by an operating system. 6

State in brief key features of each of the following types of operating system: 10

- RealTime
- Distributed
- Parallel
- Time sharing.
2. OR
3. 2a) Draw and explain the architecture of Windows 2000. 8

Differentiate system calls and library functions. 4

Discuss the advantages of multiprocessor system. What are different types of multiprocessor system? 4

P.T.O.



---



# 3.a) Explain the concept of context switching with the help of neat diagram.

6

# b) Two processes P1 and P2 need to access a critical section of code. Consider the following synchronization construct used by processes.

* P1         *1                 1*           P2   *1                              6
while (true) {                  while (true) {
wants 1 = true;                 wants 2 = true;
while (wants 2 == true);                while (wants 1 == true);
/* critical section */              /* critical section*/
wants 1 = false;                    wants 2 = false
}                              }
/* remainder section */         /* remainder section */

Here wants 1 and wants 2 are shared variables, which are initialized to false. Which one of the following statement is true about the above construct? Justify. Does the solution prevent Deadlock? Does this solution prevent mutual exclusion?

# Draw and explain the process state transition diagram.

4

# OR

# 4a) Implement the producer-consumer problem using monitor and discuss how the critical section requirements are fulfilled.

8

# Describe bankers algorithm with pseudo-code.

8

# 5.a) Consider the following processes:

| Process | Arrival Time | Burst Time |
| ------- | ------------ | ---------- |
| P1      | 0.0 ms       | 6 ms       |
| P2      | 0.5 ms       | 4 ms       |
| P3      | 1.0 ms       | 2 ms       |
| P4      | 1.2 ms       | 1 ms       |

Find the average turnaround time and average waiting time with respect to FCFS, SJF and Round Robin (quantum = 1 ms). Also draw Gantt chart for each algorithm.

# b) Discuss the design issues for multiprocessor scheduling.

6

# Compare and explain preemptive and non-preemptive CPU scheduling algorithms.

4

# OR


---



# 6.

a) What are the characteristics of real-time scheduling? Explain.

b) State and explain the scheduling criteria for uniprocessor scheduling.

c) Write an algorithm for scheduling the jobs using Short-Remaining Time Next (SRTN) Method.

# SECTION-Ⅱ

What is page fault rate? Explain with an example.

Compare and explain paging and segmentation.

Differentiate the contiguous and non-contiguous memory allocation.

OR

# 8.

a) Write short note on virtual memory management.

Explain in detail variable partitioning memory management.

Describe the following terms in brief:

- Principle of locality
- Thrashing.

# 9.

a) On a disk with 1000 cylinders numbers 0 to 999, compute the number of tracks the disk arm must move to satisfy all the requests in the disk queue. Assume the last request serviced was at track 756 and the head is moving toward 0. The queue in FIFO order contains requests for the following tracks: 811, 348, 153, 968, 407, 500.

What is the total distance that disk arm moves to satisfy all the pending requests for the following disk scheduling algorithms? (With the help of diagram).

- FIFO
- SSTF
- C-SCAN
- C-LOOK

Explain two-level, tree structured and acyclic graph directions.

# OR


---



# Current Page

# 1. Describe the following:

- I/O Buffering
- File sharing
- Record Blocking

Write short note on secondary storage management.

# 2. Explain the use of following built-in variables in awk programming:

- NR
- FS
- OFS
- NF
- FILENAME
- ARGC
- ARGV

# 3. How will differentiate between program threats and system threats?

Describe the following terms:

- Trojan Horse
- Virus

# OR

# 2.a) State and explain different methods used for implementing access matrix.

What do you understand by Unix shell? What are different shells in Unix? Explain.

