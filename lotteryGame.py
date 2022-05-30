# A Lottery game including a $1,000,000 payout
import random

# Generates 7 lottery random numbers from a range between 1 and 50 and sorts them into order.
# Used that random.sample function so the game will not produce duplicates
def lotto_numbers():
    generated = random.sample(range(1, 50), 7)
    generated.sort()
    return generated

# Asks for user's numbers and sorts into a list. With exception control
def guessed_numbers():
    picks = 7
    i = 0
    user_numbers = []
    while i < picks:
        entries = int(input("Pick 7 numbers between 1 and 50. Pick #{0}: ".format(i + 1)))
        if entries <= 0 or entries > 50:
            print("That's not a valid number. Pick a number between 1 and 50.")
        else:
            user_numbers.append(entries)
            user_numbers.sort()
            i = i + 1
    return user_numbers

# Checks user numbers against generated numbers and scores how many were correct.
def check_numbers(winning_numbers, guesses):
    score = 0
    for element in winning_numbers:
        if element in guesses:
            score += 1
    return score

# Check score against payout table.
def winning_payout(win):
    if win == 7:
        return "You have won $1,000,000!"
    elif win == 6:
        return "You have won $50,000!"
    elif win == 5:
        return "You have won $10,000!"
    elif win == 4:
        return "You have won $5,000!"
    elif win == 3:
        return "You have won $1,000!"
    elif win == 2:
        return "You have won $100!"
    elif win == 1:
        return "You have won $50!"
    else:
        return "Sorry you didn't win. Try playing again."

# Main game loop
def main():
    print("Welcome to the lottery game \n Let's GO!!!!!")
    try:
        guesses = guessed_numbers()
        winning_numbers = lotto_numbers()
        win = check_numbers(winning_numbers, guesses)
        payout = winning_payout(win)
        print("You guessed: " + str(guesses) + "\nThe winning lotto numbers are "
              + str(winning_numbers) + "\nYou guessed " + str(win) + " correctly \n" + payout)

    finally:
        while True:
            play_again = input("Would you like to play again? (Y/N) ")
            if play_again.lower() == "y":
                main()
            if play_again.lower() != "n":
                print("Unexpected answer. Try again. Y or N?")
            else:
                break


if __name__ == '__main__':
    main()
