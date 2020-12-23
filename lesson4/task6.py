from itertools import count
from itertools import cycle

print("Реализация первого скрипта: ")
#def count_el():
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

#g = count_el()
#print(g)
#iter = cycle(g)
#print(next(iter))

print("Реализация второго скрипта: ")
my_list = [342, 343, 345, 347]
i = 0
for el in cycle(my_list):
    if i > 10:
        break
    else:
        i +=1
        print(el)




