print("""
*******************************************
Pythagorean Theorem (Hypotenuse Calculation)
*******************************************
""")

a = int(input("a:"))
b = int(input("b:"))

hypotenuse = ((a ** 2) + (b ** 2)) ** 0.5

print("Hypotenuse side: {}".format(hypotenuse))


print("""
*******************************************
Pythagorean Theorem (Special Triangles List)
*******************************************
""")

def special_triangles():
    special_triangles_list = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                special_triangles_list.append((i, j, int(c)))

    return special_triangles_list


for i in special_triangles():
    print(i)
