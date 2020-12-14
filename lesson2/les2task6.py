#goods_list = [(1,{"название":"компьютер", "цена":20000, "количество":5, "ед":"шт."}),
#        (2,{"название":"принтер", "цена":6000, "количество":2, "ед":"шт."}),
#        (3,{"название":"сканер", "цена":2000, "количество":7, "ед":"шт."})]
""" Прописываем ввод сведений от пользователя """
n = int(input("Введите количество товаров, которые Вы хотите внести: "))
goods_list = []
for i in range(n):
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения: ")
    new_dict = {"название": name,
                "цена": price,
                "количество": quantity,
                "ед":unit}
    new_tuple = tuple([i+1, new_dict])
    goods_list.append(new_tuple)
""" Формируем аналитику """
names_list = []
prices_list = []
quantities_list = []
units_list = []

for el in goods_list:
    names_list.append(el[1].get("название"))
    prices_list.append(el[1].get("цена"))
    quantities_list.append(el[1].get("количество"))
    units_list.append(el[1].get("ед"))

analytics_dict = {"название":list(set(names_list)),
                  "цена":list(set(prices_list)),
                  "количество":list(set(quantities_list)),
                  "ед":list(set(units_list))}

print(analytics_dict)