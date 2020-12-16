sum = 0

while(True):
    my_str = input("Введите строку чисел, разделённых пробелом. Для прекращения введите q: ")
    my_list = my_str.split(" ")
    we_need_to_break = False
    for memb in my_list:
        if memb == "q":
            we_need_to_break = True
            break
        sum += float(memb)
    print(f"Сумма введённых чисел равна {sum}")
    if we_need_to_break:
        break

print(sum)