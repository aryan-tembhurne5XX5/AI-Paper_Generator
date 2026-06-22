
# May 2024 (ENDSEM) EXAM

# TY (SEMESTER - II)

# COURSE NAME: Language Processor

# Branch: Computer Engineering

# Course Code: CSUA32207

# compiler construction (PATTERN 2020)

# Time: [1Hr. 30 Min] [Max. Marks: 40]

Instructions to candidates:

- Figures to the right indicate full marks.
- Use of scientific calculator is allowed.
- Use suitable data wherever required.
- All questions are compulsory. Solve any one sub question from Question 3 and any two sub questions each from Questions 4, 5 and 6 respectively.

| Q. No. | Question Description                                                                                                                                                                                                                                   | Max. Marks | CO   | BT Level   | |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---- | ---------- |---|
| Q.1    | a) Discuss and Describe the Pass Structure of an Assembler?                                                                                                                                                                                            | \[2]       | CO 1 | Understand | |
| Q.2    | Differentiate between absolute and direct linking loader?                                                                                                                                                                                              | \[2]       | CO 2 | Understand | |
| Q.3    | a) How does LEX handle conflicts or ambiguities in the specification? With appropriate example, discuss strategies to resolve such issues effectively during the generation of a lexical analyzer?                                                     | \[6]       | CO 3 | Apply      | |
|        | b) Discuss the method of input buffering for speed reading during the lexical analysis. How does buffering improve the performance of the lexical analyzer, especially when dealing with input from external sources such as files or network streams? | \[6]       | CO 3 | Apply      | |
| Q.4    | a) Apply LL(1) Parser for the below Grammar and construct First, Follow and make a Parser Table and show whether the Grammar is Feasible or Not Feasible?                                                                                              | \[5]       | CO 4 | Apply      | |
|        | E → TE'                                                                                                                                                                                                                                                |            |      |            | |
|        | E' → +TE' \| ε                                                                                                                                                                                                                                         |            |      |            |
|        | T → FT                                                                                                                                                                                                                                                 |            |      |            | |
|        | T' → \*FT' \| ε                                                                                                                                                                                                                                        |            |      |            |
|        | F → id \| (E)                                                                                                                                                                                                                                          |            |      |            |
|        | \*ε denotes epsilon                                                                                                                                                                                                                                    |            |      |            | |
|        | Consider the grammar                                                                                                                                                                                                                                   |            |      |            | |
|        | E → 2E2                                                                                                                                                                                                                                                | \[5]       | CO 4 | Apply      | |
|        | E → 3E3                                                                                                                                                                                                                                                |            |      |            | |
|        | E → 4                                                                                                                                                                                                                                                  |            |      |            | |
|        | Perform Shift Reduce parsing for input string "32423"                                                                                                                                                                                                  |            |      |            | |




---



# Predictive Parser

E -> E + T
T -> T * F | F
F -> ( E ) | id

# Q.5

# a)

Generate the three-address code for the following code.

While (A &#x3C; C and B > D)
do if A == 1 then c = c + 1
else
while A &#x3C;= D
do A = A + B

# b)

Generate the 3-address code for the following expression:

Result = P * (Q - R) + 2 * (Q - R - 100)

and represent 3 address code using quadruple, triple and indirect triple.

# c)

Generate the three-address code for the following code. Explain how a three-address code is represented.

sum = 0
for (i = 0; i &#x3C;= 20; i++)
sum = sum + X[i] + Y[i]

# Q.6

# a)

Which different optimization technique will you apply in each of the following 5 separate sample code snippets and what will be the result after optimization of each?

A = B * C
int main() {
for(int i = 0; i &#x3C; 10; i++) {
num = 10;
cout &#x3C;&#x3C; "LPCC";
}
return 0;
}
D = B // D not used further
E = A * B + 4
A = 10.4
B = A / 1.3
if (A) go to L1;

# b)

Generate a DAG for the expression below and explain how and why common subexpressions need to be eliminated. What other information does DAG provide which is useful for code optimization?

A + B * D + B * D + C

# c)

Apply the technique used to partition three address code into basic blocks and construct the flow graph for a function which calculates factorial of a number.

