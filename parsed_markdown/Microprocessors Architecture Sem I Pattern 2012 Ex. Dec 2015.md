
# S.E. (Computer Engineering) (First Semester)

# EXAMINATION, 2015

# MICROPROCESSOR ARCHITECTURE

# (2012 PATTERN)

Total No. of Questions: [Total No. of Printed Pages]

Seat No.: [4857]-1075

Time: Two Hours

Maximum Marks: 50

N.B. Answer any four questions




---



# Explain four level of hierarchical protection in 80386 Dx microprocessor

The 80386 Dx microprocessor implements a four-level hierarchical protection mechanism to enhance system security and stability. The four levels are:

1. Ring 0: This is the highest privilege level, typically used by the operating system kernel. It has unrestricted access to all system resources.
2. Ring 1: This level is used for device drivers and other system services that require more privileges than user applications but less than the kernel.
3. Ring 2: This level is often used for system utilities and services that need to interact with the hardware but do not require full kernel access.
4. Ring 3: This is the lowest privilege level, used for user applications. It has the least access to system resources, ensuring that user programs cannot interfere with the operating system or other applications.

# Draw and explain the architecture of 8086 microprocessor

The architecture of the 8086 microprocessor consists of several key components:

- ALU (Arithmetic Logic Unit): Performs arithmetic and logical operations.
- Registers: Includes general-purpose registers, segment registers, and special-purpose registers.
- Control Unit: Directs the operation of the processor and coordinates the activities of the other components.
- Bus Interface Unit: Manages data transfer between the CPU and memory or I/O devices.

# What is maximum size of each segment in 80386 Dx microprocessor? Why

The maximum size of each segment in the 80386 Dx microprocessor is 4 GB. This is due to the 32-bit addressing capability of the processor, which allows it to address a total of 232 bytes of memory. Each segment can thus be defined to occupy a maximum of 4 GB of addressable space.




---




# Advantages of Multicore Design

- Improved performance through parallel processing.
- Better energy efficiency compared to single-core processors.
- Enhanced multitasking capabilities.
- Scalability for future applications and workloads.
- Reduced heat generation per core.

# Multiprocessor Architectures

Multiprocessor architectures can be categorized into several types:

- Symmetric Multiprocessing (SMP)
- Asymmetric Multiprocessing (AMP)
- Clustered Multiprocessing
- Massively Parallel Processing (MPP)

# Front Side Bus and Back Side Bus

The front side bus (FSB) is the main pathway for data communication between the CPU and the main memory. The back side bus (BSB) is used to connect the CPU to the cache memory, allowing for faster access to frequently used data.

# Instruction Sets for I-A-64 Architecture

The I-A-64 architecture supports various instruction sets, including:

- Integer instructions
- Floating-point instructions
- Load/store instructions
- Branch instructions

