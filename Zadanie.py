z = int(input('Введите число: '))

def get_fibonacci(z):
    fib_nums = []
    a, b = 1, 1
    for i in range(z-1):
        fib_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (z):
        fib_nums.insert(0, a)
        a, b = b, a - b
    return fib_nums

fib_nums = get_fibonacci(z)
print(get_fibonacci(z))
