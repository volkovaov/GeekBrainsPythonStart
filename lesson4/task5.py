from functools import reduce

"""сгененируем список"""
my_list = [el for el in range(100, 1001) if el %2 == 0]
#print(len(my_list))
print(my_list)
"""пишем ф-цию, которой будем вычислять произведение элементов списка"""
def my_func(el, next_el):
    result = el * next_el
    return result

print(f"Произведение элементов списка равно: {reduce(my_func, my_list)}")





