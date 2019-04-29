class livingOrganism:
    def breathe(self):
        print("Every living organism take breathe")
    
    def _eat(self):
        print("every living organism eat food")

    def __drink(self):
        print("every organism drink water")

class Birds:
    def _wings(self):
        orga = livingOrganism()
        orga.breathe()
        orga._eat()
        #orga.__drink()
        print("Every bird has two wings")

class Owl:
    def fly(self):
        birdy = Birds()
        birdy._wings()
        print("I can fly")

owl = Owl()
owl.fly()

# lo = livingOrganism()
# lo.__drink()




