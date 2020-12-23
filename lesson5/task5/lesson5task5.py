f_out = open("file.txt", "w")

list = [100, 50, 20, 1.5]
string_of_numbers = ' '.join(map(str, list))

f_out.write(string_of_numbers)

f_out.close()

f_in = open("file.txt", "r")

line = f_in.read()

f_in.close()

list_of_numbers = line.split(" ")
list_of_numbers = map(float, list_of_numbers)

print(sum(list_of_numbers))