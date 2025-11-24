import os
import json

class ATM:
    def __init__(self, users_file='users.json'):
        self.users_file = users_file
        self.current_user = None
        self.load_users()
    
    def load_users(self):
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                    data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
            except (json.JSONDecodeError, ValueError):
                data = {}
            self.users = {}
            for k, v in data.items():
                try:
                    pin = v.get('pin')
                    balance = float(v.get('balance', 0))
                except Exception:
                    pin = None
                    balance = 0.0
                self.users[str(k)] = {'pin': pin, 'balance': balance}
        else:
            self.users = {'123456': {'pin': '1234', 'balance': 100.0}}
            self.save_users()
    
    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=2)
    
    def login(self, account_number, pin):
        account_number = str(account_number)
        if account_number in self.users and self.users[account_number].get('pin') == pin:
            self.current_user = account_number
            return True
        return False
    
    def check_balance(self):
        if self.current_user:
            balance = float(self.users[self.current_user].get('balance', 0.0))
            print(f"Your balance: ${balance:.2f}")
            return balance
        print("No user is currently logged in.")
        return None
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print("Invalid amount.")
            return False
        if self.current_user and amount > 0:
            self.users[self.current_user]['balance'] = round(self.users[self.current_user].get('balance', 0.0) + amount, 2)
            self.save_users()
            print(f"Deposited: ${amount:.2f}")
            return True
        print("Deposit failed. Make sure you're logged in and the amount is positive.")
        return False
    
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print("Invalid amount.")
            return False
        if self.current_user and amount > 0:
            if self.users[self.current_user].get('balance', 0.0) >= amount:
                self.users[self.current_user]['balance'] = round(self.users[self.current_user].get('balance', 0.0) - amount, 2)
                self.save_users()
                print(f"Withdrawn: ${amount:.2f}")
                return True
            else:
                print("Insufficient balance")
                return False
        print("Withdrawal failed. Make sure you're logged in and the amount is positive.")
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
                        while True:
                            amt_str = input("Enter amount: ")
                            try:
                                amt = float(amt_str)
                                if amt <= 0:
                                    print("Enter a positive amount.")
                                    continue
                                atm.deposit(amt)
                                break
                            except ValueError:
                                print("Please enter a valid number.")
                    elif option == '3':
                        while True:
                            amt_str = input("Enter amount: ")
                            try:
                                amt = float(amt_str)
                                if amt <= 0:
                                    print("Enter a positive amount.")
                                    continue
                                if atm.withdraw(amt):
                                    break
                                else:
                                    break
                            except ValueError:
                                print("Please enter a valid number.")
                    elif option == '4':
                        atm.logout()
                        break
                    else:
                        print("Invalid option, please choose 1-4.")
            else:
                print("Invalid credentials")
        elif choice == '2':
            break
        else:
            print("Please select a valid option.")
    
if __name__ == "__main__":
    main()
