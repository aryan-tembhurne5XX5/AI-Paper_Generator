
# B.E. (Information Technology)

# MODERN COMPILERS

# (2012 Pattern) (Elective - I) (End Sem) (Semester - I)

Time : 2½ Hours

[Max. Marks : 70]

Total No. of Questions : 8

SEAT No. : P1873 [4859]-1063 [Total No. of Pages : 3]

# Instructions to the candidates:

1. Attempt Q1 or Q2, Q3 or Q4, Q5 or Q6, Q7 or Q8
2. Neat diagrams must be drawn wherever necessary.
3. Assume suitable data, if necessary.

# 1 a) Define callee-save and caller-save registers. How do the use of registers save time for programming languages? [6]

# b) Draw control-flow graph for the given code. Find the live ranges of a, b, c. [6]

a = 0
L1 : b = a + 1
c = c + b
a = b*2
if a &#x3C; N goto L1
return c

# c) Explain the terms Mutator and incremental garbage collection. Explain Tricolor Marking along with its algorithm. [8]

# OR

# 2a When we say that a "variable escapes"? For each variable a, b, c, d in the given program, find whether it escapes and why? [6]

int f(int a, int*b)
{
int c[3], d;
d = a + 1;
b = g(c, &#x26;b);
return c[1] + b;
}

P.T.O.


---



# 1)

# b)

Write Maximal Munch algorithm for optimal tiling instruction selection

# c)

and comment on its efficiency. [6]

Explain copying garbage collection with a neat diagram. Write Cheney's algorithm and comment on its cost. [8]

# 3)

# a)

Explain Higher-order functions and Functional programming language in brief. What are three flavors of Functional programming language? [6]

# b)

What is closure? How it can be implemented using Heap-allocation? [6]

# c)

Explain tail position with suitable example. Write the steps to implement tail call. OR [6]

# 4)

# a)

Define inline expansion. Explain the rules for inline expansion. [6]

# b)

Explain call-by-name and call-by-need with respect to lazy evaluation. [6]

# c)

Explain strictness analysis. [6]

# 5)

# a)

Explain Inter-procedural data-flow analysis in brief. Describe different functions for flow-insensitive side effect analysis. [8]

# b)

What are possible caches in a system? Describe different approaches for instruction-cache optimization. [8]

# OR

# 6)

# a)

Define call-graph. Draw call-graph for given code: [8]

Procedure f()
begin call g()

call h()
End
procedure g()
begin       call h()

end          call i()
procedure h()
begin
end
procedure i()
begin
end




---




# 7

b) What is inter-procedural optimization? Describe different kinds of inter-procedural optimizations. [8]

# 7a

What are reasons for variable aliases? Explain variable aliases based on type and based on flow. [8]

b) What is reaching definitions? Write in and out definitions for reaching definitions. [8]

# OR

# Q8

a) Explain transformations using dataflow analysis using suitable examples. [8]

b) Explain explicit and implicit parametric polymorphism with suitable examples. [4]

c) Draw IR tree representation and quadruple: a = b[i] + c. [4]

