score =int(input("Введите значение расходов: "))
result =int(input("Введите значение доходов: "))
profit =result - score
if profit < 0:
    print("Очень жаль, но в этом периоде Ваша компания принесла только убытки")
elif profit == 0:
    print("В этом периоде Вам удалось избежать убытков")
elif profit > 0:
    print(f"Поздравляем! Прибыль Вашей компании составила {profit}")
    staff =int(input("Введите численность сотрудников: "))
    staff_profit = profit/staff
    print(f"Прибыль Вашей фирмы в пересчете на одного сотрудника составляет: {staff_profit}")


