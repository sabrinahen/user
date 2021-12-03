class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount 
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount 

    def display_user_balance(self):
        print(f"User:  {self.name} \nBalance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()


michael = User("Michael Jordan", "mjchicago@gmail.com")
david = User("David Blaine", "magicdave@gmail.com")
sabrina = User("Sabrina Henrice", "bestdeveloper@gmail.com")

sabrina.make_deposit(100).make_deposit(100).make_deposit(400).display_user_balance()
