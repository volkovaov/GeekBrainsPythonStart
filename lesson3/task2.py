

def card(name, surname, date, city, e_mail, teltfon):

    print(f"{name},{surname},{date},{city},{e_mail},{teltfon}")

name = input("Введите Ваше имя: ")
surname = input("Введите Вашу фамилию: ")
date = input("Введите дату Вашего рождения: ")
city = input("Введите название горолда, в котором Вы живете: ")
e_mail = input("Введите адрес своей электронной почты: ")
teltfon = input("Введите номер своего телефона: ")

card(name, surname, date, city, e_mail, teltfon)
