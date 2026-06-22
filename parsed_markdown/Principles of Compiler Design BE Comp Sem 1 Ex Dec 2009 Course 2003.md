
# B.E. (Computer Engg.)

# PRINCIPLES OF COMPILER DESIGN

# (2003 Course) (410444) sem 1

Time : 3 Hours

Max. Marks : 100

Total No. of Questions : 12

Total No. of Pages : 3

# Instructions to the candidates :

1. Answers to the two sections should be written in separate answer books.
2. Neat diagrams must be drawn wherever necessary.
3. Figures to the right indicate full marks.
4. Your answers will be valued as a whole.
5. Assume suitable data, if necessary.

# SECTION - I

# 1a

Write a Lex specification to read a C program and calculate number of new line characters, tabs and white spaces in the program. [8]

# b)

Whether lexical analysis detects any errors? Explain with example. [8]

# OR

# Q2)

# a)

Explain with example various Compiler Construction tools. [9]

# b)

Why compilation phases are divided into front-end and back-end? What are the advantages? [4]

Explain the following: [3]

- itoken.
- iilexeme.
- pattern.

# a)

Show that the following grammar is LR(1) but not LALR(1). [10]

S → Aa | bAc | Bc | bBa

A → d

B → d

# Explain Recursive Descent parser with an example [8]

# OR

# 4)a

Show that following grammar is LL(1) but not SLR(1). [8]

S → AaAb | BbBa

A → ε

B → ε

P.T.O.


---



# Resolved? With examples explain in which condition S-R and R-R conflict can occur in SLR, canonical LR and LALR parsers. (Make use of LR(O), LR(1) items).

[10]

# 5a

Write a translation scheme to generate three address code for assignment sentences with array and pointer references.

[8]

Explain concept of back-patching with example.

[8]

# OR

# 6a

Translate executable sentences of the following C program.

[8]

main ( )
{
int i = 1;
int a[10];
while(i &#x3C;= 10)
{
a[i]=0;
i = i + 1;
}
}

into syntax tree, postfix notation, three-address code.

# b)

What are synthesized and inherited attributes? What are Marker Non-terminal symbols? Give example.

[8]

# SECTION - II

# 7a)

With example explain different parameter passing methods.

[8]

Explain Runtime support and Storage organization.

[8]

# OR

# Q8)

a) What are different storage allocation strategies? Explain anyone in detail.

[8]

What is "Display" mechanism? Explain it with example.

[8]




---



# 9

a) What is a basic block and flow graph? Generate three address code for the following program. Find the basic blocks in it and write flow graph for the same.

begin
prod := 0;
i := 1;
do
begin
prod := prod + a[i] * b[i];
i := i + 1;
end
while i &#x3C;= 20
end

[8]

b) What is next use information explain in detail. [8]

OR

# Q10

a) Explain peephole optimization in detail. [8]

b) What is a DAG? Explain role of a DAG in code generation phase. [8]

# Q11

a) What is the need of code optimization? Discuss principal sources of code optimization. [10]

b) Discuss algorithm for live variable analysis. [8]

OR

# Q12

a) Enlist and explain with example various transformations on basic blocks. [8]

b) With example explain what is Global Common Sub-expression? Write algorithm for Global Common Sub-expression Elimination. [10]

