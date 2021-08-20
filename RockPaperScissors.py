import random

print("""
*****************************
Rock - Paper - Scissors Game
*****************************
""")

def rpc():
    user = input("What is your choice? 'r' for rock, 'p' for paper 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    # r>s, s>p, p>r
    if (user == 'r' and computer == 's'):
        result = "You Won"
    elif (user == 's' and computer == 'p'):
        result = "You Won"
    elif (user == 'p' and computer == 'r'):
        result = "You Won"
    elif user == computer:
        result = "It\'s a Tie"
    else:
        result = "You Lost"
    print(result,f"Your choice is {user} and computer's choice is {computer}")

rpc()
