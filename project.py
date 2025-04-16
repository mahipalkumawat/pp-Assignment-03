import numpy as np

# User data: Names and Initial Balances
users = ['Hemant', 'Prajval', 'Badal']
balances = np.array([5000, 7000, 6000])  # Initial balance for each user
def get_user_index(name):
    if name in users:
        return users.index(name)
    else:
        return -1

# Function to check balance
def check_balance(user_index):
    print(f"\n💰 {users[user_index]}'s Current Balance: ₹{balances[user_index]}")

# Function to credit (deposit) money
def credit(user_index, amount):
    if amount > 0:
        balances[user_index] += amount
        print(f"\n₹{amount} credited successfully to {users[user_index]}'s account!")
    else:
        print("\nInvalid amount! Please enter a positive value.")
    check_balance(user_index)

# Function to withdraw money
def withdraw(user_index, amount):
    if amount > 0:
        if amount <= balances[user_index]:
            balances[user_index] -= amount
            print(f"\n₹{amount} withdrawn successfully from {users[user_index]}'s account!")
        else:
            print("\nInsufficient balance!")
    else:
        print("\nInvalid amount! Please enter a positive value.")
    check_balance(user_index)

# Main Menu
def main_menu(user_index):
    while True:
        print(f"\n===== 🏦 WELCOME {users[user_index]} 🏦 =====")
        print("1. Check Balance")
        print("2. Credit (Deposit) Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4): ")
        
        if choice == '1':
            check_balance(user_index)
        
        elif choice == '2':
            amount = float(input("Enter the amount to credit: ₹"))
            credit(user_index, amount)
        
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: ₹"))
            withdraw(user_index, amount)
        
        elif choice == '4':
            print(f"\nExiting... Thank you {users[user_index]} for using our services!")
            break
        
        else:
            print("\nInvalid choice! Please select a valid option.")

# Start the system
def start():
    print("===== MULTI-USER BANK MANAGEMENT SYSTEM =====")
    name = input("\nEnter your name (Hemant, Prajval, Badal): ").capitalize()
    
    # Get user index
    user_index = get_user_index(name)
    
    if user_index != -1:
        print(f"\nWelcome, {name}!")
        main_menu(user_index)
    else:
        print("\nUser not found! Please enter a valid name.")

# Run the system
start()