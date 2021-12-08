class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"I'm the owner {self.owner} of account with balance {self.balance}."

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Current account balance is {self.balance}."
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print('Withdrawal Accepted')
            return f"Current account balance is {self.balance}."
        else:
            return "You are withdrawing amount more than your account balance."

acct1 = Account('Saurabh',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
deposit_balance = acct1.deposit(50)
print(deposit_balance)
withdraw_balance = acct1.withdraw(75)
print(withdraw_balance)
print(acct1.withdraw(500))

    