print("""
*************************
Read numbers between (1-100)
Press '0' for exit
*************************
""")

ones_digit = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens_digit = ["", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def read(number):
    first = number % 10
    second = number // 10

    return tens_digit[second] + " " + ones_digit[first]

while True:
    number = int(input("Number:"))
    print(read(number))
    if number == 0:
        print("Bye Bye....")
        break

