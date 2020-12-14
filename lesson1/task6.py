a =int(input("Введите начальный результат: "))
b =int(input("Введите желаемый результат: "))
score = 1
print(f"{score}-й день: {a}")
while a <= b:
    a += a*0.1
    score += 1
    print(f"{score}-й день: {a}")
print(f"Вы достигнете ожидаемого результата через {score} дней")


