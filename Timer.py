#Timer

# import time

# my_timer = int(input("Enter time in seconds: "))

# for i in range (my_timer, 0, -1):
#     seconds = i % 60
#     minutes = int(i / 60) % 60
#     hours = int(i / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIMES UP!")






# Loops revision

# i = 50
# while i > 0:
#     print(i)
#     i -= 1

         #OR

# for i in range(50, 0, -1):
#     print(i)


# total = 1
# for i in range (1, 101):
#     if i % 7 == 0:
#         print(i)
#         total += 1
    
# i = 1
# while i <= 5:
#     if i == 3:
#         break
#     print (i)
#     i += 1






# even_count = 0
# odd_count = 0
# largest = None
# num = []
# is_running = True

# while is_running:
#     nums = input("Enter number (or type 's' to stop): ").lower()
#     if nums == "s":
#         break
#     else:
#         nums = int(nums)
#         num.append(nums)

# for nums in num:
#     if nums % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

#     if largest is None:
#         largest = nums
#     elif nums > largest:
#         largest = nums

# print(f"Total even numbers: {even_count}")
# print(f"Total odd numbers: {odd_count}")
# print(f"Lagest number: {largest}")




# count = 0
# is_running = True

# while is_running:
#     num = input("Enter number (or type 's' to stop): ").lower()
#     if num == "s":
#         break
#     else:
#         num = int(num)

#     if num < 0:
#         pass
#     elif num >= 10:
#         count +=1

# print(count)




# def multiply(a, b):
#     return a * b

# result = multiply(4, 2345673)
# print(result)





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









import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
is_running = True
guesses = 0
attempts = 7

print("Welcome to the number gussesing game!")
print(f"Choose a number between {lowest_num} and {highest_num}")


while is_running and attempts > 0:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Invalid range!")
            print(f"Please choose a number between {lowest_num} and {highest_num}")
        elif guess > answer:
            print("Too high! Try again.")
        elif guess < answer:
            print("Too low! Try again")
            
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Your number of guessess were: {guesses}")
            is_running = False
        
        attempts -= 1
        print(f"Attempts left: {attempts}")
    
    else:
        print("Invalid guess")
        print(f"Please choose a number between {lowest_num} and {highest_num}")

    if attempts == 0:
        print(f"You lost. The number was {answer}")