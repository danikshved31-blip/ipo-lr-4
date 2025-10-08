num = int(input("Введите число: "))
if num < 1:
    print("Число не простое")
elif num == 1 and num == 2:
    print("число простое")
else:
    i = 2
    while i < num:
        if num % i != 0:   
            i+= 1
            print ("число простое ")
            break
        else:
            print("число не простое")
            break
