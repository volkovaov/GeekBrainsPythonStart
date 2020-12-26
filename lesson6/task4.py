#создаю базовый класс
class Auto:
    #создаю конструктор
    def __init__(self, s, c, n, p = False):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    #создаю методы базового класса
    def go(self):
        print(f"Автомобиль {self.name} поехал, со скоростью {self.speed}.")
    def stop(self):
        print(f"Автомобиль {self.name} остановился.")
    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")
    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} составляет {self.speed}.")

class TownCar(Auto):
    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость автомобиля {self.name} составляет {self.speed}. Обнаружено превышение скорости на {self.speed-60} км/ч!")
        else:
            print(f"Текущая скорость автомобиля {self.name} составляет {self.speed}.")

class WorkCar(Auto):
    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость автомобиля {self.name} составляет {self.speed}. Обнаружено превышение скорости на {self.speed-40} км/ч!")
        else:
            print(f"Текущая скорость автомобиля {self.name} составляет {self.speed}.")

class SportCar(Auto):
    def go(self):
        print(f"Автомобиль {self.name} рванул с места, со скоростью {self.speed}. Разгон составил 7.5 с.")

class PoliceCar(Auto):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        self.is_police = True
    def go(self):
        print(f"Полицейский автомобиль {self.name} отправился на патрулирование, со скоростью {self.speed}.")

tc_1 = TownCar(80, "Blue", "Honda")
tc_1.go()
tc_1.show_speed()
tc_1.turn("направо")

sc_1 = SportCar(120, "Red", "Lamborghini")
sc_1.go()
sc_1.show_speed()

wc_1 = WorkCar(40, "Orange", "KAMAZ")
wc_1.go()
wc_1.show_speed()
wc_1.turn("налево")

pc_1 = PoliceCar(90, "Black", "Ford")
pc_1.go()
pc_1.show_speed()
pc_1.turn("налево")
if pc_1.is_police:
    print(f"Автомобиль {pc_1.name} полицейский.")
