import random
import time

print(""""
********************
Number Guessing Game
********************
""")

def guess(x,y):
    random_number = random.randint(x,y)
    guess = 0
    number_of_guesses = 7
    while guess != random_number:
        guess = int(input(f"Guess a number between {x} and {y}: "))
        if guess < random_number:
            print("Checking your number...")
            time.sleep(1)
            print("Sorry, guess again. Your number is too low")
            number_of_guesses -= 1
        elif guess > random_number:
            print("Checking your number...")
            time.sleep(1)
            print("Sorry, guess again. Your number is too high")
            number_of_guesses -= 1
        else:
            print("Checking your number...")
            time.sleep(1)
            print(f"Bingo, Congratulations. You have guessed the number {random_number}")
            break
        if number_of_guesses == 0:
            print(f"You used all your guesses...The number was{random_number}")
            break


x = int(input("Specifiy your lower boundry: "))
y = int(input("Specifiy your upper boundry: "))
guess(x,y)
