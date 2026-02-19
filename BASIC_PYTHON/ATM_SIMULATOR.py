# ATM_SIMULATOR
file_name = "atm_data.txt"

# balance is a global variable that stores money
balance = 1000

# pin is a global variable that stores ATM pin
pin = "1234"


# Load Data
def Load_data():
    # global keyword allows us to modify variables outside the function
    global balance, pin

    try:
        # Open the file in read mode
        file = open(file_name, "r")

        # Read all lines from the file and store them in a list
        lines = file.readlines()

        # Close the file after reading
        file.close()

        # Read the first line, remove spaces/newline, store as PIN
        pin = lines[0].strip()

        # Read the second line, remove spaces/newline,
        # convert it to integer and store as balance
        balance = int(lines[1].strip())

    except:
        # If any error occurs (file not found, invalid data, etc.)
        # program will continue with default pin and balance
        pass


# Check Balance
def check_balance():
    print("Account Balance is:", balance)


# Save Data
def save_data():
    file = open(file_name, "w")
    file.write(pin + "\n")
    file.write(str(balance))
    file.close()


# Deposit money
def deposit_money():
    global balance

    try:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        save_data()
        print("Money deposited successfully")
    except:
        print("Please enter numbers only")


# Withdraw money
def Withdraw_money():
    global balance

    try:
        amount = int(input("Enter the amount you want to withdraw: "))

        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            save_data()
            print("Please collect your cash")

    except:
        print("Please enter numbers only")


# Change PIN
def change_pin():
    global pin
    old_pin = input("Enter old PIN: ")

    if old_pin == pin:
        new_pin = input("Enter new PIN: ")
        pin = new_pin
        save_data()
        print("PIN changed successfully")
    else:
        print("Incorrect PIN")


# MAIN PROGRAM
def main():
    Load_data()

    user_pin = input("Enter the PIN: ")

    if user_pin != pin:
        print("Incorrect PIN")
        return

    while True:
        print("\n---------- ATM MENU ----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("enter ur choice:")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("thank you for using atm")
            break


main()
