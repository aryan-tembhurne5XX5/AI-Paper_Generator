
# B.E. (Electronics)

# REAL TIME OPERATING SYSTEMS

Time : 3 Hours (2003 Course) (Elective - II) (404212)

[Max. Marks : 100]

Total No. of Questions : 12

Total No. of Pages : 3

P 1276 [3864] - 253

# Instructions to the candidates:

1. Answers to the two sections should be written in separate answer books.
2. In Section-I attempt Q.1 or Q.2, Q.3 or Q.4 and Q.5 or Q.6 in Section-II attempt Q.7 or Q.8, Q.9 or Q.10 and Q.11 or Q.12.
3. Neat diagrams, flow charts must be drawn and well commented pseudo code written wherever necessary.
4. Figures to the right indicate full marks.
5. Assume suitable data, if necessary.

# SECTION - I

# Q1)

# a)

Discuss the memory requirements in foreground / background and multi tasking system. [8]

Explain clock tick in multitasking system. What are the constraints in selection of the clock tick in multitasking system? How accurate time this can give? [8]

# OR

# a)

What is RMS theorem? How it is useful in assigning tasks priorities? Check whether the following set of periodic real-time tasks is schedulable under RMS on a uniprocessor system : T = (e1 = 20, p1 = 100),

b) T2 = (e2 = 30, p2 = 150), T3 = (e3 = 60, p3 = 200). [8]

Discuss interrupt and interrupt timings for foreground / background, non-preemptive and preemptive kernel. [8]

# 3)

# a)

Explain, Locking and unlocking of scheduler in uCOSII, Nesting of scheduler lock, Possible situation and precautions while using scheduler lock/unlock. [8]

# b)

What is the use of following members of OS_TCB? And how they are manipulated? [8]

INT8U OSTCBX;

INT8U OSTCBY;

INT8U OSTCBitX;

INT8U OSTCBitY;




---



# Qa) Explain, what is ready list in uCOSII? How uCOSII add the task in the ready list? How uCOSII remove a task from ready list?

[8]

# structure OS-EVENT.

[8]

# 5a Write short note on any two:

[6]

- iSemaphore management in uCOSII.
- iiMutual exclusion semaphore in uCOSII

# b) iiEvent flag management in uCOSII.

[6]

Explain in detail OSMutexCreate().

# c) Enlist different MUTEX services. What configuration constants provided to configure MUTEX?

[6]

# OR

# 6a Explain Event Flag Group data structure OS_FLAG_GRP and OS_FLAG_NODE.

[6]

# Write short note on any two:

[6]

- iSemaphore management in uCOSII.
- iiMutual exclusion semaphore in uCOSII.

What is relationship between Task, ISR and Semaphore in uCOSII?

[6]

# SECTION- II

# Q7)a) How to use Mailox as binary semaphore? Explain by using pseudo code.

# b)

[6]

What is relationship between Task, ISR and Message Queue in uCOSII?

[6]

# c) What are message queue services in uCOSII? How Message Queue services enabled/disabled in uCOSII.

[6]

# OR

# 8a Explain the relationship between tasks, ISR and message queue.

[6]

# b) What are the features of message queue in uCOSII?

[6]

# c) Explain Mailbox services and configuration in uCOSII.

[6]

# 9a Explain Memory Control Block data structure OS_MEM.

[4]

# b) Explain memory partition and multiple memory partition in uCOSII.

[4]

# c) Define porting of uCOSII. What requirements the processor should satisfy to run uCOSII.

[4]

What is testing of port? What are the steps to follow for testing of port?

# OR

[4]




---



# Q10)

a) Explain the need of memory management services by OS as compare to compiler functions. [4]

them. [4]

c) How OS_CPU.H makes uCOSII processor and implementation specific?

d) Explain uCOSII hardware/software architecture. [4]

[4]

# Q11)

Answer the following by considering the implementation of temperature controller.

a) Define the hardware architecture for the system. [4]

c) Define the tasks for the system and assign the tasks priority and explain. [4]

d) Enlist the services of uCOSII required in the system. [4]

Write the application software for the system. [4]

OR

# Q12)

Answer the following by considering the implementation of chocolate vending machine.

a) Define the hardware architecture for the system. [4]

Define the tasks for the system and assign the tasks priority and explain. [4]

c) Enlist the services of uCOSII required in the system. [4]

d) Write the application software for the system. [4]

