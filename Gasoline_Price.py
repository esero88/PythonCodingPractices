print("Gasoline Price Calculation")

km_per_price = float(input("Amount of gasoline burned per kilometer (in Turkish penny) :"))
kilometer = int(input("Travelled distance (in kilometer) :"))

#c = km_per_price * kilometer
print("Total: {} tl".format(km_per_price * kilometer))
