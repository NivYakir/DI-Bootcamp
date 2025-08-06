# Exercise 1: Bank Account

class BankAccount:
    def __init__(self, balance: int, username: str, password: str, authenticated: bool = False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount: int):
        if self.authenticated:
            if not isinstance(amount, int):
                raise TypeError("Amount must be an integer")
            
            if amount <= 0:
                raise ValueError("Amount must be a positive integer")
            
            self.balance += amount
            return self
        
        else:
            raise PermissionError("User is not authenticated")
        

    def withdraw(self, amount: int):
        if not self.authenticated:
            raise PermissionError("User is not authenticated")
        
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer")
        
        if amount <= 0:
            raise ValueError("Amount must be a positive integer")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount
        return self
    
    
    def authenticate(self, user_str, pass_str):
        if user_str == self.username and pass_str == self.password:
            self.authenticated = True
            print('Success')
            return self
        
        else:
            print('Incorrect Username and/or Password')

class MinBalanceAccount(BankAccount):
    def __init__(self, balance: int, username: str, password: str, authenticated: bool = False, minimum_balance : int = 0):
        super().__init__(balance, username, password, authenticated)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount: int):
        if self.authenticated:
            if not isinstance(amount, int):
                raise TypeError("Amount must be an integer")
            
            if amount <= 0:
                raise ValueError("Amount must be a positive integer")
            
            if self.balance - amount < self.minimum_balance:
                raise ValueError("Balance would go below the minimum requirement")
            
            self.balance -= amount
            return self
        
        else:
            raise PermissionError("User is not authenticated")

class ATM:
    def __init__(self, account_list, try_limit):
        # validates that account_list is a list
        if not isinstance(account_list, list):
            raise TypeError("account_list must be a list")
        
        # validates that each item in the list is a valid Account
        for item in account_list:
            if not isinstance(item, BankAccount):
                raise TypeError(f"{item} is not a valid Bank Account")
        
        self.account_list = account_list

        try:
            # validates that try_limit input is a positive int
            if not isinstance(try_limit, int) or try_limit <= 0:
                raise ValueError("try_limit must be a positive integer")
            self.try_limit = try_limit

        except Exception as e:
            # if error is raised, the try_limit is set to 2
            print(f"Invalid Input: {e}\ntry_limit has automatically been set to 2")
            self.try_limit = 2

        self.current_tries = 0

    def show_main_menu(self, user_input='login'):
        print('''
            ***MAIN MENU***
            |             |
            | # LOG IN    |
            | # QUIT      |
            |             |
            ***************
            ''')
        while True:
            user_input = input("Please select an option: ")
            if user_input.lower().strip() == 'login':
                return self.log_in()
            elif user_input.lower() == 'quit':
                print("You have exited from the ATM. Good Day!")
                break
            else:
                print("Invalid Entry, please try again: ")

    def log_in(self):


        while self.current_tries != self.try_limit:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            for account in self.account_list:
                # checks if the username/password matches for any of the BankAccounts in the account_list
                if account.username == username and account.password == password:
                    account.authenticate(username, password)
                    return self.show_account_menu(account)

            self.current_tries += 1
        
        print("You have reached the max amount of tries. The ATM will temporarily shut down.")
        self.show_main_menu('quit')
    
    def show_account_menu(self, account: BankAccount):

        try:
            choice = int(input("Select a number: (1)Deposit (2)Withdraw (3)Exit: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

        if choice not in range(1,4) or isinstance(choice, int) == False:
            print("Invalid Input. Please select (1)Deposit (2)Withdraw (3)Exit")
        elif choice == 1:
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            account.withdraw(amount)
        elif choice == 3:
            print("You have been logged out.")
            

            






atm1 = ATM([],2)
atm1.show_main_menu()




# bank1 = BankAccount(1000, 'nivya', 'pass1234')
# bank1.authenticate('nivya', 'pass1234')
# bank1.withdraw(1100)
# print(bank1.__dict__)

