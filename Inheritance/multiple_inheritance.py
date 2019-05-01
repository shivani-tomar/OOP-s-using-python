class A :
    def __init__(self):
        print("Hi , I am init of class A")

    def cal(self):
        print("computer does calculation faster than human")


class B:
    def __init__(self):
        print("Hi, I am init of class B")

    def cal(self):
        print("computer is faster than human")


class D:
    def __init__(self):
        print("Hi, I am init of class D")

    def cal(self):
        print("computer is fasterrrrrrrrr than human")

    def boo(self):
        print("I love Boo")




class C( B, D, A):
    def __init__(self):
        print("Hi, I am init of class C")



c = C()
c.cal()
print(isinstance(c, C))
print(isinstance(c, B))
print(isinstance(c,D))
print(isinstance(c, A))
print(c)
print(dir(c))

