first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78,  123, 55]

#new_list = [(i, el) for i, el in first_list if el[i] < el[i + 1]]

#new_list = [el[i+1]  if el[i] < el[i+1] for i in range(len(first_list))]```

#new_list = [el_next for el in first_list if el < el_next]

new_list = [first_list[i+1] for i in range(len(first_list) -1) if first_list[i] < first_list[i+1]]

print(new_list)
