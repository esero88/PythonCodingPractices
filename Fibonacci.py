number = int(input("Up to where do you want to create the fibonacci series?: "))

a = 1
b = 1
fibonacci =[a,b]

for i in range(0,number+1):
    a,b = b,a+b
    #print("a:", a,"b:", b)
    fibonacci.append(b)
print(fibonacci)
