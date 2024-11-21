#Slot machine project

import random

def spin_row():
    symbols = ['🍑', '🍫', '🐈‍⬛', '🥑', '🍟']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍑':
            return bet * 3
        elif row[0] == '🍫':
            return bet * 4
        elif row[0] == '🐈‍⬛':
            return bet * 5
        elif row[0] == '🥑':
            return bet * 10
        elif row[0] == '🍟':
            return bet * 20
    else:
        return 0


def main ():
    balance = 100

    print("--------------------------")
    print("Welcome to Momo Slots!")
    print("Symbols: 🍑 🍫 🐈‍⬛ 🥑 🍟")
    print("--------------------------")

    while balance > 0:
        print(f"Your current balance is: ${balance:,.2f}")

        bet = input("How much do you want to bet: $")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than $0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you didn't win this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if not play_again == "Y":
            break

    print("-------------------------------------------------")
    print(f"Game over! Your final balance is ${balance:,.2f}")
    print("-------------------------------------------------")


if __name__ == '__main__':
    main()
