# EXPENSE_TRACKER_PROJECT
file_name = "expenses.txt"

expenses = []


# Load old expenses from file
def load_expenses():
    try:
        file = open(file_name, "r")
        for line in file:
            expenses.append(int(line.strip()))
        file.close()
    except:
        # If file does not exist, start with empty list
        pass


# Save expenses to file
def save_expenses():
    file = open(file_name, "w")
    for exp in expenses:
        file.write(str(exp) + "\n")
    file.close()


# Add new expense
def add_expense():
    try:
        amount = int(input("Enter expense amount: "))
        expenses.append(amount)
        save_expenses()
        print("Expense added successfully")
    except:
        print("Please enter numbers only")


# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded")
    else:
        print("Your expenses:")
        for i in range(len(expenses)):
            print(i + 1, "->", expenses[i])


# Calculate total expense
def total_expense():
    total = sum(expenses)
    print("Total expense is:", total)


# Main program
def main():
    load_expenses()

    while True:
        print("\n------ EXPENSE TRACKER MENU ------")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Thank you for using Expense Tracker")
            break

        else:
            print("Invalid choice, try again")


main()
