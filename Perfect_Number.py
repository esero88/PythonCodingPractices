print("""
*************************
Chasing the perfect number

Please press "0" to exit
*************************
""")
while True:
    var_num = int(input("Please enter a number:"))
    if var_num == 0:
        print("Bye Bye....")
        break
    lst = []
    tot = 0
    for i in range(1, var_num):
        if var_num % i == 0:
            lst.append(i)
    for i in liste:
        tot = (i + tot)
    if tot == var_num:
        print("Bingo!! you've selected a perfect number")
    else:
        print("Doh!!, this is not a perfect number")
