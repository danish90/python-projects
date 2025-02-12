#create a simplified ATM Simulation program; user can perform basic transactions, such as checking their balance, depositing money, withdrawing money

def ATM_options():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def current_balance(balance):
    print(f"Your current balance is: ${balance:,.2f}")

def deposit():
    amount = float(input(f"Enter an amount to deposit: "))

    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input(f"Enter amount to withdraw: "))

    if amount > balance:
        print(f"You do not have enough funds. Your balance is ${balance:,.2f}")
        return 0
    elif amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount


def main():

    balance = 100

    print()
    print("Welcome to the ATM!")
    print()
 
    while True:

        print(f"Current Balance: ${balance:,.2f}")
        ATM_options()
        option = int(input(f"Choose an option: "))

        if option == 1:
            current_balance(balance)
            print()
        elif option == 2:
            # deposit() #this is not needed as python will execute it in the line below; if run by itself, it will not be able to store the value anywhere
            deposit_amount = deposit()
            if deposit_amount > 0:
                balance += deposit_amount #python's order of operations STARTS from right, and goes to left.  by writing it this way, python will execute the deposit() function first, so it can store the value, then add it to balance
                print(f"Deposit successful! Your new balance is: ${balance:,.2f}")
                print()
            else:
                print("Deposit unsuccessful. Please try again")
                print()
        elif option == 3:
            withdraw_amount = withdraw(balance)
            if balance > withdraw_amount > 0:
                balance -= withdraw_amount
                print(f"Withdrawal sucessful! Your new balance is: ${balance:,.2f}")
                print()
            else:
                print("Withdrawal unsuccessful. Please try again")
                print()
        elif option == 4:
            print("Thank you for using the ATM. Goodbye.")
            break
        else:
            print("That wasn't a valid option. Please try again")
            print()
            # option = int(input(f"Choose an option: "))

if __name__ == '__main__':
    main()
