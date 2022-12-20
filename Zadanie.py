#Задание 1
n = int (input ("Введите число:"))
summa = 0
while n > 0:
    summa = summa + n % 10
    n //= 10
print('Summa =', summa)


#Задание 2
b = int(input())
lst = (round((1+1/i)**i, 3)
       for i in range(1, b+1))
print(f'Последовательность: {lst}\n Сумма элементов: {round(sum(lst), 3)}')


#Задание 3
#наверное, нужно через input, чтобы пользователь сам ввёл, но у меня получилось
# только с готовым списком

y = [5, 4, 3, 2, 1]
y.sort()
print(y)


