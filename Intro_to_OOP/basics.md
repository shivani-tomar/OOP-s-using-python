# Intro to OOP's :-

The whole world comprises of objects whether its table, chair, water-bottles , lappy, pen, pencil or anything. That's why we use object oriented programming in computational world. object oriented paradigm consist of two basic pillars which are given below : -

1) class
2) objects

## Class :-

A class may be defined as the blue print of the object which have no space in memory. It is like as the declaration of variable in procedure oriented programming which was not allocated any memory. As blue print is the lay out of the structures and actions . Same thing as class does. A class consist of data variables and methods which represent attributes of any object and  actions of the objects. It is the class which going to tell what will happen when you create the object of class.

When we create a class , object of that particular class is passed to it by default which is named as "self". It is a default object of its own class. "self" may be defined as self refrencial object.

## Objects : - 

AN Object may be defined as the instance of the class having all data members and methods of class with required memory allocation i.e. an object has space in memory. 

A class consist of constructor and destructor

#### Construcotr :-

A constructor may be defined as a method which got executed every time when we initialize a class or create an object. There are three types of constructor which are given below :-

1) default constructor
2) parameterized constructor
3) copy constructor

Default constructor :- 

default constructors are the constructor which get executed by default having no arguements passed into it. It is usually used for print statements to get to know wether class has been instantiated or not.

Parametrized constructor : - 

In this type of constructor , arguements are passed. It is mostly used to initialize some variables while creating instance of the class. 

Copy constructor :- 

This is a special type of constructor in which object of another class is passed and can be used to access the variables and methods (mostly public) and maipulate them if neccesary.


#### Destructor :- 

A destructor may be defined as a method which got executed when the object of a class is destroyed. In python , "__del__()" is default destructor which executes when object is destroyed.

In python, we cannot have multiple constructor at a time .  There should be only one constructor for a class which can be default constructor or parameterized constructor or copy constructor. The function name of constructor in python is only "__init__()" in which you can pass parameters , objects etc.

There is "super()" method to call the constructor of parent class.






