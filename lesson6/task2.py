class Road:
    #создадим конструктор
    def __init__(self, lh, wh, tss, ms):
        self._length = lh
        self._width = wh
        self._thikness = tss
        self._massa = ms

    #создадим метод класса
    def result (self):
        #b = lh * wh * tss *ms
        b = self._length * self._width * self._thikness * self._massa
        print(f"Масса {self._length} метров дороги при ширине {self._width} метров с толщиной покрытия {self._thikness} метра равна {b} килограмм")

    #создадим экземпляр класса

data = Road(5000, 20, 0.05, 25)
data.result() #5000, 20, 0.05, 25)


