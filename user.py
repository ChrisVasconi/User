

class User:
    bank_name = "First National Dojo"

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def withdraw_money(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


guido = User("Guido van Rossum", )
monty = User("Monty Python",)
rick = User("Rick James", )


guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(600)
guido.withdraw_money(50)
guido.display_user_balance()
monty.make_deposit(200)
monty.make_deposit(39)
monty.withdraw_money(28)
monty.withdraw_money(120)
monty.display_user_balance()
rick.make_deposit(300)
rick.withdraw_money(20)
rick.withdraw_money(100)
rick.withdraw_money(15)
rick.display_user_balance()
