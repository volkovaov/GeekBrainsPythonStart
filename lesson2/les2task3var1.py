winter_list = [12, 1, 2]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]

month_number =int(input("Введите число, соответствующее месяцу года: "))
if month_number > 12 or month_number < 1:
    print("Введено неправильное число! Попробуйте снова!")
if month_number in winter_list:
    print("Время года - зима!")
elif month_number in spring_list:
    print("Время года - весна!")
elif month_number in summer_list:
    print("Время года - лето!")
elif month_number in autumn_list:
    print("Время года - осень!")