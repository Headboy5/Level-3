import random as r
from faker import Faker as fk
from faker.providers import credit_card
class BankAccount:
    # Initialize the class
    def __init__(self, account_number, account_holder, sort_code, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
        self.sort_code = sort_code

    # Deposit into balance from user entry
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: £{amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw from balance - no overdrafts
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew: £{amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance

    # Display account information
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Sort Code: {self.sort_code}")

    # Create a bank card with random information
    def create_card(self):
        # Use a Faker instance (not the class) to access provider methods
        fake = fk()
        fake.add_provider(credit_card)
        expiry = fake.credit_card_expire()
        number = fake.credit_card_number()

        BankCard = {
            "card_number": number,
            "expiry_date": expiry,
            "cardholder_name": self.account_holder
        }
        return BankCard
    
    def RegisterAddress(self, address):
        self.address = address

    def PhoneNumber(self, phone_number):
        self.phone_number = phone_number

def bank():
    fake = fk()
    fake.add_provider(credit_card)
    account = BankAccount(f"{r.randint(10000000, 99999999)}", fake.name(), f"{r.randint(10, 99)}-{r.randint(10, 99)}-{r.randint(10, 99)}", r.randint(5, 9999))
    exit = False
    # Menu loop
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
        # Make this into the equivilant of a switch statement
        match choice:
            case '1':
                amount = float(input("Enter amount to deposit: £"))
                account.deposit(amount)
                input("Press Enter to continue...")
            case '2':
                amount = float(input("Enter amount to withdraw: £"))
                account.withdraw(amount)
                input("Press Enter to continue...")
            case '3':
                print(f"Current Balance: £{account.get_balance():.2f}")
                input("Press Enter to continue...")
            case '4':
                account.display_account_info()
                input("Press Enter to continue...")
            case '5':
                card = account.create_card()
                print(f"Bank Card Created: {card}")
                input("Press Enter to continue...")
            case '6':
                address = input("Enter your address: ")
                account.RegisterAddress(address)
                print("Address registered.")
                input("Press Enter to continue...")
            case '7':
                phone_number = input("Enter your phone number: ")
                account.PhoneNumber(phone_number)
                print("Phone number registered.")
                input("Press Enter to continue...")
            case '8':
                exit = True
                print("Exiting...")
                return True
            case _:
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")

def main():
    # Error handling and restart mechanism
    exit = False
    try:
        exit = bank()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if exit == False:
            if input("Would you like to restart the program? (y/n): ").lower() == 'y':
                main()
            else:
                print("Program terminated.")

if __name__ == "__main__":
    main()