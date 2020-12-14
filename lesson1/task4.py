n = (int(input("Введите целое положительное число: ")))
gross = n % 10
tail = n
while tail > 0:
    digit = tail % 10
    if digit > gross:
        gross = digit
        if gross == 9:
            break
    tail = tail // 10
print(f"Наибольшая цифра в числе {n}, равна {gross}")