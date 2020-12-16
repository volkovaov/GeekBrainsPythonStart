"""
print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))

print(ord("а"))
print(ord("я"))
print(ord("А"))
print(ord("Я"))

print(ord("a")-ord("A"))
print(chr(ord("a")-32))
"""
def int_func(my_str):
    my_list = list(my_str)
    my_list[0] = chr(ord(my_list[0])-32)
    return ''.join(my_list)

while(True):
    my_str = input("Введите слово, состоящее из маленьких латинских букв: ")
    my_list = list(my_str)
    only_small_latin = True
    for memb in my_list:
        code = ord(memb)
        if code < 97 or code > 122:
            only_small_latin = False
            break
    if only_small_latin:
        break

print(int_func(my_str))

