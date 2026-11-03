def check_balance(balance):
    print(f"\\nAvailable balance: Rs. {balance:.2f}")
    return balance


def deposit_money(balance):
    try:
        amount = float(input("Enter amount to deposit: Rs. "))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            balance += amount
            print(f"Deposit successful. New balance: Rs. {balance:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")
    return balance


def withdraw_money(balance):
    try:
        amount = float(input("Enter amount to withdraw: Rs. "))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Please collect your cash: Rs. {amount:.2f}")
            print(f"Remaining balance: Rs. {balance:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")
    return balance


# Demo account details (for practice only)
correct_pin = "1234"
balance = 5000.00
attempts = 0
max_attempts = 3

print("========== WELCOME TO PYTHON ATM ==========")

while attempts < max_attempts:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("\\nLogin successful!")
        break
    else:
        attempts += 1
        print("Incorrect PIN.")
        print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Too many incorrect attempts. Account access blocked.")
else:
    while True:
        print("\\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = withdraw_money(balance)
        elif choice == "3":
            balance = deposit_money(balance)
        elif choice == "4":
            print("Thank you for using Python ATM!")
            break
        else:
            print("Invalid choice! Please select from 1 to 4.")
