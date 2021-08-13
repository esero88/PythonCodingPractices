print("""
*************************
Chasing the perfect number

Please press "0" to exit
*************************
""")
while True:
    sayi = int(input("Please enter a number:"))
    if sayi == 0:
        print("Bye Bye....")
        break
    liste = []
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            liste.append(i)
    for i in liste:
        toplam = (i + toplam)
    if toplam == sayi:
        print("Bingo!! you've selected a perfect number")
    else:
        print("Doh!!, this is not a perfect number")
