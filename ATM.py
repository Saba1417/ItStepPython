import os
import json

class ATM:
    def __init__(self, users_file='users.json'):
        self.users_file = users_file
        self.current_user = None
        self.load_users()
    
    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)
        else:
            self.users = {}
    
    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def login(self, account_number, pin):
        if account_number in self.users and self.users[account_number]['pin'] == pin:
            self.current_user = account_number
            return True
        return False
    
    def check_balance(self):
        if self.current_user:
            balance = self.users[self.current_user]['balance']
            print(f"Your balance: ${balance:.2f}")
            return balance
        return None
    
    def deposit(self, amount):
        if self.current_user and amount > 0:
            self.users[self.current_user]['balance'] += amount
            self.save_users()
            print(f"Deposited: ${amount:.2f}")
            return True
        return False
    
    def withdraw(self, amount):
        if self.current_user and amount > 0:
            if self.users[self.current_user]['balance'] >= amount:
                self.users[self.current_user]['balance'] -= amount
                self.save_users()
                print(f"Withdrawn: ${amount:.2f}")
                return True
            else:
                print("Insufficient balance")
                return False
        return False
    
    def logout(self):
        self.current_user = None
        print("Logged out successfully")

def main():
    atm = ATM()
    
    while True:
        print("\n=== ATM Menu ===")
        print("1. Login")
        print("2. Exit")
        choice = input("Select option: ")
        
        if choice == '1':
            account = input("Account number: ")
            pin = input("PIN: ")
            if atm.login(account, pin):
                while True:
                    print("\n=== Account Menu ===")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    option = input("Select option: ")
                    
                    if option == '1':
                        atm.check_balance()
                    elif option == '2':
                        amount = float(input("Enter amount: "))
                        atm.deposit(amount)
                    elif option == '3':
                        amount = float(input("Enter amount: "))
                        atm.withdraw(amount)
                    elif option == '4':
                        atm.logout()
                        break
            else:
                print("Invalid credentials")
        elif choice == '2':
            break

if __name__ == "__main__":
    main()

