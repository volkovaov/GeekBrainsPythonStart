my_str =input("Введите последовательность невозрастающих натуральных чисел: ")
rating = my_str.split(',')
for i in range(len(rating)):
   rating[i]=int(rating[i])

y =int(input("Введите натуральное число: "))

rating.append(y)
rating.sort(reverse=True)
print(rating)
