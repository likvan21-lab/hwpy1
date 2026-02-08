class BankAccount:
    def __init__(self, name, secret, balance):
        self.name = name
        self.__balance = balance
        self.__secret = secret

    def check_balance(self, secret):
        if secret == self.__secret:
            print(f"{self.name} balance: {self.__balance}")
        else:
            print("Invalid secret number")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful. New balance:", self.__balance)
        else:
            print("Invalid amount")

    def withdraw(self, secret, amount):
        if secret != self.__secret:
            print("Invalid secret number")
            return
        if amount > self.__balance:
            print("Not enough money")
        else:
            self.__balance -= amount
            print("Withdraw successful. Remaining balance:", self.__balance)

    def transfer(self, secret, other_acc, amount):
        if secret != self.__secret:
            print("Invalid secret number")
            return
        if amount > self.__balance:
            print("Not enough money to transfer")
        else:
            self.__balance -= amount
            other_acc.deposit(amount)
            print(f"Transfer successful to {other_acc.name}")

    def pay_service(self, secret, service_name, amount):
        if secret != self.__secret:
            print("Invalid secret number")
            return
        if amount > self.__balance:
            print("Not enough money to pay")
        else:
            self.__balance -= amount
            print(f"Paid {amount} for {service_name}")
            print("Remaining balance:", self.__balance)



print("Welcome to my BANK ATM ")

name = input("Enter your name: ")
secret = input("Set your secret number: ")

balance = float(input("enter your money: "))
my_acc = BankAccount(name, secret,balance)

other_acc = BankAccount("Friend", "999",5000)

while True:
    print("\n------ MENU ------")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Pay service")
    print("6. Exit")

    choice = input("Choose (1-6): ")

    if choice == "1":
        sec = input("Enter secret: ")
        my_acc.check_balance(sec)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        my_acc.deposit(amount)

    elif choice == "3":
        sec = input("Enter secret: ")
        amount = float(input("Enter amount to withdraw: "))
        my_acc.withdraw(sec, amount)

    elif choice == "4":
        sec = input("Enter secret: ")
        amount = float(input("Enter amount to transfer: "))
        my_acc.transfer(sec, other_acc, amount)

    elif choice == "5":
        sec = input("Enter secret: ")
        service = input("Enter service name: ")
        amount = float(input("Enter amount to pay: "))
        my_acc.pay_service(sec, service, amount)

    elif choice == "6":
        print("Thank you for using our service")
        break

    else:
        print("Invalid choice, please try again")