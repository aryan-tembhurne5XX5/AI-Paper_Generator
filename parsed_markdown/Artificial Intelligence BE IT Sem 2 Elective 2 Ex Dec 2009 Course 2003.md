Total No. of Questions : 12] [Total No. of Pages : 3
P1126 [3664]-359
B.E. (Information Technology)
ARTIFICIAL INTELLIGENCE (414451)
(Elective-II) (2003 Course) sem II

Time : 3 Hours/ [Max. Marks : 100
Instructions :
1) Answers to the two sections should be written in separate books.
2) Neat diagram must be drawn wherever necessary.
3) Figures to the right indicate full marks.
4) Use of logarithmic tables, slide rules and electronic pocket calculator is allowed.
5) Assume suitable data, if necessary.

## SECTION - I

**Q1)** a) Define Artificial intelligence. What is Turing Test and what was it intended to accomplish? [8]
b) Best First search uses both an OPEN list and a CLOSED list. Describe the purpose of each for the Best-First algorithm. Explain with suitable example. [8]
OR
**Q2)** a) Hill climbing is a standard iterative improvement algorithm similar to greedy Best-First search. What are the primary problems with hill climbing? [8]
b) Describe the essence of a constraint satisfaction problem. What are some of the major applications of constraint satisfaction search? [8]
**Q3)** a) What is predicate logic? Describe the advantages of predicate logic over propositional logic. [8]
b) Briefly explaining Truth Maintenance system. Explain with suitable example how TMS allows truth values to be changed during reasoning. [8]
OR
**Q4)** a) Represent each of the following sentences in first-order logic and then convert each one of them into Well Formed Formula (WFF). [8]
i) A whale is a mammal.
ii) John knows Jane's father.
iii) If it's raining, then the ground is wet.
iv) If the switch is on and the light is off then the light-bulb is broken.
v) All computers have a processor.

P.T.O.

---

b) What is resolution? Explain resolution is predicate logic with suitable example. [8]

**Q5)** a) Explain the major modules of a natural language interpretation system and explain their functions. [9]
    b) What is understanding? Explain understanding as constraint satisfaction with suitable example. [9]
OR
**Q6)** a) There are many important relationships that may hold between phrases and parts of their discourse context. Explain the following terms with respect to pragmatic analysis :- [9]
    i) Identical entities
    ii) Parts of action
    iii) Elements of sets
    iv) Causal chains.
    b) Draw and explain types of junction in a line drawing in Waltz algorithm. Also show all permissible labeling at those junctions. [9]

<u>SECTION - II</u>

<!-- layout: arif, mwzd, zdhu, xsgy -->
**Q7)** a) What are the components of a planning system? Explain briefly how these components can be implemented. [8]
    b) Write brief note on i) STRIPS, ii) Least Commitment Strategy. [8]
OR
**Q8)** a) What is planning? How block world problem helps up to study planning? Give suitable example. [8]
    b) Write brief note on i) Hierarchical Planning, ii) Non-Linear planning. [8]

**Q9)** a) What is learning? Explain Failure-driven learning in details with suitable example. [8]
    b) Explain Artificial Neural Networks (ANN). Also explain how ANN mimics the human brain working. [8]
OR
**Q10)** a) What is Supervised Learning and unsupervised Learning? Explain the benefits to Neural Networks. [8]
    b) What is Inductive learning? Also explain Winston's learning program. [8]

**Q11)** a) What is Prolog? How Prolog answer user queries? [9]
    b) Explain architecture of expert system and discuss how expert system technique helps in building an efficient system. [9]
OR

<!-- layout: ezlz, wadg -->
[3664]-359 - 2 -

---

**Q12)**a) Identity and describe two good application areas for expert system within a University environment. [9]

b) Explain how Prolog copes with searching through a number of clauses, matching, unification and resolution. Also consider the following Prolog program code and write the output of the following queries :- [9]

What will be output of the following queries :-

? proud(shreyash)
? proud(X)
? parent(ajay,X)

predicates
proud(symbol).
parent(symbol,symbol).
newborn(symbol).
father(symbol,symbol).
mother(symbol,symbol).

clauses
proud(X):-parent(X,Y),newborn(Y).
parent(X,Y):- father(X,Y).
parent(X,Y):- mother(X,Y).

father (ajay, shreyash).
mother(smita, shreyash).
newborn(shreyash)

[3664]-359 - 3 -