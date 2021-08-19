import random
import time

print(""""
************************************
Number Guessing Game

Guess a number between 1 and 40

************************************
""")

random_number = random.randint(1,40)
number_of_guesses = 7
while True:
    guess = int(input("Your guess:"))
    if guess < random_number:
        print("Please wait...")
        time.sleep(1)

        print("Please guess a higher number")

        number_of_guesses -= 1
    elif guess > random_number:
        print("Please wait...")
        time.sleep(1)

        print("Please guess a lower number")

        number_of_guesses -= 1
    else:
        print("Please wait...")
        time.sleep(1)

        print("Congratulations, Number:",random_number)
        break
    if number_of_guesses == 0:
        print("You used all your guesses...")
        print("Number:",random_number)
        break
