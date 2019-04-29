class Birds:
    wings = "yes"
    def __init__(self):
        print("I am bird constructor")


class Animal(Birds):
    color = "Brown",
    name = "Piggy",
    species = "Pig"

# default constructor without any parameters.

    def __init__ (self):
        super().__init__()
        print("I am init by default constructor")

#                      OR
#           Parameterized constructor

    # def __init__(self, num):
    #     super().__init__()
    #     self.num = num
    #     print("you pass %d number and I am a parameterized constructor" %(self.num))

#                       OR
#               Copy constructor

    # def __init__(self,obj):
    #     print(obj.wings)
    #     print("I am example of copy constructor")



    def information(self):
        print("My pet name is %s and it is of  %s color having species %s" %(self.name , self.color , self.species))

    def __del__(self):
        print("I am default destructor and executed when object is destroyed from memory")

# object of bird class

bird = Birds()

# object of animal class

myPet = Animal(bird)

# location of object in memory 

print(myPet)

# accessing information function

myPet.information()

# printing data variables

print(myPet.color , myPet.name , myPet.species)

