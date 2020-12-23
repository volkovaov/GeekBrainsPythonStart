f = open("staff.txt", "r")
lines_list = f.readlines()
f.close()

salary_less_than_20000 = []
salary_sum = 0
for line in lines_list:
    words = line.split(" ")
    surname = words[0]
    salary = int(words[1])
    salary_sum += salary
    if salary < 20000:
        salary_less_than_20000.append(surname)

if len(salary_less_than_20000) > 0:
    print("Сотрудники с окладом менее 20000:")
    print(salary_less_than_20000)

print(f"Средний доход сотрудника = {salary_sum / len(lines_list)}")

