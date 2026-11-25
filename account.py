## This programm is there to practice accounts class with methods like deposit, withdraw, and check balance.
class Account():
    def __init__(self, accountHolderName, accountBalance):
        self.accountHolderName=accountHolderName,
        self.accountBalance=accountBalance

    def deposit(self, amount):

        if amount==0 or amount<=0:
            
            print("Enter Valid Number")

        else:

            self.accountBalance+=float(amount)
            print("Deposited: {}, you current account balance is {}".format(amount, self.accountBalance))


    def withdraw(self, amount):

        if float(amount)>self.accountBalance:

            print("Insufficient Balance")

        elif amount<=0:

            print("please enter valid numbers only")

        else:

            self.accountBalance=self.accountBalance-amount

            print("With draw successful")
            print("Dear {}, you current balance ater withdrawing {} is {}".format(self.accountHolderName, amount, self.accountBalance))


    def checkBalance(self):

        print("Dear {} your current account balance is {}".format(self.accountHolderName, self.accountBalance))



cust1=Account("ravi Teja", 20000)


cust1.checkBalance()
cust1.withdraw(2000)
cust1.checkBalance()
cust1.deposit(7000)
cust1.checkBalance()

