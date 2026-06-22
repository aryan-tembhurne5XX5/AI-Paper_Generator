
DECEMBER 2018 / END-SEM
F. Y. M. TECH. (Computer Engineering) (SEMESTER - I)
COURSE NAME: Machine Learning
COURSE CODE: CSPA11183A

# Q.1)

# a)

Explain in brief different learning paradigms : 1 MARK EACH (SYATEMAT [3] INCREMENTAL,

OR

Identify type of learning for the following application [3]

- You are going for a movie in the afternoon and your mother predicts that it would rain in the afternoon (DECISION TREE: SUPERVISED)
- In a Cricket match captain wins the toss and decided to bat (SUPERVISED)
- Predicting rainfall based on historical data (SUPERVISED)

# Q.2

# a)

Apply k means algorithm for the following numbers and display 3 clusters [3]

(10, 123, 14, 15, 67, 45, 87, 23, 04, 98)

K=3 SELECT RANDOM 3 SEED POINTS, CALCULATE EUCLIDIAN DISTANCE OF EACH FROM THESE SEED POINTS (e.g seed1 is 10 calculate distance of 10 from each element similarly for other 2 seed points put the smallest distance in respective cluster, stop if previous iteration and next iteration distance is same or minimum.

E.G C1=(04, 10, 14, 15, 23) C2= (45, 67, 87) C3=(98, 123)

# b)

Draw the labeled diagram of neural network [3]

2 MARKS DIAGRAM ONE MARK LABEL. COMPONENTS INCLUDE INPUT LAYER, FEATURES, ACTIVATION FUNCTION, OUTPUT LAYER.

# Q.3

# a)

Under which circumstances would you use K-means clustering? How is the k value selected? WHEN TYPE OF DATA EVOLVED IS NOT KNOWN, NO CLASS LABEL AVAILABLE

# b)

Under which circumstances is ensemble method used? What is bagging? WHEN SINGLE CLASSIFIER NOT ABLE TO PREDICT CORRECTLY

Total No. of Printed Pages: 3



---




# Q.4

Consider a case where a friend of yours will be visiting your place. You are meeting him after a long time. You want to take him to a hotel. Would you go to a newly opened hotel which serves different delicacies or a one where you visit often? How can you relate both the scenarios to Reinforcement Learning? Explain the concepts of RL in this regard with equations.

7 MARKS FOR PROBLEM IDENTIFICATION, UNDERSTANDING AND DESIGN MODEL + 7 MARKS HOW REINFORCEMENT LEARNING FORMS EQUATION FEATURES (FEEDBACK, RATING, DISHES, INTEREST ETC + REWARDS IF YOU LIKE THE HOTEL PREVIOUSLY + ELSE PENALTY IF DISLIKE)

# OR

# Q.5

Consider the scenario like Boxer trainer. How would you design a learning system which will calculate award and punishment scheme?

STRATEGY FOR WIN/LOSS NO OF MOVES, NO OF ROUNDS PLAYER PLAYED, WIN/LOSS, BEFORE LOSS ACTION, LAST 3 CONSECUTIVE ACTIONS BEFORE LOSS, SIMILARLY FOR WINNING STRATEGY

# Q. 6

Why is there a need of combining multi perspectives? Explain with the help of any suitable example. Consider an approach of combining features based on priority weighted sum of feature vector.

4 MARKS NEED + 5 MARKS EXAMPLE + 5 MARKS FEATURE VECTOR AND WEIGHTS ASSIGNED e.g monitoring run time traffic and observing violation of traffic rules from using ML based approach

# OR

# Q.7

Consider recommendation systems like movie rating or predicting a popularity of politicians during the election process. Apply adaptive learning method to predict the outcome. Which supervised approach can be applied for such prediction? Consider relevant feedback given by people on various social media sites.

7 MARKS FOR APPROACH + 7 MARKS FOR WHY THIS APPROACH SUPERVISED + UNSUPERVISED. UNSUPERVISED APPROACH FOR COLLECTING USERS OF SIMILAR INTEREST, SUPERVISED FOR BUILDING THE MODEL, FEATURES AND PREDICTING THE POPULARITY

# Q. 8

In any learning system, is context important or content important? Can an adaptive system help in both scenarios or work in combination of both? Put forth your views with each aspect. How can you relate systemic learning here?

2 MARKS + 4 MARKS FOR CONTEXT AND CONTENT + 4 MARKS FOR SYSTEMATIC LEARNING CONTEXT AND CONTENT BOTH IMPORTANT e.g. NLP PROCESSING




---


# Justify how incremental learning is better than retraining a model

[04]

# Can incremental learning face a problem of catastrophic forgetting?

(Forgetting all that is previously learnt). Explain in detail.

# CATASTROPHIC FORGETTING

TASKS WHICH THEY HAVE NOT EXPERIENCED FOR A LONG TIME

CATASTROPHIC FORGETTING: TASKS WHICH MODEL HAVE NOT EXPERIENCED FOR A LONG TIME

APPROACH: REMEMBERS OLD TASKS SELECTIVELY SLOWING DOWN LEARNING ON THE WEIGHTS IMPORTANT FOR THOSE TASKS