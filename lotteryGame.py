import random


def lotto_numbers():
    generated = []
    for num in range(7):
        random_num = random.randrange(1,50)
        generated.append(random_num)
    return generated


def guessed_numbers():
    user_numbers = list(input("Pick 7 numbers between 1 and 50: "))
    return user_numbers


def check_numbers(generated, user_numbers):
    correct = []
    for num in generated:
        if num in user_numbers:
            if num in generated:
                correct.append(num)


def main():
    guesses = guessed_numbers()
    winning_numbers = lotto_numbers()
    win = check_numbers(winning_numbers, guesses)
    print("The winning lotto numbers are " + str(winning_numbers))
    print("You guessed " + " "  + str(win) + " correctly")


if __name__ == '__main__':
    main()
