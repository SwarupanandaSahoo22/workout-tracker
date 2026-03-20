#Expense Tracker

def add_expense(expenses):
    amount = float(input("Add your expenses: "))
    category = input("Enter expense category: ")

    expense = {
        "amount" : amount,
        "category" : category
    }
    expenses.append(expense)
    print("Expenses added successfully!")

def show_expense(expenses):
    if not expenses:
        print("No expenses recorded")
        return

    print("------ YOUR EXPENSES ------")
    print(f"{'Amount':>10} | {'Category':<15}")
    print("-" * 30)

    for expense in expenses:
        print(f"${expense['amount']:>9.2f} | {expense['category']:<15}")

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']

    return total
    
def find_highest(expenses):
    if not expenses:
        return None
    
    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

        return highest
    
def main():
    expenses = []
    is_running = True

    while is_running:
        print("--------------------")
        print("Your Expense Tracker")
        print("--------------------")
        print("1. Add Expenses")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Show highest expense")
        print("5. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense(expenses)
        
        elif choice == "2":
            show_expense(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Your total expenses: ${total}")
        
        elif choice == "4":
            highest = find_highest(expenses)

            if highest:
                print(f"Highest expense: ${highest['amount']} | ({highest['category']})")
            else:
                print("No expenses recorded.")
        
        elif choice == "5":
            is_running = False
        
        else:
            print("Invalid choice")
    
    print("Thank you! Have a nice day.")

if __name__ == '__main__':
    main()