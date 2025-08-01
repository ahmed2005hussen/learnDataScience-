class User:
    def __init__(self, name, age, gender, balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

    def show_info(self):
        print("User Information:")
        print(f"Name: {self.name}.")
        print(f"Age: {self.age}.")
        print(f"Gender: {self.gender}.")
        print(f"Balance: ${self.balance}.")
