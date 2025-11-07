# BankAccount — Diagrams and program flow

This file contains diagrams for a simple bank account program: a class diagram showing main entities and a flowchart describing the program menu and feature flows. The sequence diagram below (recently added) remains unchanged.

## Class diagram (program-focused)

```mermaid
%% Class diagram: program-focused
classDiagram
class BankAccount {
  - account_holder : string
  - account_number : int
  - sort_code : string
  - balance : float
  + deposit(amount)
  + withdraw(amount)
  + get_balance()
  + display_account_info()
  + create_card()
  + register_address()
  + register_phone()
}

class BankCard {
  - card_number : string
  - expiry_date : string
  - cvv : string
  + mask_number()
}

class Program {
  + run()
  + create_account()
  + deposit()
  + withdraw()
  + check_balance()
  + create_card()
  + register_contact()
  + display_info()
  + exit()
}

```

```mermaid
%% Flowchart: program flow and features
graph TD
  Start([Start]) --> Menu[Main Menu]

  Menu --> Create[Create or Replace Account]
  Menu --> Deposit[Deposit Money]
  Menu --> Withdraw[Withdraw Money]
  Menu --> Balance[Check Balance]
  Menu --> Card[Create Bank Card]
  Menu --> Contact[Register Address and Phone]
  Menu --> Info[Display Account Info]
  Menu --> Exit[Exit]

  Create --> InputCreate[Prompt: name, sort code, initial deposit]
  InputCreate --> AccountCreated[Account Created]
  AccountCreated --> Menu

  Deposit --> PromptDeposit[Prompt: amount]
  PromptDeposit --> ValidateDeposit{amount > 0?}
  ValidateDeposit -- yes --> DoDeposit[Add to balance]
  ValidateDeposit -- no --> DepositError[Show error]
  DoDeposit --> Menu
  DepositError --> Menu

  Withdraw --> PromptWithdraw[Prompt: amount]
  PromptWithdraw --> ValidateWithdraw{sufficient balance?}
  ValidateWithdraw -- yes --> DoWithdraw[Subtract from balance]
  ValidateWithdraw -- no --> WithdrawError[Show insufficient funds]
  DoWithdraw --> Menu
  WithdrawError --> Menu

  Card --> CreateCardPrompt[Generate card data]
  CreateCardPrompt --> CardStored[Store card on account]
  CardStored --> Menu

  Contact --> PromptContact[Prompt address and phone]
  PromptContact --> StoreContact[Store on account]
  StoreContact --> Menu

  Info --> ShowInfo[Display account details and card if present]
  ShowInfo --> Menu

  Exit --> End([End])
```

---

### Sequence diagram — Program interaction examples

This sequence diagram shows typical interactions between a user, the program, and domain objects when creating an account, depositing, withdrawing, creating a card and displaying account info.

```mermaid
sequenceDiagram
  participant User
  participant Program
  participant BankAccount
  participant BankCard

  %% Create account flow
  User->>Program: Select "Create or Replace Account"
  Program->>User: Prompt for name, sort code, initial deposit
  User-->>Program: Provide name, sort code, initial deposit
  Program->>BankAccount: createAccount(name, sortCode, initialDeposit)
  BankAccount-->>Program: accountCreated(accountNumber)
  Program-->>User: Show account created confirmation

  %% Deposit flow
  User->>Program: Select "Deposit Money"
  Program->>User: Prompt for deposit amount
  User-->>Program: Provide amount
  Program->>BankAccount: deposit(amount)
  alt amount valid
    BankAccount-->>Program: newBalance
    Program-->>User: Show success and newBalance
  else invalid amount
    BankAccount-->>Program: error
    Program-->>User: Show error message
  end

  %% Withdraw flow
  User->>Program: Select "Withdraw Money"
  Program->>User: Prompt for withdrawal amount
  User-->>Program: Provide amount
  Program->>BankAccount: withdraw(amount)
  alt sufficient balance
    BankAccount-->>Program: newBalance
    Program-->>User: Show success and newBalance
  else insufficient funds
    BankAccount-->>Program: error (insufficient funds)
    Program-->>User: Show insufficient funds message
  end

  %% Create card flow
  User->>Program: Select "Create Bank Card"
  Program->>BankCard: createCardFor(accountNumber)
  BankCard-->>Program: cardCreated(maskedNumber)
  Program-->>User: Show card created confirmation (masked number)

  %% Display info flow
  User->>Program: Select "Display Account Info"
  Program->>BankAccount: getAccountInfo()
  BankAccount-->>Program: accountInfo (balance, card, contact)
  Program-->>User: Display account info

```

