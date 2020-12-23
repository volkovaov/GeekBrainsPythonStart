f_in = open("lessons.txt", "r")

lessons_dict = {}

while True:
    line = f_in.readline()
    if line == "":
        break

    new_line = ""
    words_in_line = line.split(" ")
    words_in_line2 = line.split(":")
    lesson_name = words_in_line2[0]

    lessons_sum = 0
    for word in words_in_line:
        if "(" in word:
            words2 = word.split("(")
            lessons_sum += int(words2[0])

    lessons_dict[lesson_name] = lessons_sum

f_in.close()

print(lessons_dict)