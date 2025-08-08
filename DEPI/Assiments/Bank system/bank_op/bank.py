from user_op.user import User

class Bank(User):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited : {amount:.2f} successfully.")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew : {amount:.2f} successfully.")
        else:
            print(" balance less.")

    def view_balance(self):
        print(f"Current Balance:  {self.balance:.2f}")
