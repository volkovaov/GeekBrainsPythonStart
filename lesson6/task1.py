import time

class TrafficLight:
    self.__color = "Чёрный"

    def running(self):
        while True:
            print("Светофор красный")
            time.sleep(7)
            print("Светофор жёлтый")
            time.sleep(2)
            print("Светофор зелёный")
            time.sleep(7)
            print("Светофор жёлтый")
            time.sleep(2)

traffic_light = TrafficLight()
traffic_light.running()