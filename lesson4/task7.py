n = int(input("Введите число, факториал которого хотите узнать: "))

def fact(n):
    result = 1
    for el in range(1, n + 1):
        result = result*el
        yield result

for el in fact(n):
    print(el)
