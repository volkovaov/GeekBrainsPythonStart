from sys import argv
def zar_pay(vyrabotka, stavka, bonus):
    result=(vyrabotka * stavka) + bonus
    return result

script_name,vyrabotka, stavka, bonus = argv

print("Заработная плата работника составляет: ", zar_pay(int(vyrabotka), int(stavka), int(bonus)))
