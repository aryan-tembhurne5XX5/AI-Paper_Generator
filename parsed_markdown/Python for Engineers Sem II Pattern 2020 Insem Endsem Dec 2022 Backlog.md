
Total No. of Questions - [3]                         Total No. of Printed Pages: 4
G.R. No.                                                PAPER CODE       U112-202BCBE
DEC-2022 (INSEM+ ENDSEM) EXAM
F.Y. B. TECH. (SEMESTER - II)
COURSE NAME: PYTHON FOR ENGINEERS
COURSE CODE: CS10202B
(PATTERN 2020)
Time: [2Hr}                                                           [Max. Marks: 60]

(*) Instructions to candidates:

1. Figures to the right indicate full marks.
2. Use of scientific calculator is allowed
3. Use suitable data where ever required

# Q1 Solve the following[30]

1. i. What will be the output of the following Python code? [2]

print("Viit" > "VIIT")
print("Pune" &#x3C; "PUNE")

TrueFalseTrueTrueFalseFalseNameError
2. ii. What will be the output of the following Python code? [2]

a=["A","B","C",["D"]]
b=list(a)
a[3][0]="11"
a[1]="F"
print(b)

)[ [A',B', 'C', [11]]    ) [A', F", 'C', [11]]

c)A, F, 'C', [D']]       d)AttributeError
3. iii. What will be the output of the following Python code? [2]

numbers = [32, 13, 5, 77]
numbers.sorted(reverse=True)
print(Reversed List:',numbers)

)Reversed List: [77, 32, 13, 5]b)[77, 32, 13, 5]

AttributeError                          NameError
4. iv. What will be the output of the following Python code? [2]

12=[9,10,3,4,"ABC",5]
12.insert(2,[11.0,13.0])
print(12)

a) [9, 10, [11.0, 13.0], 3, 4, 'ABC', 5]

b) [[9, [11.0, 13.0],10, 3, 4, 'ABC', 5]

c) [[9, (11.0, 13.0),10, 3, 4, 'ABC', 5]

d) [[9, 10,( 11.0, 13.0), 3, 4, 'ABC', 5]




---



# v.

What is the output of the following? [2]

A=[12,14,15]

B=[12,14]

A<b< p="">
</b<>
a) False

b) True

c) Invalid Operation

d) [1,2]

# vi.

What is the output of the following code [2]

D1= dict(('college', "VIT"),('city', "Pune"), ('Pincode', 411039))

print(D1)

{'college': 'VIT', 'city': 'Pune', 'Pincode': 411039}

a) Options: SyntaxError: invalid syntax

b) ('college', 'VIT'), ('city', 'Pune'), ('Pincode', 411039)

c) ['college', 'VIT', 'city', 'Pune', 'Pincode', 411039]

# vii.

Select the correct output of the following String operations [2]

txt = "I love Python, Python is my favorite subject"

x = txt.count("Python", 10, 22)

print(x)

a) 1

b) 2

c) SyntaxError

d) No output

# viii.

Which of the following will give "Engineering " as output? [2]

str1="VIIT,Engineering,Pune"

a) print(str1[-5:-16])

b) print(str1[-17:-5])

c) print(str1[-16:-5])

d) print(str1[-5:-17])

# ix.

Select which is True for for loop [2]

a) Python's for loop used to iterates over the items of list, tuple, dictionary, set, or string is executed when the loop terminates

b) else clause of for loop naturally

c) else clause of for loop is executed when the loop terminates abruptly

d) We use for loop when we want to perform a task indefinitely until a particular condition is met

# x.

What is the output of the following range() function [2]

for num in range(2,-5,-1):

print(num, end=", ")

a) 2, 1, 0

b) 21, 0

c) 2, 1, 0, -1, -2, -3, -4, -5

# xi.

What is the output of the following [2]

a= [1, 2, 3, 4, 5]

for i in range(1, 5):

a[i-1]= a[i]

for i in range(0, 5):

print(a[i], end = "")

a) 23451

b) 5 1 2 3 4

# xii.

What will be the output of the following Python code? [2]

lst=[3,4,6,1,2]

lst[1:2]=[7,8]

print(lst)

a) [3, 7, 8, 6, 1, 2]

b) Syntax error

c) [3,[7,8],6,1,2]

d) [3,4,6,7,8]




---



# xiii. What will be the output of given Python code? [2]

S='cppbuzzchicago
print(S[-3:-15:-2])

- a) aiezbp
- b) aiezbpp
- c) caiczb
- d) pbzcia

# xiv. A while loop in Python is used for what type of iteration? [2]

- Indefinite
- Discriminant
- c) definite
- d) indeterminate

# xv. Select which is true for Python function [2]

1. A function is a code block that only executes when it is called.
2. Python function always returns a value.
3. A function only executes when it is called and we can reuse it in a program.
4. Python doesn't support nested function.

- a) 1, 2, 3, 4
- d) 2

# Q2 Solve any three out of four

# a. Differentiate between import and 'from import' in Python with example? [5]

Write a NumPy program to count the number of "p" in a given array, element-wise.

Original Array: ['Python' 'POPULER' 'VIIT' 'F.Y.' 'BteCh']
Expected Output: [1 2 0 0 0]

# b. Reshape the given input to 2 rows and 2 columns and Write a python code to get addition of all elements, row wise and column wise in a numpy array? [5]

Input: [14, 15, 13, 17]
Expected Output 1: sum= 111
Expected Output 2: sum= [27 32]
Expected Output 3: sum= [29 30]

# c. Reshape the given input to 3 rows and 3 columns and Write a python code to

1. a) get sum of second column only
2. b) to find minimum and maximum values from each row and columns respectively

Input: Original Array= [14 13 15 12 11 16 17 19 18]
Expected Output:
a) Reshaped Array= [[[14 13 15]
[12 11 16]
[17 19 18]]
1st column_sum= 43
b) Min from each row: [13 11 17]
Max from each col [17 19 18]




---



# Q3 Solve any three out of four

# a. Describe working of open(), read(), write(), split() and close() function in file handling with example.

[5]

# b. Write a user defined function Even_Lines() to display even number lines from the text file. Consider file name as - data.txt.

[5]

Input:

Nothing is impossible. The word itself says I'm possible!

There is nothing impossible to they who will try.

The bad news is time flies. The good news is you're the pilot.

Keep your face always toward the sunshine, and shadows will fall behind you.

# c. Write a function count_word() to count and display the total number of words from the file. Consider file name as - data.txt

[5]

Input:

Nothing is impossible. The word itself says I'm possible!

There is nothing impossible to they who will try.

The bad news is time flies. The good news is you're the pilot.

Keep your face always toward the sunshine, and shadows will fall behind you.

# d. Consider following lines for the file data.txt and predict the output:

[5]

Input:

Nothing is impossible. The word itself says I'm possible!

There is nothing impossible to they who will try.

The bad news is time flies. The good news is you're the pilot.

Keep your face always toward the sunshine, and shadows will fall behind you.

Program:

f = open("data.txt")
l1 = f.readline()
l2 = f.readline(20)
ch3 = f.read(12)
print(l2)
print(ch3)
print(f.readline())
f.close()

