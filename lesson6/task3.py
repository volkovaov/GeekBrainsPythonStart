class Worker:
    #создаю конструктор для экземпляров класса
    def __init__(self, n, s, p, b, w):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}

    #создаю дочерний класс
class Position(Worker):
    #создаю метогды класса
    def __init__(self, n, s, p, b, w):
        super().__init__(n, s, p, b, w)

    def get_full_name(self):
        print(f"{self.name}, {self.surname}")

    def get_total_income(self):
        print(f"Доходы сотрудника {self.name}, {self.surname} составляют: {self._income['wage'] + self._income['bonus']} галактических кредитов")

#создаю экземпляр класса
work_1 = Position("Люк", "Скайуокер", "Молодой джедай", 70000, 30000)
work_1.get_full_name()
work_1.get_total_income()









