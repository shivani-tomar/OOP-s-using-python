class Bank:
    currentAmount = 0.0
    rate = 12
    def __init___(self, account_holder_name , initial_amount , account_number):
        self.account_holder_name = account_holder_name
        self.initial_amount = initial_amount
        self.account_number = account_number
        print("Welcome to XYZ bank ")
        print("Your details are ")
        print(self.account_holder_name , self.initial_amount , self.account_number)

    def display_currentAmount(self):
        print("Your current amount is %d" %(self.currentAmount))

    def deposit(self, amount):
        self.amount = amount
        currentAmount += self.amount

    def withDrawal(self, amount):
        self.amount = amount
        currentAmount -= self.amount

    def monthlyInterestGiven(self):
        interest = (currentAmount * rate * 1 )/(1200)
        currentAmount += interest


account = Bank("Olivia" , 1000.0 , "ADHK13579" )

account.display_currentAmount()
account.deposit(1000)
account.withDrawal(200)
account.monthlyInterestGiven()
account.display_currentAmount()


# Now, due to abstraction , nobody care about what's going to happen in the function or what calculation is done . One can easily 
# create object of the class and use the method to implement required action.This is called abstraction . 
# It's like bin() function in python which convert any decimal number into binary but how it do it we don't know 
# neither we worry to know about it. We just give input to it 
# and it gave output function. That's all.