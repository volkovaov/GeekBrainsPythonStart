from random import randint
my_list = [randint(-10,10) for i in range(20)]
unique_list = [el for el in my_list if my_list.count(el)==1]
print(f"Source list:\n{my_list}\nNo repetition list:\n{unique_list}")