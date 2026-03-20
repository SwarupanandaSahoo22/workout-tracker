# Bank account (OOPS)

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit must be greater than zero")
#             return
#         self._balance += amount
#         self.transactions.append(f"Deposited: ${amount}")

#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("Insufficient funds")
#         else:
#             self._balance -= amount
#             self.transactions.append(f"Withdrew: ${amount}")

#     def show_balance(self):
#         print(f"Balance: ${self._balance}")
    
#     def show_transaction(self):
#         if not self.transactions:
#             print("No transactions yet.")

#         else:
#             for t in self.transaction:
#                 print(t)

# acc1 = BankAccount("Kundan", 20000)
# acc2 = BankAccount("Aishu", 25000)

# acc2.deposit(10000)
# acc2.withdraw(500)
# acc2.show_balance()
# acc2.show_transaction()







# # Password Vault

# class PasswordVault:
#     def __init__(self):
#         self.passwords = {}

#     def add_password(self, website, password):
#         self.passwords[website] = password
#         print(f"Password saved for {website}")

#     def get_password(self, website):
#         if website in self.passwords:
#             print(f"{website}: {self.passwords[website]}")
        
#         else:
#             print("No password found for this website.")
    
# vault = PasswordVault()

# vault.add_password("gmail", "swarupa@2005")
# vault.add_password("instagram", "zxkonssus12345")

# vault.get_password("gmail")
# vault.get_password("instagram")



class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount
        self.transactions.append(f"Deposited : ${amount:,.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Current balance: ${self._balance:,.2f}")
        self._balance -= amount
        self.transactions.append(f"Withdrew  : ${amount:,.2f}")

    @property
    def balance(self):
        return self._balance

    def show_balance(self):
        print(f"Balance: ${self._balance:,.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print(f"\n--- Transactions for {self.owner} ---")
            for t in self.transactions:
                print(f"  {t}")
            print(f"  {'Current Balance':12}: ${self._balance:,.2f}")
            print("-------------------------------\n")

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance=${self._balance:,.2f})"

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance!r})"


# --- Main ---
if __name__ == "__main__":
    acc1 = BankAccount("Kundan", 20000)
    acc2 = BankAccount("Aishu", 25000)

    acc2.deposit(10000)
    acc2.withdraw(500)
    acc2.show_balance()
    acc2.show_transactions()

    print(acc1)
    print(acc2)