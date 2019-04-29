class Birds:
    _species = "bird"
    __wings = "two"
    def __init__(self , name):
        self.name = name
        print("My bird name is %s" %(self.name))

    def fly(self):
        print("All birds can fly")

    def _eatInsect(self):
        print("few birds eat insects")

    def __cannotFly(self):
        print("Rare birds cannot fly like penguin")


class Cuckoo(Birds):
    def __init__(self):
        print("I am cuckoo")


class Owl(Cuckoo):
    def __init__(self):



koyal = Cuckoo("Any")

# accessing public method of Birds class

koyal.fly()

# accessing protected method of Birds class

koyal._eatInsects()

# accessing private member of Birds class which gives an error that
