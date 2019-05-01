class A:
    def mammal(self):
        print("I am mammal")

class B(A):
    def human(self):
        print("human is a mammal")


b = B()

b.mammal()
b.human()