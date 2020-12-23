words = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}

f_in = open("in.txt", "r")
f_out = open("out.txt", "w")

while True:
    line = f_in.readline()
    if line == "":
        break

    new_line = ""
    words_in_line = line.split(" ")
    for word in words_in_line:
        new_word = words.get(word)
        if new_word == None:
            new_line += word
        else:
            new_line += words.get(word)
    f_out.write(new_line)

f_in.close()
f_out.close()