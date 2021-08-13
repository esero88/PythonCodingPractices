import math

print("""
***********************
Calculator

Operations;

1.Addition

2.Substraction

3.Multiplication

4.Division

5.Combination

6.Absolute Value

7.Factorial

8.e^x

9.Logarithm
**********************
""")
while True:
    memory = []
    operation = int(input("Please select operation:"))
    a = float(input("a:"))
    b = float(input("b:"))
    if operation == 0:
        print("Exit...")
        break
    elif operation == 1:
        print("{} + {} = {}".format(a, b, a + b))
    elif operation == 2:
        print("{} - {} = {}".format(a, b, a - b))
    elif operation == 3:
        print("{} * {} = {}".format(a, b, a * b))
    elif operation == 4:
        print("{} / {} = {}".format(a, b, a / b))
    elif operation == 5:
        print("C({},{}) = {} dir".format(a, b, math.comb(a, b)))
    elif operation == 6:
        print("∣{}∣ = {}".format(a, math.fabs(a)))
        memory.append(math.fabs(a))
    elif operation == 7:
        print("{}! = {}".format(a, math.factorial(a)))
    elif operation == 8:
        print("e^{} = {}".format(a,math.exp(a)))
        memory.append(math.exp(a))
    elif operation == 9:
        print("log({}) = {}".format(a,math.log(a,10)))
