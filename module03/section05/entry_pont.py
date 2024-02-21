from messages import print_message
import randomizer


print(f"1 {__name__}")

guesses = 0
number = randomizer.get_random_number()
randomizer.test_scope()

guess = int(input("Guess my number between 1 and 1000: "))


while guess != number:
    guesses += 1
    print_message(number, guess)
    guess = int(input("Guess again: "))

print("\n\nGreat, you got it in", guesses, "guesses!")
