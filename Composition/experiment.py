class livingOrganism:
    __cells = "yes"
    def breathe(self):
        print("Every living organism take breathe")
    
    def _eat(self):
        print(self.__cells)
        print("every living organism eat food")

    def __drink(self):
        print("every organism drink water")

    def makeDrink(self):
        print("I am making drink")
        self.__drink()

class Birds:
    def _wings(self):
        orga = livingOrganism()
        orga.breathe()
        orga._eat()
        # To access private method of a class , need to put class - name starting with underscore
        orga._livingOrganism__drink()
        orga.makeDrink()
        print("Every bird has two wings")

class Owl:
    def fly(self):
        birdy = Birds()
        birdy._wings()
        print("I am owl and I can fly")

owl = Owl()
owl.fly()

lo = livingOrganism()
#print(lo.__cells)
# lo._livingOrganism__drink()

print(dir(owl))


# Through owl class , we are able to access and call the methods of Birds and livingOrganism as Owl class consist of Birds class 
# and Birds class consist of livingOrganism class. In this way , they consist each other like a roll and form composition.



