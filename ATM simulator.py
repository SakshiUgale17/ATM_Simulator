# Initialize account balance
balance = 1000

# Function to check balance
def check_balance():
    print(f"Your account balance is ${balance}")

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"${amount} has been deposited successfully.")
        check_balance()
    else:
        print("Invalid amount. Please enter a positive amount.")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > 0:
        if balance >= amount:
            balance -= amount
            print(f"${amount} has been withdrawn successfully.")
            check_balance()
        else:
            print("Insufficient balance.")
    else:
        print("Invalid amount. Please enter a positive amount.")

# Main loop
while True:
    print("\nATM Simulator")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

