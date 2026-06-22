
Total No. of Questions : 12]            [3664] - 335  [Total No. of Pages : 3
P1365

# B.E. (Computer Engineering)

# OPERATING SYSTEMS

# sem- 1

# (2003 Course) (410442)

Time : 3 Hours

[Max. Marks : 100]

# Instructions to the candidates:

1. Answer all questions from each section.
2. Answers to the two sections should be written in separate books.
3. Figures to the right indicate full marks.
4. Neat diagrams must be drawn wherever necessary.
5. Assume suitable data, if necessary.

# SECTION - I

# 1a

What is busy waiting with respect to process synchronization? Explain how semaphore reduces the severity of this problem. Also define with examples:

- General semaphores.
- Binary semaphores.
- Strong semaphores.
- Weak semaphores.

[8]

What is bounded buffer Producer/Consumer problem? Write a solution using monitors. [8]

OR

# Qa)

Jurassic Park consists of a dinosaur museum and a park for safari riding. There are m passengers and n single passenger cars. Passengers wander around the museum for a while, then line up to take a ride in a safari car. When a car is available, it loads the one passenger it can hold and rides around the park for a random amount of time. If the n cars are all riding passengers around, then a passenger who wants to ride waits; if a car is ready to load but there are no waiting passengers, then the car waits. Use semaphores to synchronize the m passenger processes and the n car processes. [8]

# b)

What is basic requirement for execution of concurrent processes? Explain how concurrency is achieved in uniprocessor system. What is distinction between competing and cooperating processes? [8]

P.T.O.



---




# Q3)

a) State and explain different methods used for implementing access matrix. Why access matrix is required? [8]

Apply the deadlock detection algorithm to the following data and show the results. [8]

| Available  | (2 1 0 0) |
| ---------- | --------- |
| Request    | 1 0 1 0   |
| Allocation | 2 0 0 1   |
|            | 2 0 0 1   |
|            | 0 0 1 0   |
|            | 2 1 0 0   |
|            | 0 1 2 0   |

Also state advantages and disadvantages of the algorithm.

OR

# 4)

a) What is deadlock? Explain and compare various techniques to handle deadlock? [8]

Describe two approaches to intrusion detection. What does an audit record contains? [8]

# 5)

a) Explain with neat diagram UNIX file system structure and its characteristics. [6]

system call. Define system throughput as the number of processes the system can execute in a given time period. Describe how the buffer cache can help response time. Does it necessarily help system throughput. [6]

Explain with neat diagram structure of a buffer pool. [6]

OR

# Qa)

Explain various UNIX kernel components, their responsibilities and their inter relationship with each other. [10]

Describe with example various building block primitives of UNIX system. [4]

c) Write an algorithm for bwrite. [4]

# SECTION - II

# Q7)

a) Write and explain algorithm for mount system call. Also state the mount table entries. [10]

When opening a named pipe for reading a process sleeps in the open until another process opens the pipe for writing. Why? [4]




---



# c) Compare the access permissions a process must have for following operations and comment -

- i) Creating a new file requires write permission in a directory.
- ii) Unlinking a file requires write permission in the directory, not on a file. [4]

# OR

# 8a) Write and explain the algorithm to convert a pathname to an inode. [8]

# b) Explain the structure of a regular file in UNIX. [4]

# c) What are the link files? What are the types of links? Compare between them. [6]

# Q9) a) Explain the following process concepts with suitable example - [8]

- i) Signals.
- User ids of a process. [8]

# b) What is context of a process explain in detail?

# OR

# Q10)a) What is kernel profiling explain in brief? [4]

# b) Explain with example process scheduling. [6]

# c) List out various kernel level data structure used in process subsystem with its fields and inter relationship. [6]

# Q11)a) Explain how stream provide greater modularity and flexibility for the I/O subsystem. [6]

# b) Explain page stealer process in UNIX. [4]

# c) Explain allocation of swap space in UNIX. [6]

# OR

# Q12)a) How page faults are handled in UNIX? [6]

# b) Why is it advantageous to schedule the child process before the parent after a fork call if copy on write bits are set on shared pages? How can kernel force the child to run first? [4]

# c) Write a note on terminal drivers. [6]

