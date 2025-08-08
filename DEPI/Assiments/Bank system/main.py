from bank_op.bank import Bank
from banks.CIB import CIB
from banks.QNB import QNB

name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
amount = int(input("Enter your amount: "))

account = Bank(name, age, gender, amount)

cib = CIB(account)
qnb = QNB(account)

print("----------------------------- \n \n")

while True:
    print(f"Welcome {name} :) ")
    print("What do you want: ")
    print("1- Show info")
    print("2- Deposit")
    print("3- Withdraw")
    print("4- View your balance")
    print("5- Loan from CIB")
    print("6- Loan from QNB")
    print("7- Exit")

    choice = int(input("Enter your choice pls: "))
    print("\n")

    if choice == 1:
        account.show_info()
        print("\n")

    elif choice == 2:
        dep = int(input("Enter the amount to deposit: "))
        account.deposit(dep)
        print("\n")

    elif choice == 3:
        wi = int(input("Enter the amount to withdraw: "))
        account.withdraw(wi)
        print("\n")

    elif choice == 4:
        account.view_balance()
        print("\n")

    elif choice == 5:
        loan_amount = int(input("Enter loan amount from CIB: "))
        duration = int(input("Enter duration in months: "))
        cib.take_loan(loan_amount, duration)
        print("\n")

    elif choice == 6:
        loan_amount = int(input("Enter loan amount from QNB: "))
        duration = int(input("Enter duration in months: "))
        qnb.take_loan(loan_amount, duration)
        print("\n")

    elif choice == 7:
        break

    else:
        print("Please enter a number between 1 and 7\n")

print("Thx for using the app :)")
