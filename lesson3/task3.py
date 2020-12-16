digit_1 = int(input("введите 1е число: "))
digit_2 = int(input("введите 2е число: "))
digit_3 = int(input("введите 3е число: "))

def my_func(digit_1, digit_2, digit_3):
    my_list = [digit_1, digit_2, digit_3]
    my_list.sort(reverse = True)
    result = my_list[0] + my_list[1]
    return (result)

print(f"Сумма наибольших двух чисел равна: {my_func(digit_1, digit_2, digit_3)}")