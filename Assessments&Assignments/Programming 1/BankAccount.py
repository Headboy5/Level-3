import random as r
from faker import Faker as fk
from faker.providers import credit_card


class BankAccount:
    # Initialize the class
    def __init__(self, account_number = 0, account_holder = "N/A", sort_code = "00-00-00", balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        # _balance is treated as a "protected" attribute (leading underscore)
        # — not enforced, but communicates callers should use get_balance()/deposit()/withdraw().
        self._balance = balance
        self.sort_code = sort_code
        self.faker = fk()
        self.faker.add_provider(credit_card)

    def create_account(self):
        # Create a new account by prompting the user (keep it simple and explicit)
        name = input("Enter account holder name (or leave blank for a random name): ").strip()
        if not name:
            name = fk().name()
        sort_code = input("Enter sort code (or leave blank for auto-generated): ").strip()
        if not sort_code:
            sort_code = f"{r.randint(10, 99)}-{r.randint(10, 99)}-{r.randint(10, 99)}"
        init_dep = input("Initial deposit amount (or leave blank for 0): ").strip()
        try:
            init_dep_val = float(init_dep) if init_dep else 0.0
        except ValueError:
            print("Invalid initial deposit - defaulting to 0.")
            init_dep_val = 0.0
        account = BankAccount(f"{r.randint(10000000, 99999999)}", name, sort_code, init_dep_val)
        account.display_account_info()
        return account

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

    # Simple getters/setters to demonstrate encapsulation (assignment requirement)
    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, name):
        if not name or not str(name).strip():
            raise ValueError("Account holder name cannot be empty.")
        self.account_holder = str(name).strip()

    def get_sort_code(self):
        return self.sort_code

    def set_sort_code(self, sc):
        if not sc or not str(sc).strip():
            raise ValueError("Sort code cannot be empty.")
        self.sort_code = str(sc).strip()

    @property
    def balance(self):
        """Read-only property for balance (getter). Use deposit()/withdraw() to change."""
        return self._balance

    # Display account information
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Sort Code: {self.sort_code}")
        # Also show the current balance as part of account details
        print(f"Balance: £{self._balance:.2f}")

    # Create a bank card with random information
    def create_card(self):
        expiry = self.faker.credit_card_expire()

        # `credit_card_number()` generates a plausible card number string. In the
        # earlier version of this file a manual random grouping was used; Faker
        # provides the same and is easier to read.
        number = self.faker.credit_card_number()

        BankCard = {
            "card_number": number,
            "expiry_date": expiry,
            "cvv": self.faker.credit_card_security_code()
        }
        return BankCard
    
    def RegisterAddress(self, address):
        self.address = address
        # Minimal validation: do not accept empty addresses
        if not address or not str(address).strip():
            print("Invalid address. Address not registered.")
            return
        self.address = str(address).strip()

    def PhoneNumber(self, phone_number):
        self.phone_number = phone_number
        # Minimal validation: do not accept empty phone numbers
        if not phone_number or not str(phone_number).strip():
            print("Invalid phone number. Phone number not registered.")
            return
        self.phone_number = str(phone_number).strip()

def bank():
    account = BankAccount()
    account = account.create_account()
    repeat = True
    # Menu loop
    while repeat:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Create Bank Card")
        print("6. Register Address and Phone Number")
        print("7. Display Account Info")
        print("8. Exit")

        choice = input("Choose an option: ")
        # Menu choice handling using match-case
        match choice:
            # Create a new account
            case '1':
                account = account.create_account()
                input("Press Enter to continue...")
            # Deposit money
            case '2':
                try:
                    amount = float(input("Enter amount to deposit: £"))
                except ValueError:
                    print("Invalid amount input. Deposit cancelled.")
                    input("Press Enter to continue...")
                    continue
                try:
                    account.deposit(amount)
                    print(f"Deposited: £{amount:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
                input("Press Enter to continue...")
            # Withdraw money
            case '3':
                try:
                    amount = float(input("Enter amount to withdraw: £"))
                except ValueError:
                    print("Invalid amount input. Withdrawal cancelled.")
                    input("Press Enter to continue...")
                    continue
                try:
                    account.withdraw(amount)
                    print(f"Withdrew: £{amount:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
                input("Press Enter to continue...")
            # Check balance
            case '4':
                print(f"Current Balance: £{account.get_balance():.2f}")
                input("Press Enter to continue...")
            # Create a bank card
            case '5':
                card = account.create_card()
                print(f"Bank Card Created: {card}")
                input("Press Enter to continue...")
            # Register address and phone number
            case '6':
                address = input("Enter your address: ")
                account.RegisterAddress(address)
                if hasattr(account, 'address') and account.address:
                    print("Address registered.")
                phone_number = input("Enter your phone number: ")
                account.PhoneNumber(phone_number)
                if hasattr(account, 'phone_number') and account.phone_number:
                    print("Phone number registered.")
                input("Press Enter to continue...")
            # Display account info
            case '7':
                account.display_account_info()
                input("Press Enter to continue...")
            # Exit
            case '8':
                repeat = False
                print("Exiting...")
                return False
            # Invalid option
            case _:
                print("Invalid option. Please try again.")
                input("Press Enter to continue...")

def main():
    ()
    # Error handling and restart mechanism
    repeat = True
    try:
        repeat = bank()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # If the program did not exit cleanly we offer a restart. The current
        # implementation calls `main()` recursively which is okay for a small
        # number of restarts but could grow the call stack if abused. A looped
        # restart (while True:) would avoid recursion and is safer long-term.
        if repeat == True:
            if input("Would you like to restart the program? (y/n): ").lower() == 'y':
                main()
            else:
                print("Program terminated.")
if __name__ == "__main__":
    main()