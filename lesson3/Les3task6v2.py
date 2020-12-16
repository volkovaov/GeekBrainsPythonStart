
def int_func(my_str):
    my_list = list(my_str)
    my_list[0] = chr(ord(my_list[0])-32)
    return ''.join(my_list)

my_str = input("Введите несколько слов, состоящих из маленьких латинских букв, разделённые пробелом: ")
list_words = my_str.split(" ")
result = ""
for word in list_words:
    result += int_func(word) + " "

print(result)