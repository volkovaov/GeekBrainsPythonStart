a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

def calc_result(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        c = None
    return(c)

print(calc_result(a, b))
