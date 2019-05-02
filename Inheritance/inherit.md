# Inheritance :-
Inheritance may be defined as the process of acquiring the properties of parent class without affecting it in deriving class.

## Parent class : -

A class whose properties are acquired by another class is classed parent class

## Derived class:-
A class which is acquiring the properties of another class is called derived class or sub-class.

## Types of inheritance :- 

There are many types of inheritance defined in computing world which are given below : -
1) Single Inheritance
2) Multiple Inheritance
3) Multi-level Inheritance
4) Hybrid Inheritance

## Single Inheritance :-

In this type of inheritance , there is only two level i.e. one is parent class and second one is derived class. And derived class inherit the parent class to acquire its properties. Below diagram shows the single inheritance relation bet class

                                                |---------------------|
                                                |                     |
                                                |    class A          |
                                                |                     |
                                                |---------------------|
                                                           |
                                                           |
                                                           |
                                                           |
                                                          \|/
                                                |---------------------|
                                                |                     |
                                                |     class B         |
                                                |---------------------|
## Multiple Inheritance :-

In this type of inheritance , A class can inherit more than one class. But, a problem arises in this type of inheritance and the problem is when two classes have same method then which method derived class should run As there is ambiguity in the methods. But python resolve this ambiguity working on the ordering of inheritance i.e. in such type of case , python executes the method of first inherited class. Below diagram shows the concept of multiple inheritance.

                            |-----------|          |--------------|                |------------|
                            | class A   |          |  class B     |                | class C    |
                            |-----------|          |--------------|                |------------|
                                 |                        |                               |
                                 |                        |                               |
                                 |                        |                               |
                                 |                        |                               |
                                 |------------------------|-------------------------------|
                                                          |
                                                          |
                                                         \|/
                                                    |------------|
                                                    | class D    |
                                                    |------------|


## Multi-Level Inheritance :-

In this type of inheritance , the hierarchy of class is maintained i.e one class inherit another class and this class is further inherited by another class and chain goes on until you wanna stop it. Below diagram show three level inheritance.

                                                                 |---------------|
                                                                 |   class A     |
                                                                 |---------------|
                                                                         |
                                                                         |
                                                                        \|/
                                                                 |---------------|
                                                                 |    class B    |
                                                                 |---------------|
                                                                         |
                                                                         |
                                                                        \|/
                                                                 |----------------|
                                                                 |    class C     |
                                                                 |----------------|


## Hybrid Inheritance : - 

This type of inheritance is the mixture of multiple inheritance and multi level inheritance. Below diagram will show the concept of hybrid inheritance.


                                                                 |---------------|
                                                                 |    class A    |
                                                                 |---------------|
                                                                 /       |        \
                                                                /        |         \
                                                               /         |          \
                                                              /          |           \
                                                |------------|      |---------|     |---------------|
                                                |   class B  |      | class C |     |     class D   |
                                                |------------|      |---------|     |---------------|
                                                       \                 |                  /
                                                        \                |                 /
                                                         \               |                /
                                                          \              |               /
                                                          |------------------------------|
                                                          |          class E             |
                                                          |------------------------------|
<!-- 
In this inheritance , we face diamond problem which states that class B , C and D all have inherited class A . So, all three have properties of class A . ANd when class E inherit class B, C, D then from which class it should inherit the property of class A. -->


Now, let's try to know the concept of access modifiers and their uses.

## Access modifiers of data :-

There are three types of access modifiers of data or methods which are given below :-

1) public
2) protected
3) private

Public : - 

Public data variables or methods can be accessed from anywhere wether its within a class or outside of class.

Protected :- 

Protected data can only be accessed by within a class and immidiate subclass or derived class of it.

Private :-

Private data and methods can only be accessed within the class. To use a variable or method outside a class then you need to do either call this method by creating an object with its class name concatenated with private data or method.


In python , public data and methodsare declared as normal variable or data is declared. 
To declare a variable and method as protected , you need to put single underscore ('_') with its name like below given example 

def _Hello():
     print("Hello world !!!")                          #( protected mathod)


_isHungry = 'No'                                       #(protected variable)


To declare a variable or method private , then concatenate its name with double underscore like given below example

def __Hello():
     print("hello world!!!")                          # (private method)


__isHungry = "No"

To access private data outside of class then concatenate its name with "_className"
