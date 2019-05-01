class A:
    
    def hello(self):
        print("I belong to class A")


class B(A):

    def target(self):
        print("Get admission in P.G.")


class C(B):

    def time_left(self):
        print("About one and half month is left")


c = C()
c.hello()
c.target()
c.time_left()
#print(dir(c))