class Employee:                                                                 class Department:
    def __init__(self, name , Id):                                                  def deptName(self):
        self.name = name                                                                print("Department name is XYZ")
        self.Id = Id                                    
                                                                                    def contactNum(self):
    def resp(self):                                                                     print("contact number is **********")
        print("coding is your duty")
                                                                                    def info(self):
    def extraFaci(self):                                                                print("we provide PQRS information")
        print("You will be provided extra facilities")


# Above two examples of two classes one is having information about the employees in a organization and another 
# have about the department. So , these two class encapsule the information of two objects - employee and department
