class Shapes:

    def __init__(self):
        print("Lets calculate areas")

    def area(self,radius):
        self.radius = radius
        print(3.14 * self.radius * self.radius)
        

    def area(self, length = 0, width = 0):
        self.length = length
        self.width = width
        print(self.length * self.width)

    def area(self ,  length = 0.0 , width = 0.0):
        self.length = length
        self.width = width
        print(self.length * self.width)
        

    def area(self, radius = 0.0 , height = 0):
        self.radius = radius
        self.height = height
        print(0.33 * 3.14 * self.radius ** 2 * self.height)

s = Shapes()
s.area(7)
s.area(6.3 , 6.3)
s.area(7, 8)
s.area(0.7 , 8)
