class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручки {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандаша {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркера {self.title}")

pen = Pen("Parker")
pen.draw()

pencil = Pencil("Koh-i-noor")
pencil.draw()

handle = Handle("Stabilo")
handle.draw()

