import random 
import string 
import os.path 

class Account: 
    def __init__(self, account_type): 
        self.account_type = account_type 
        self.account_number = None 
        self.balance = 0 

def create_account(): 
    # Ask for the account type 
    account_type = input("Which type of bank account would you like to open?\n1. Business Account\n2. Personal Account\nEnter 1 or 2\n-> ") 

    if account_type == "1": 
        account_type = "BusinessAccount" 
        print("Your Business Account has been created.\nPlease have your account number and default password:") 
    elif account_type == "2": 
        account_type = "PersonalAccount" 
        print("Your Personal Account has been created.\nPlease have your account number and default password:") 
    else: 
        print("Wrong input") 
        return 

    # Create an instance of the Account class 
    account = Account(account_type) 

    # Generate the account number 
    account.account_number = ''.join(random.choices(string.digits, k=9)) 
    print(f"Account number: {account.account_number}") 

    # Generate a random password 
    password_length = 4 
    password_characters = string.digits 
    password = ''.join(random.choices(password_characters, k=password_length)) 
    print(f"Default password: {password}") 

    # Save the account details to a file 
    if not os.path.isfile("account.txt"): 
        open("account.txt", "w").close() 

    with open("account.txt", "a") as f: 
        f.write(f"{account.account_type},{account.account_number},{password},{account.balance}\n") 

def WithDraw(account_number): 
    # ask user for the amount to withdraw 
    amount = int(input("Enter the amount you want to withdraw: ")) 

    # Find the account details from the file 
    account_details = next((line.strip().split(',') for line in open('account.txt', 'r') if int(line.split(',')[1]) == account_number), None) 

    if account_details is not None: 
        balance = int(account_details[3]) 

        if amount <= balance: 
            balance -= amount 

            # Update the file with the new balance 
            with open('account.txt', 'r') as f: 
                lines = f.readlines() 
            with open('account.txt', 'w') as f: 
                for line in lines: 
                    if int(line.split(',')[1]) == account_number: 
                        f.write(f"{account_details[0]},{account_details[1]},{account_details[2]},{balance}\n") 
                    else: 
                        f.write(line) 

            print(f"Money is successfully withdrawn!\nYour current balance is: Nu.{balance}") 
        else: 
            print("Insufficient balance") 
    else: 
        print("Account not found") 

def Deposit(account_number): 
    # ask user for the amount to deposit 
    amount = int(input("Enter the amount you want to deposit: Nu. ")) 

    # Find the account details from the file 
    account_details = next((line.strip().split(',') for line in open('account.txt', 'r') if int(line.split(',')[1]) == account_number), None) 

    if account_details is not None: 
        balance = int(account_details[3]) 
        balance += amount 

        # Update the file with the new balance 
        with open('account.txt', 'r') as f: 
            lines = f.readlines() 
        with open('account.txt', 'w') as f: 
            for line in lines: 
                if int(line.split(',')[1]) == account_number: 
                    f.write(f"{account_details[0]},{account_details[1]},{account_details[2]},{balance}\n") 
                else: 
                    f.write(line) 

        print(f"Amount is successfully deposited!\nYour current balance is: Nu.{balance}") 
    else: 
        print("Account not found") 

def Transfer(account_number): 
    # ask user for the recipient's account number 
    reciever_account_number = int(input("Enter the recipient account number: ")) 

    # Check if the recipient account exists 
    if reciever_account_number in [int(line.split(',')[1]) for line in open('account.txt', 'r')]: 

        # ask user for the amount to transfer 
        amount = int(input("Enter the amount you want to transfer: Nu. ")) 

        # Find the sender's account details 
        account_details = next((line.strip().split(',') for line in open('account.txt', 'r') if int(line.split(',')[1]) == account_number), None) 

        if account_details is not None: 
            sender_balance = int(account_details[3]) 

            if amount > sender_balance: 
                print("Insufficient balance") 
                return 

            # Find the recipient's account details from account.txt. 
            reciever_details = next((line.strip().split(',') for line in open('account.txt', 'r') if int(line.split(',')[1]) == reciever_account_number), None) 

            if reciever_details is not None: 
                reciever_balance = int(reciever_details[3]) 
                sender_balance -= amount 
                reciever_balance += amount 

                # Update the file with the new balances 
                updated_accounts = [] 
                for line in open('account.txt', 'r'): 
                    if int(line.split(',')[1]) == account_number: 
                        updated_accounts.append(f"{account_details[0]},{account_details[1]},{account_details[2]},{sender_balance}\n") 
                    elif int(line.split(',')[1]) == reciever_account_number: 
                        updated_accounts.append(f"{reciever_details[0]},{reciever_details[1]},{reciever_details[2]},{reciever_balance}\n") 
                    else: 
                        updated_accounts.append(line) 

                with open('account.txt', 'w') as f: 
                    f.writelines(updated_accounts) 

                print(f"Amount is successfully transferred!\nYour current balance is: Nu.{sender_balance}") 
            else: 
                print("Recipient account not found") 
        else: 
            print("Sender account not found") 
    else: 
        print("Recipient account not found") 

def Delete(account_number): 
    # ask user for confirmation 
    answer = input("Are you sure you want to delete your account (yes/no)? ") 

    if answer.lower() == 'yes': 
        # Read all lines from the file 
        with open('account.txt', 'r') as f: 
            lines = f.readlines() 

        # Write back all lines except the one to be deleted 
        with open('account.txt', 'w') as f: 
            for line in lines: 
                if int(line.split(',')[1]) != account_number: 
                    f.write(line) 

        print("Your account has been deleted.") 
    else: 
        print("Account deletion cancelled.") 

def Login(): 
    # ask user for the account number 
    account_number = int(input("Enter the account number: ")) 

    # Check if the account number exists 
    if account_number in [int(line.split(',')[1]) for line in open('account.txt', 'r')]: 

        # input from user for the password 
        password = int(input("Enter the password: ")) 

        # Find the account details 
        account_details = next((line.strip().split(',') for line in open('account.txt', 'r') if int(line.split(',')[1]) == account_number), None) 

        if password == int(account_details[2]): 
            print(f"Your balance is: Nu.{account_details[3]}") 

            # input from user for the action to perform 
            option = int(input("What do you want to do:\n1.WithDraw\n2.Deposit\n3.Transfer\n4.Delete Account\nPlease Enter the number: ")) 

            if option == 1: 
                WithDraw(account_number) 
            elif option == 2: 
                Deposit(account_number) 
            elif option == 3: 
                Transfer(account_number) 
            elif option == 4: 
                Delete(account_number) 
        else: 
            print("Incorrect password") 
    else: 
        print("Account not found") 

def main(): 
    print("KUZANGPOLA!\nWelcome to the banking application!") 

    # initial action 
    ans = input("What do you want to do:\n1. Log in to my account\n2. Create a new account\nPlease select the number: ") 

    if ans == "1": 
        Login() 
    elif ans == "2": 
        create_account() 
    else: 
        print("Error in input") 

if __name__ == "__main__": 
    main()
