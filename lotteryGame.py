# A Lottery game including a $1,000,000 payout
import random
import time


# Generates 7 lottery random numbers from a range between 1 and 50 and sorts them into order.
# Used that random.sample function so the game will not produce duplicates
def lotto_numbers():
    generated = random.sample(range(1, 51), 7)
    time.sleep(1)
    print("Here comes the winning numbers...")
    for x in generated:
        time.sleep(1)
        print("Drawing... ", x)
    generated.sort()
    return generated


# Asks for user's numbers. Returns user numbers as a list.
# User control for value exceptions and picking the same number.
def guessed_numbers():
    picks = 7
    i = 0
    user_numbers = []

    print("Pick 7 numbers between 1 and 50.".center(50))

    while i < picks:
        try:
            entries = int(input("Pick #{0}: ".format(i + 1)))
            if entries <= 0 or entries > 50:
                print("That's not a valid number. Pick a number between 1 and 50.")
            elif entries in user_numbers:
                print("You already picked that number. Try another.")
            else:
                user_numbers.append(entries)
                user_numbers.sort()
                i = i + 1
        except ValueError:
            print("Oops. Please enter a valid number.")

    return user_numbers


# Checks user numbers against generated numbers, scores how many were correct.
# Returns both the score and the numbers correctly guessed.
def check_numbers(winning_numbers, guesses):
    correct = []
    score = 0
    for number in winning_numbers:
        if number in guesses:
            correct.append(number)
            score += 1
    return score, correct


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
    header = "".center(60, "#")
    print(header, "\n")
    print("\tWelcome to the lottery game\t".center(50, "#"))
    print("\tLet's Go!\t".center(48, "#"), "\n")
    print(header)
    try:
        guesses = guessed_numbers()
        winning_numbers = lotto_numbers()
        win = check_numbers(winning_numbers, guesses)
        payout = winning_payout(win[0])
        print(" ", "\n" + header, "\nYou guessed: ", str(guesses), "\n\nThe winning lotto numbers are ",
              str(winning_numbers), "\n\nYou hit the numbers: ", str(win[1]), "\n\nYou guessed ",
              str(win[0]), "correctly.", "\n")
        print(payout)
        print(header)

    finally:
        while True:
            play_again = input("\nWould you like to play again? (Y/N) ")
            if play_again.lower() == "y":
                main()
            elif play_again.lower() != "n":
                print("Unexpected answer. Try again. Y or N?")
            else:
                break


if __name__ == '__main__':
    main()
