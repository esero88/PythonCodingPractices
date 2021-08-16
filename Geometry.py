print("""
***********************************

Shape Geometry Program

Select the geometry type that you want to enter;

1. Guadrilateral

2. Triangle

***********************************
""")

choice = int(input("Please make your choice:"))

if choice == 1:
    print("Please enter the sides in order")
    a = abs(int(input("Please enter the value of side 1: ")))
    b = abs(int(input("Please enter the value of side 2: ")))
    c = abs(int(input("Please enter the value of side 3: ")))
    d = abs(int(input("Please enter the value of side 4: ")))
    if a == b == c == d:
        print("According to the data that we have, the quadrilateral you entered is a square.")
    elif a == c and b == d:
        print("According to the data that we have, the quadrilateral you entered is a rectangle.")
    else:
        print("According to the data that we have, the quadrilateral you entered is a ordinary quadrilateral.")

elif choice == 2:
    x = abs(int(input("Please enter the value of side 1: ")))
    y = abs(int(input("Please enter the value of side 2: ")))
    z = abs(int(input("Please enter the value of side 3: ")))
    if abs(x + y) > z and abs(x + z) > y and abs(y + z) > x:
        if x == y and x == z:
            print("According to the data that we have, the triangle you entered is a equilateral triangle.")
        elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
            print("According to the data that we have, the triangle you entered is a isosceles triangle.")
        else:
            print("According to the data that we have, the triangle you entered is a scalene triangle.")
    else:
        print("According to the data we have, a triangle cannot be formed from the sides you entered.")

else:
    print("You have made invalid choice")
