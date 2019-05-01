class A:
    def I_a(self):
        print("I am class A's function")

class B(A):
    def I_b(self):
        print("I am class B's function")

class C(A):
    def I_c(self):
        print("I am class C's function")

class D(A):
    def I_d(self):
        print("I am class D's function")

class E(B,C,D):
    def I_e(self):
        print("I am class E's function")


e = E()
b = B()
c = C()
d = D()

e.I_a()
e.I_b()
e.I_c()
e.I_d()
e.I_e()

b.I_a()

# print(dir(e))
# print(dir(d))
# print(dir(c))
# print(dir(d))