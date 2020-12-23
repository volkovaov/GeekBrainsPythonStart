f = open("my_file.txt", "r")
lines_list = f.readlines()
f.close()

i = 1
for line in lines_list:
    words_in_line = line.split(" ")
    word_count = len(words_in_line)
    print(f"В строке {i}: {word_count} слов")
    i += 1

print(f"В файле {len(lines_list)} строк.")
