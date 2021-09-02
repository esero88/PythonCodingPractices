print("""
***************************
Factorial Calculation

Press 'q' for exit.
***************************
""")

while True:
    number = input("Number:")
    if (number == "q"):
        print("Bye Bye.")
        break

    else:
        number = int(number)

        factorial = 1

        for i in range(2,number+1):
            factorial *= i
        print("Factoriyel:",factorial)
