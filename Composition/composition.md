# Composition :- 

Composition meaning is consist of or "Has A" relationship between classes. In composition , we access methods and data variables of one class in other by creating the object of the class whose properties we want to access in the class in which we want to access these properties. 
Lets understand this concept by tiffin box. Suppose your mom has packed lunch for you in fresh up and then put it into lunch box.
So, we can say that lunch-box has wrapper/fresh-up and fresh-up has cutlet. There is has a relationship between cutlet and fresh-up and fresh-up and lunch-box. 
                                                                    OR
you can say that lunch box consist of wrapper and wrapper consist of cutlet. So, there is consist of relationship between lunch box and wrapper and cutlet.

## Special properties of composition : - 

As we go to inner class , it goes from general to special and as we go outer to the class , we go special to general class.

Inner class has mostly all the properties of outer class but it's vice versa is not true.


                                                    |---------------------------|
                                                    |        class A            |
                                                    |   |-------------------|   |
                                                    |   |    class B        |   |
                                                    |   |   |-----------|   |   |
                                                    |   |   |  class C  |   |   |
                                                    |   |   |           |   |   |
                                                    |   |   |           |   |   |
                                                    |   |   |-----------|   |   |
                                                    |   |                   |   |
                                                    |   |-------------------|   |
                                                    |                           |
                                                    |---------------------------|  

Lets class A is living organism and class B is birds and class C is owl. Then we can say that all owl are birds and all birds are living organism.

Private members of class cannot be accessed through composition.

There is no protected access concept in composition as they are accessible from C's class object by using class B.

## Difference between inheritane and composition :-

Most of the time inheritance and composition are taken as same things as through both we access properties of another class in one class. But both are different from each other.

In inheritance , we don't create any object of class but in composition we create object of the class.

In composition , constructor of the class whose object is created , executed automatically as we are creating object of that class but in inheritance , we need to call the constructor or need to use super() function to do it.

There is no concept of protected access modifier  in composition as it is accessible through level hierarchy but protected access modifier concept is true in inheritace  , specially in multi-level inheritance.

These are few differnces in between inheritance and composition , which I can remember right now.

