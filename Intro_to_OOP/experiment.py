class Animal :
    color = "Brown",
    name = "Piggy",
    species = "Pig"

    def information(self):
        print("My pet name is %s and it is of  %s color having species %s" %(self.name , self.color , self.species))



myPet = Animal()

# location of object in memory 

print(myPet)

# accessing information function

myPet.information()

# printing data variables

print(myPet.color , myPet.name , myPet.species)
