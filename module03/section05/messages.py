def print_message(number, guess):
    if guess > number:
        print(guess, "is too high.")
    elif guess < number:
        print(guess, " is too low.")
