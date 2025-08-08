from bank_op.bank import Bank
from user_op.user import User
class QNB:
    max_loan = 2000000

    def __init__(self, account):
        self.account = account

    def take_loan(self, loan_amount, duration):
        if loan_amount <= 0 or duration <= 0:
            print("Loan amount and duration must be positive.")
            return
        if loan_amount > self.max_loan:
            print("Loan amount must be less than two million.")
            return

        self.account.balance += loan_amount
        print(f"Loan approved! New balance: ${self.account.balance:.2f}")
