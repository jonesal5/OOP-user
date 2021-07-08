#add a make_withdrawal method to the User class
class User:
    def __init__(self, name, email):
        self.name = name                
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    
#create 3 instances of the user class
Alyssa = User("Alyssa K", "alyssak@dojo.com")

Michael = User("Michael Jordan", "MJordan@coding.com")

Kobe = User("Kobe Bryant", "kobebryant@codingdojo.com")


#have the first user make 3 deposits and 1 withdrawal and display their balance.
Alyssa.make_deposit(100)
Alyssa.make_deposit(200)
Alyssa.make_deposit(300)
Alyssa.make_withdrawal(500)
Alyssa.display_user_balance()

#have the second user make 2 deposits and 2 withdrawals and display their balance.
Michael.make_deposit(500)
Michael.make_deposit(100)
Michael.make_withdrawal(200)
Michael.make_withdrawal(100)
Michael.display_user_balance()

#have the third user make 1 deposit and 3 withdrawals and display their balance.
Kobe.make_deposit(800)
Kobe.make_withdrawal(200)
Kobe.make_withdrawal(400)
Kobe.make_withdrawal(200)
Kobe.display_user_balance()
