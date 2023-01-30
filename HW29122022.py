while True:
    number = int(input('Введите число'))
    if number > 0 and number < 10:
        print (number**3)
        break
    else:
        print ("Введите число в указанном диапозоне 1....10")
