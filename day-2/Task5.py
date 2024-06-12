import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    while guess != number_to_guess:
        guess = int(input("Enter your guess (1-100): "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Correct! You guessed the number.")

# Example usage
guess_the_number()
