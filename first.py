class Account:
   def __init__(self,account_number,balance): 
      self.account_number = account_number
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
   def withdraw(self, amount):
      if amount <= self.balance:
         self.balance-=amount
      else:
         print('vag vikhari')
   def display_balance(self):
      print(f'Account Numner: {self.account_number}, Balance: {self.balance}')

class SavingAccount(Account):
  def __init__(self, account_number, balance, interest_rate):
     super().__init__(account_number, balance)
     self.interest_rate = interest_rate
   
  def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

account1 = Account('331543',10000)
account2 = SavingAccount('331533',15000,5)

account1.deposit(500)
account1.withdraw(200)
account1.display_balance()

account2.deposit(1000)
account2.add_interest()
account2.display_balance()

