my_str =input("Внесите строку из нескольких слов, разделенных пробелами: ")
my_list =my_str.split()
#print(my_list)
for ind, el in enumerate(my_list,1):
    print(ind, el[0:11])
