#Banking Program

# def show_deposit(balance):
#     print(f"Your balance is: ${balance:.2f}")

# def deposit():
#     amount = float(input("Enter an amount to be deposited: "))

#     if amount < 0:
#         print("That's not a valid amount")
#         return 0
#     else:
#         return amount

# def withdraw(balance):
#     amount = float(input("Enter an amount to be withdrawn: "))

#     if amount > balance:
#         print("Insufficent balance")
#         return 0
#     elif amount < 0:
#         print("Amount must be greater than 0")
#         return 0
    
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print("*" * 30)
#         print("Welcome the Bank")
#         print("*" * 30)
#         print("1. Show deposit")
#         print("2. Show balance")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             show_deposit(balance)
#         elif choice == '2':
#             balance += deposit()
#         elif choice == '3':
#             balance -= withdraw(balance)
#         elif choice == '4':
#             is_running = False
#         else:
#             print("Invalid choice!")

#     print("Thank you! Have a nice day!")

# if __name__ == '__main__':
#     main()







# ATM program

def show_deposit(balance):
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be deposited: "))

    if amount < 0:
        print("That's an invalid amount")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be grrater than zero")
        return 0
    else:
        return amount
    

def main():
    balance = 2000
    is_running = True
    transaction = []

    while is_running:
        print("*************************")
        print("WELCOME TO THE ATM")
        print("*************************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction histoy")
        print("5. Exist")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_deposit(balance)

        elif choice == "2":
            x = deposit()
            balance += x
            transaction.append(f"Deposited: ${x}")

        elif choice == "3":
            y = withdraw(balance)
            if x > 0:
                balance -= y
                transaction.append(f"Withdrew: ${y}")
        
        elif choice == "4":
            if transaction:
                for t in transaction:
                    print(t)
            else:
                print("No transactions yet")
            
        elif choice == "5":
            is_running = False
            
        else:
            print("Invalid choice!")
            
    print("Thank you! Have a nice day.")
  
if __name__ == '__main__':
    main()
