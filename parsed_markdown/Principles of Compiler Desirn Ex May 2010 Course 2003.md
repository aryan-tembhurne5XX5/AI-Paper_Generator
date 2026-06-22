
# B.E. (Computer Engineering)

# PRINCIPLES OF COMPILER DESIGN

Time: 3 Hours

Max. Marks: 100

Total No. of Questions: 12

Total No. of Pages: 3

P1375

[3764] - 414

# Instructions to the candidates:

1. Answers to the two sections should be written in separate books.
2. Neat diagrams must be drawn wherever necessary.
3. Figures to the right indicate full marks.
4. Your answers will be valued as a whole.
5. Assume suitable data, if necessary.

# SECTION - I

1. a) Compare Compiler and Interpreter. [4]

b) Define following: i) Incremental Compiler [4]

ii) Cross compiler

c) Write a LEX program for a subset of C. [8]
2. OR

a) Explain various Compiler Construction tools. [8]

b) Write a LEX program to calculate number of words in the input C file. Program also should remove comments from the program. [8]
3. a) Construct LALR parsing table for following grammar. [10]

S -> AA

A -> aA

A -> b

b) Explain operator precedence parser. [8]
4. OR

a) Show that following grammar is LL(1) but not SLR(1). [9]

S -> AaAb | BbBa

A -> E

b) B -> E [9]

Write a YACC program for a simple calculator.

P.T.O.




---



# Q5)

a) Explain what is inherited and synthesized attributes. With example explain how these are calculated. [8]

Write Quadruple and Triple representation for following expression. [8]

A=B+C*D/E+-F*-G

OR

# 6)

a) Write intermediate code generated for following sentences. [8]

While a &#x3C; b do

If c &#x3C; d then

x = y + z

Else

x = y - z

Explain with example concept of backpatching [8]

# SECTION - II

7a) What is the need of Activation record? With example explain how these are generated. [8]

b) With example explain different parameter passing methods. [8]

OR

# 8a

Enlist and explain in short different ways of accessing non-local names. [8]

What are different storage allocation strategies. Explain any one in detail.

b) [8]

# Q9)

a) Explain peephole optimization in detail. [8]

b) Explain the dynamic programming code generation algorithm. [8]

OR

# Q10)

a) Explain various transformations that can be done on basic blocks. [8]

Write a note on code generator generators. [8]

# QI1)

a) With example explain different types of loops in flow graph. [8]

b) What is the need of code optimization? Discuss principal sources of code optimization. [10]




---



# Q12

# a)

For the following three address code statements [10]

1. PROD = 0
2. 1 = 1
3. T2 = ADDR(A) - 4
4. T4 = ADDR(B) - 4
5. T1 = 4 * I
6. T3 = T2[T1]
7. T5 = T4[T1]
8. T6 = T3 * T5
9. PROD = PROD + T6
10. I = I + 1
11. IF (I &#x3C;= 20) GOTO (V)

Compute basic blocks and draw the flow graph.

# b)

Discuss algorithm for live variable analysis [8]

