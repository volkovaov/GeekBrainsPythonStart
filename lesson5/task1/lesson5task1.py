f = open("my_file.txt", "w")
print("Введите строки для записи в файл. Ввод завершается пустой строкой.")
str_list = []

while True:
    s = input()
    if s == "":
        break
    str_list.append(s + "\n")

f.writelines(str_list)

f.close()
