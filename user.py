class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount 

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


sabrina.make_deposit(10000)
print(sabrina.account_balance)
david.make_deposit(500)
print(david.account_balance)
michael.make_deposit(500)
print(michael.account_balance)

michael.make_withdrawl(100)
print(michael.account_balance)

michael.display_user_balance()

sabrina.transfer_money(michael, 150)

