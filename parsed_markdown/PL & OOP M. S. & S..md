Marking Scheme U218-146(TL)

# 1)

# a)

Six steps of problem solving - Each step carry one mark. [6]

# b)

To addition of digits. [6]

Flow chart - 3 marks

Algorithm - 3 marks

# c)

Definition of problem - 2 marks [4]

Ways to solve problem - 2 marks

# OR

# Q2)

# a)

Different strategies for algorithm design - explanation with example [6]

# b)

Write output of following functions [6]

| Sign(0)         |           |
| --------------- | --------- |
| Abs(-8)         | 8         |
| String(-345.88) | "-345.88" |
| Max(5,7,8,9)    | 9         |
| Mid(s,3,2)      | ea        |
| Right(s,3)      | ater      |

where s=theater

# c)

Need of function - at least four points each carry 1 mark. [4]

# Q3)

# a)

List down major types of module and explain their function with example

List of types of module - 2 marks [6]

Function with example - 4 marks [4]

# b)

Correct decision table carries four marks

# c)

Case structure explanation with flowchart 2 marks [4]

Example - 2 marks

# OR

# a)

Explain three decision logic structure with example [6]

# Q4)

# a)

Explanation with example.

# b)

In a multiplex the charges for a movie varies according to the age of the persons. Using the positive logic, develop a solution to print the ticket changes given the age of person. [4]

Solution in the form of flowchart or algorithm

Call by value 2 marks [4]

Call by reference 2 marks




---


U218-146(T1)
# Solution

1. The six steps of problem solving include the following:

# Draw a flowchart and write an algorithm to find addition of digits.

# Flowchart

START
SUM=0
READ N
N1=07 FALSE
TRUE
REM=N%10
SUM=SUM+R
N=N/10
PRINT SUM
END

# Algorithm

1. Step 1: Input N
2. Step 2: Sum = 0
3. Step 3: While (N != 0)
4. Rem = N % 10;
5. Sum = Sum + Rem;
6. N = N /10;




---


# Step 4: Print Sum

# c) What is meant by problem? What are the ways to solve problem [4]

A problem can present itself in many forms. Examples of problems are as follows:

- Question: What movie should we see?
- Need to do something: Generate the monthly payroll.
- Obstacle to progress: A part is missing that is causing work to halt on a project.
- Status of a process: What is the status of the project?
- What-if simulation: How much money needs to be deducted from each pay check to save for a down payment on a car?
- Evaluation of a solution to another problem: Should traveling be done by train or car?
- Lack of information: How much money is left on the mortgage?
- Undesirable state: A person has gone into debt.
- Lack of control: A company has decided to downsize.

There are many ways in which a problem can be solved. The following are some of the possibilities:

- Algorithm: An algorithm is a series of steps used to arrive at an outcome that represents the best answer to a problem. It is a specification of a behavioral process. An algorithm is a finite set of instructions that govern a behavior step by step, such as the manipulation of data. Problems that require algorithms are often the problems that computers solve best.
- Heuristic solutions: Heuristic solutions involve the use of human ingenuity and reasoning. They are based on learning through experience.


---



# Passing of time: Some problems are solved simply by the passing of time

An undesirable state may change, or it may no longer be a problem.

# Gaining resources: The solution to a problem may be more resources—such as

more money, time, or people

OR [6]

# Q2a Explain different strategies for algorithm design

# Strategies to solve the problem: brute force, greedy, divide and conquer and backtracking.

# Brute Force

The brute force method of algorithm design is intended to bring into mind hammering a screw into a board of wood. The solution may not be elegant or efficient, but it will work. Generally, this involves considering every aspect of every element of an array, regardless of whether each element is important. It is an exhaustive, programmatic consideration of everything, which takes time. Generally, brute force methods are inefficient but still serviceable in many situations.

# Greedy

Greedy algorithms involve considering the largest portion of the problem set first. For example, if the problem considers how to pack a set of items into a bag or a box, the greedy method would put the largest item in first followed by the second largest, and so forth. The greedy method will occasionally find an efficient method; however, more often than not, the solution will be similar to a brute force method.

# Divide &#x26; Conquer

Suppose that a problem involved shuffling a deck of cards. It could be determined that a deck of cards is shuffled if each half of the deck is shuffled and randomly recombined. Due to the fact each half could be




---



considered a deck, what occurs is a recursive solution. The only component left to define is the base case, which would say that the dividing of decks stops when the deck only consists of one card. Afterwards, each subdeck could be randomly combined to reproduce the larger deck. This could be continued until the full deck is shuffled. This method is called divide and conquer, when the algorithm seeks to divide the problem into smaller problems which are, in turn, solved in the same manner.

# Back Tracking

A method often called backtracking is one other possibility toward finding an efficient solution by starting with the solution and finding the problem. If an algorithm can be developed that takes an appropriate solution and slowly takes parts of it away until it comes to the problem and the algorithm can be reversed, it is sometimes possible to determine an efficient solution to a problem.

)Write output of following functions [6]

- 1.Sign(0) : 0
- 2.Abs (-8): 8
- 3.String(-345.88) : "-345.88"
- 4.Max (5,7,8,9) : 9
- 5.Mid(S,3,2)ea
- 6.Right(s,3) ater where s=theater

# What is the need of function? [4]

- Modularize a program
- Divide and conquer
- Manageable program development
- Software reusability




---



# Use existing functions as building blocks form new programs

- Abstraction-hide internal details (library functions)
- Avoid code repetition

# Q3) a) List down major types of module and explain their function with example. [6]

# Types of modules

The control module: It shows the overall flow of the data through the program. All other modules are subordinate to it.

The initialization modules: Processes instructions that are executed only once during the program, and only at the beginning. These instructions include opening files and setting the beginning values of variables used in processing.

The Process modules: may be processed only once, or they may be part of a loop, which is processed more than one during the solution. There are several kind of Process modules:

- Calculation modules
- Print modules
- Read and data validation modules

Wrapup modules: Process all instructions that are executed only once during the program and only at the end. These instructions include closing files and printing totals, among others.

Modules in an object-oriented program may include event modules such as mouse down, mouse up, key entry, &#x26; so on.

# b) Draw a decision table for the following set of conditions for gross income tax and rate:


---




# Tax Rate Structure

1. Gross &#x3C;= 5,000 tax rate 5%
2. Income between 5,000 - 10,000 tax rate 8%
3. Income between 10,000 - 15,000 tax rate 10%
4. Gross > 15,000 tax rate 15% [4]

# Decision Table

| Solution                       | Rate |
| ------------------------------ | ---- |
| Gross <= 5,000                 | 5%   |
| Income between 5,000 - 10,000  | 8%   |
| Income between 10,000 - 15,000 | 10%  |
| Gross > 15,000                 | 15%  |

# Case Structure Explanation

Explain case structure with flowchart and example [4].

Is similar to a series of If/Then/Else statements.

Positive Logic

Syntax:

Select Case testvalue
Case value1
statement group 1
Case value2
statement group 2
End Select

Case True Case a action




---


# Case b action

# Case Else action

# Case Example

Select Case Grade
Case 90...100
LetterGrade = "A"
Case 80..89.9
LetterGrade = "B"
Case 70..79.9
LetterGrade = "C"
Case 60..69.9
LetterGrade = "D"
Else
LetterGrade = "F"
End Select

# Q4) a) Explain three decision logic structure with example [6]

# Straight-through Logic

All decisions are processed sequentially, one after another. Least efficient, but most thorough.

# Positive Logic

Processing flow continues through the module instead of processing succeeding decisions, once the result is True.

# Negative Logic

Flow is based on result being False. Nested decisions use Positive or Negative, but not Straight-through.


---



# Straight-through Logic

All conditions are tested.

Least efficient, but most exhaustive.

| F | T |
| - | - |
| F | T |

# Positive Logic:

Uses If/Then/Else instructions

Continues processing based on True results




---



# Grade Evaluation Logic

| F Grade >= 90 | T    |
| ------------- | ---- |
| F Grade >= 80 | ="A" |
| F Grade < 90  | T    |
| F Grade < 80  | ="B" |

# Negative Logic:

Executes process based on False

Processes another decision when the result is True

| F Grade < 90 | T       |
| ------------ | ------- |
| F Grade < 80 | ="A"    |
| LtrG         | LtrG =  |
| ="B"         | "Other" |




---


b) Using positive logic, solve the following set of conditions to calculate hotel bill: [4]

1. Sales of eatables up to 100 Rs., 11% discount
2. Sales of eatables up to 1000 Rs., 22% discount
3. Sales of eatables up to 10000 Rs., 33% discount

As per attached sheet

c) What are the parameter passing techniques? [4]

# Call by Value

Calling a function with parameters passed as values

int a=10;
void fun(int a)
fun(a);

Here fun (a) is a call by value. Any modification done within the function is local to it and will not be affected outside the function.

# Example program - Call by value

#include<stdio class="h">
void main() {
int a=10;
printf("%d",a);          // a=10
fun(a);                  // a=10
printf("%d",a);
}
void fun(int x) {
printf("%d",x);        // x=10
x++;                    // x=11
}
printf("%d",x);
</stdio>
# Call by reference

Calling a function by passing pointers as parameters (address of variables is passed instead of variables)

int a=1;
void fun(int *x)
fun(&#x26;a);

Any modification done to variable a will affect outside the function also.


---



Example Program - Call by reference

#include<stdio class="h">
void main()
{
int a=10;
printf("%d",a);    a=10
fun(8&#x26;a);
printf("%d",a);     a=11
}

void fun(int *x)
{
printf("%d",x);      $x=10
x++;
printf("%d",x);      x=11
}
</stdio>




---


# Flow chart

| L   | T        |
| --- | -------- |
| F   | Discount |
| upt | 1000     |
| F   | Discout  |
| t   | Ofo      |
| f   | Discount |
|     | 33       |

# Algorithm

If sales &#x3C;= 100

elseif Discount = 11%

ebse if Discount = 22%

sales > 0 O Sules = 10,000

Discount = 33%