
Total No. of Questions - []                 Total No. of Printed Pages

G.R. No.                          Paper Code-U2I8-126 (T1)

OCTOBER 2018/IN-SEM (T1)

S. Y. B. TECH. (COM(SEMESTER - I)

COURSE NAME: Object Oriented Programming COURSE CODE: (CSUA21176)

Solution&#x26; Marking Scheme

(PATTERN 2017)

Time: [1 Hour]                              [Max. Marks: 30]

# Q.1)

# a) OOP Features

Data Abstraction, Encapsulation, Data Hiding, Inheritance, Polymorphism, classes and objects - 6 marks

# b) Declaration of class and objects - 1 mark

# Definition of function with Proper logic - 3 Marks

# Declaration of static variable - 2 Marks

#include<iostream>
using namespace std;
class vote
{
static int candidates[6];
static int number_of_voters;
public:
void get_number_of_voters();
void count_votes(int i);
void get_result();
};

void vote::count_votes(int i)
{
candidates[i]++;
number_of_voters++;
}

void vote::get_number_of_voters()
{
cout&#x3C;&#x3C;"The total number of voters is "&#x3C;<number_of_voters<<endl; }="" void="" vote::get_result()="" {="" for(int="" i="1;i<=5;i++)" &#x3C;="" pre="">
</number_of_voters<<endl;></iostream>


---



# Voting System

cout&#x3C;<i<<" got&#x22;&#x3C;&#x3C;candidates[i]&#x3C;&#x3C;&#x22;="" votes&#x22;&#x3C;&#x3C;endl;="" }="" int="" vote::candidates[6];="" vote::number_of_voters;="" main()="" {="" char="" ch="y" ;="" ballot;="" do="" cout&#x3C;&#x3C;&#x22;enter="" candidate="" number="" you="" want="" to="" vote(1="" 5)&#x22;&#x3C;&#x3C;endl;="" vote="" obj;="" cin="">>ballot;
if(ballot&#x3C;1 || ballot>5)
{ cout&#x3C;&#x3C;"Please enter between 1 to 5"&#x3C;<endl; }="" continue;="" obj.count="" votes(ballot);="" cout&#x3C;&#x3C;&#x22;do="" you="" want="" to="" continue="" voting?="" (y="" n)="" &#x22;&#x3C;&#x3C;endl;="" cin="">>ch;
}
while(ch=='y'|| ch=='Y');
cout&#x3C;&#x3C;"The number of votes for each candidate are as follows"&#x3C;<endl; vote="" result;="" result.get="" result();="" }="" result.get_number_of_voters();="" &#x3C;="" pre="">
# 2. Differences

4 marks

# OR

# 2a. Definition

1 mark

# Purpose of copy constructor

2 marks

# Example (with Syntax)

3 Marks

# b) Declaration of class and objects

2 marks

# Definition of function with Proper logic

4 Marks




---




# Electricity Bill Calculation

#include<iostream>
using namespace std;

class Electric {
double unit;
static int bill;
public:
Electric();
void accept();
void print_bill();
};

Electric::Electric() {
cout &#x3C;&#x3C; "Default Values of Units are" &#x3C;&#x3C; endl;
cout &#x3C;&#x3C; "Units 1-100" &#x3C;&#x3C; "\t" &#x3C;&#x3C; "Rs." &#x3C;&#x3C; "\t" &#x3C;&#x3C; 3 &#x3C;&#x3C; endl;
cout &#x3C;&#x3C; "Units 101-300" &#x3C;&#x3C; "\t" &#x3C;&#x3C; "Rs." &#x3C;&#x3C; "\t" &#x3C;&#x3C; 7 &#x3C;&#x3C; endl;
cout &#x3C;&#x3C; "Units 301-500" &#x3C;&#x3C; "\t" &#x3C;&#x3C; "Rs." &#x3C;&#x3C; "\t" &#x3C;&#x3C; 9 &#x3C;&#x3C; endl;
cout &#x3C;&#x3C; "Units 501-1000" &#x3C;&#x3C; "\t" &#x3C;&#x3C; "Rs." &#x3C;&#x3C; "\t" &#x3C;&#x3C; 11 &#x3C;&#x3C; endl;
cout &#x3C;&#x3C; "Beyond 1000" &#x3C;&#x3C; "\t" &#x3C;&#x3C; "Rs." &#x3C;&#x3C; "\t" &#x3C;&#x3C; 13 &#x3C;&#x3C; endl;
}

void Electric::accept() {
cout &#x3C;&#x3C; "\n No. Of Units Consumed: ";
cin >> unit;
}

void Electric::print_bill() {
if (unit >= 1 &#x26;&#x26; unit &#x3C;= 100)
bill = unit * 3;
else if (unit > 101 &#x26;&#x26; unit &#x3C;= 300)
bill = unit * 7;
else if (unit > 301 &#x26;&#x26; unit &#x3C;= 500)
bill = unit * 9;
else if (unit > 501 &#x26;&#x26; unit &#x3C;= 1000)
bill = unit * 11;
else if (unit > 1000)
bill = unit * 13;

cout &#x3C;&#x3C; "\n Electricity Bill = " &#x3C;&#x3C; bill;
}

int main() {
Electric e;
e.accept();
e.print_bill();
return 0;
}
</iostream>




---



# Q3

# a) Declaration of class and objects

4 marks

# Function for copying and concatenation of two string

2 marks each

#include &#x3C;iostream>
using namespace std;

class String {
char word[20];
char bword[40];
public:
void GetData();
void operator =(char[]);
void operator +(char[]);
void display();
};

void String::GetData() {
cout &#x3C;&#x3C; "Enter the string to evaluate : ";
cin >> word;
for (int i = 0; i &#x3C; 20; i++) {
//if(word[i]!='\0')
bword[i] = word[i];
}
}

void String::display() {
cout &#x3C;&#x3C; "\nThe original string is : " &#x3C;&#x3C; word &#x3C;&#x3C; "\n\n";
}

void String::operator =(char copy[20]) {
int i = 0;
while (word[i] != '\0') {
copy[i] = word[i];
i++;
}




---



copy[i]='\0';
cout&#x3C;&#x3C;"\nThe copied word is:"&#x3C;<copy<<`"\n\n"; }="" void="" string::operator="" +(char="" copy[20]){="" int="" j,="" flag="0," i;="" for(i="0;" i&#x3C;40;="" i++){="" if(bword[i]="=&#x27;\0&#x27;){" for(j="0;" j&#x3C;20;="" j++){="" if(copy[j]!="\0" ){="" bword[i]="copy[j];" i++;="" else{="" break;="" if(flag="=-1)" ;="" cout&#x3C;&#x3C;&#x22;the="" concatenated="" word="" is:="" &#x22;&#x3C;&#x3C;bword&#x3C;&#x3C;&#x22;\n\n&#x22;;="" main(){="" string="" obj;="" obj.getdata();="" choice,="" dummy="0," count="0;" char="" copy[20];="" do{="" cout&#x3C;&#x3C;&#x22;\nwhat="" would="" you="" like="" to="" do??n&#x22;;="" cout&#x3C;&#x3C;&#x22;\n1.copy="" word\n2.concatenate\n3.display\n4.exit&#x22;;="" cin="">>choice;
switch(choice){
case 1:
{  obj=copy;
break;
}
case 2:
</copy<<`"\n\n";>


---



cout&#x3C;&#x3C;"\nEnter new string to concatenate : ";
cin>>copy;
obj+copy;
break;
}
case 3:
{    obj.display();

}     break;
case 4:
default:       return 0;
cout&#x3C;&#x3C;"\nPlease enter a valid choice.\n\n";
}
}while(1);
return 0;
}

b public and private derivation                         2 marks each
) Function overloading ii) friend function              2 marks each

4aDeclaration of class and objects                       2 marks
Order of execution                         4 marks for Program

Base and derived class have their own constructor
Constructor is used to construct the object and destructor is called destroy the
object  Order of Execution:

First base constructor is called
Next derived constructor is called
Next destructor of derived class is called
Next destructor of base class is called
class base
{




---



public:
base()
{
cout&#x3C;&#x3C;"Base class constructor is called";
}
~base()
{
cout&#x3C;&#x3C;"Base class destructor is called";
}};
class child:public base
{
public:
child()
{
cout&#x3C;&#x3C;"child class constructor is called";
}
~child()
{
cout&#x3C;&#x3C;"child class destructor is called";
}};
int main()
{
child d;
return 0;
}

If base class constructor is not taking argument, then there is no need to define constructor in derived class. If base class is having a constructor with argument then we need to define constructor in derived class and pass argument to base class constructor.

| Definition                                    | 1 mark  |
| --------------------------------------------- | ------- |
| Pitfalls of operator overloading (at least 3) | 3 marks |
| Concept of re usability                       | 2 marks |
| Justification with example                    | 2 marks |

