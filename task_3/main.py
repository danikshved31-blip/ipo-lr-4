num = int(input("Введите число: "))
if num < 1:
    print("Число не простое")
else:
    i = 2
    while i < num:
        num % i != 0
        i+ = 1
        print ("Простое чило")
