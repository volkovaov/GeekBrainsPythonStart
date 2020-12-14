first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for i in range(0, len(first_list), 2):
    new_list.append(first_list[i])

for k in range(1, len(first_list), 2):
    new_list.insert(k-1, first_list[k])

print(new_list)
