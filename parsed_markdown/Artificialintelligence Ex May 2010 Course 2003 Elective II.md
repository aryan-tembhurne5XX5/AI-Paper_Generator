Total No. of Questions : 12] [Total No. of Pages : 4

P1383 [3764]-441

B.E. (Information Technology)
ARTIFICIAL INTELLIGENCE
(2003 Course) (Elective - II) (414451)

Time : 3 Hours] [Max. Marks : 100

Instructions to the candidates:

1) Answers to the two sections should be written in separate sheet.
2) Use of logarithmic tables, slide rules and electronic pocket calculator is allowed.
3) Neat diagrams must be drawn wherever necessary.
4) Figures to the right indicate full marks.
5) Assume suitable data, if necessary.

## SECTION - I

**Q1)** a) Define Artificial Intelligence and justify with suitable example how does conventional computing differs from the intelligent computing? [6]

b) In what situations Means-Ends-Analysis is used. Also explain the role of difference tables in Means-Ends-Analysis. [6]

c) Explain state space approach in solving any AI problem. Discuss this for 8-puzzle (Sliding tiles) problem. [6]

OR

**Q2)** a) Explain the following with respect to minimax search procedure. [6]
i) Static evaluation function.
ii) Maximizing ply, Maximizing player.
iii) Manimizing ply, Manimizing player.

b) Specify the global database, rules and termination condition for production system to solve the following water-jug problem. Given a 4 Litre jug filled with water and an empty 3 Litre jug. How can one obtain precisely 2 Litre water in 3 Litre jug. Water may be discharged or poured from one jug to another or fill with water pump. [6]

P.T.O.

---

c) Apply constraint satisfaction algorithm to solve a cryptoarithmetic problem given below : [6]

$$
\begin{array}{r}
T O O \\
+T O O \\
+T O O \\
+T O O \\
\hline
G O O D
\end{array}
$$

**Q3)** a) With suitable examples, explain the steps needed to convert a WFF in predicate logic to its equivalent clause form. Also Convert the following sentence into WFF in predicate logic and convert it into clause form. "Anything any one eats and isn't killed by is food." [8]

b) Elucidate components of the scripts. Identify the props, roles, and scenes in the Restaurant script. [8]

OR

**Q4)** a) What do you understand by conceptual dependency? Give a conceptual dependency structure for the sentence "Sonali drove her car to office".[8]

b) Consider a simple inheritance: If X is a dog. Then X is a mammal. If we add (to working memory) the fact Pluto is a dog, also the following fact will be added: Pluto is a mammal. Later on we know that Pluto is a dog is not true. What to do with Pluto is a mammal and other derived facts? What is this situation called as? Explain. [8]

**Q5)** a) Explain understanding as constraint satisfaction. Also label the following figure using Waltz algorithm. [8]

![A line drawing of three cubes arranged in an L-shape](page_2_image_1_v2.jpg)

b) Write short note on :- [8]
i) Perception.
ii) Vision.

OR

[3764]-441

2

---

**Q6)** a) With suitable examples explain the following terms with respect to pragmatic analysis of NLP :-- [8]

i) Parts of entities.

ii) Entities involving in actions.

iii) Illocutionary force.

iv) Planning sequences.

b) Describe in details the difference between language understanding and language generation. Also explain the problem in developing a program which is capable of carrying on a dialog with a group of people. [8]

## SECTION - II

**Q7)** a) What is planning? Why block world problem is studied as a planning problem. [5]

b) Explain how Goal stack planning is different from non linear planning methods. [5]

c) What is goal stack planning? What are the operators used to solve block world problem. Specify their respective Precondition (P), Delete (D) & Add (A) lists. [8]

OR

**Q8)** a) Consider the following block world problem. Represent the start state and goal state using STRIPS type of operators. Using goal stack planning process, what will be the initial goal stack? What operators will be used to achieve the first goal? Specify its preconditions. [9]

![Start State and Goal State diagrams showing blocks A, B, C, D](page_3_image_1_v2.jpg)

b) Explain the components of a Planning System. [9]

**Q9)** a) What is learning? Explain supervised learning, reinforcement learning and unsupervised learning. [8]

b) Explain version space method of concept learning described by Mitchell. Also write version space characteristics. [8]

OR

**Q10)** a) Explain how perceptron model a neuron by taking a weighted sum of its inputs? Also explain with suitable diagram how several perceptrons can be combined to compute more complex function? [8]

[3764]-441

3

---

b) Explain the interesting features of Hopfield network. How these features are achieved? [8]

<!-- layout: ftyw, wbcw -->
**QII)** a) What is Expert system? Explain its various components/parts. Discuss the concept of uncertainly in expert system. [8]

b) What kinds of knowledge do we have to represent in an Expert System? For which kinds would we use rules, and for which would we use frames? [8]

OR

<!-- layout: hsgy, eeek -->
**Q12)** a) Given the following Prolog program, state the solutions for the query `?-flies(X)` and `?-bird(X)`. [4]

```prolog
aeroplane(concorde).
aeroplane(jumbo).
on(fred, concorde).
on(jim, no 18bus).
bird(percy).
animal(leo).
animal(tweety).
animal(peter).
hasFeathers(tweety).
hasFeathers(peter).
flies(X) :- bird(X).
flies(X) :- aeroplane(X).
flies(X) :- on(X, Y), aeroplane(Y).
bird(X) :- animal(X), hasFeathers(X).
```

<!-- layout: bjtf, sjbu -->
b) Represent the following facts in the language of logic :- [6]
i) Alison likes cakes or Alison eats cakes.
ii) If Alison likes cakes then Alison eats cakes.
iii) If Richard is a friend of Alison then Alison likes Richard.
iv) Alison eats everything that she likes.
v) There exists some bird that doesn't fly.
vi) All elephants are grey.

c) Using predicates `is_city`, `is_beautiful`, and `is_beautiful_city` write Prolog rules and facts that state : [6]
i) Pune is a city.
ii) Pune is beautiful.
iii) If something is a city and is beautiful then it is a beautiful city.
Illustrate your answer by explaining the execution of a query that asks 'Is Pune a beautiful city?'

***

[3764]-441
4