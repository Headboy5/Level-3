class BankAccount:
    def __init__(self, account_number, account_holder, sort_code, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.sort_code = sort_code

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: £{amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: £{amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance
    
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Sort Code: {self.sort_code}")

    def create_card(self):
        BankCard = {
            "card_number": "1234 5678 9012 3456",
            "expiry_date": "12/25",
            "cardholder_name": self.account_holder
        }
        return BankCard
    
    def RegisterAddress(self, address):
        self.address = address

    def PhoneNumber(self, phone_number):
        self.phone_number = phone_number

def main():
    account = BankAccount("12345678", "John Doe", "12-34-56", 1000)
    exit = False
    while not exit:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Account Info")
        print("5. Create Bank Card")
        print("6. Register Address")
        print("7. Register Phone Number")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: £"))
            account.deposit(amount)
            input("Press Enter to continue...")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: £"))
            account.withdraw(amount)
            input("Press Enter to continue...")
        elif choice == '3':
            print(f"Current Balance: £{account.get_balance():.2f}")
            input("Press Enter to continue...")
        elif choice == '4':
            account.display_account_info()
            input("Press Enter to continue...")
        elif choice == '5':
            card = account.create_card()
            print(f"Bank Card Created: {card}")
            input("Press Enter to continue...")
        elif choice == '6':
            address = input("Enter your address: ")
            account.RegisterAddress(address)
            print("Address registered.")
            input("Press Enter to continue...")
        elif choice == '7':
            phone_number = input("Enter your phone number: ")
            account.PhoneNumber(phone_number)
            print("Phone number registered.")
            input("Press Enter to continue...")
        elif choice == '8':
            exit = True
            print("Exiting...")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()