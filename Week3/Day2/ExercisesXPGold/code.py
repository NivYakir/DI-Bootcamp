# Exercise 1: Bank Account

class BankAccount:
    def __init__(self, balance, username, password):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        try:
            if not isinstance(amount, int):
                raise TypeError("Deposit amount must be an integer.")
            
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            
            self.balance += amount
            return self
            
        except Exception as e:
            print(f"Deposit failed: {e}")
    
    def withdraw(self, amount):
        try:
            if not isinstance(amount, int):
                raise TypeError("Withdrawal amount must be an integer.")
            
            if amount > self.balance:
                raise ValueError("Insufficient Balance for withdrawal.")
            
            self.balance -= amount
            return self

        except Exception as e:
            print(f"Withdrawal failed: {e}")

    def authenticator(self):
        if self.username == self.password:
            self.authenticated = True
        return self


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance=0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, minimum_balance, amount):
        try:
            if self.balance < minimum_balance:
                raise ValueError("Your current balance is below the minimum balance amount.")
            
            self.balance -= amount
            return self
        
        except Exception as e:
            print(f"Withdrawal Failed: {e}")