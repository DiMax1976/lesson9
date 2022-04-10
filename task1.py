# Создать класс TrafficLight (светофор).
#
#     определить у него один атрибут color (цвет) и метод running (запуск);
#     атрибут реализовать как приватный;
#     в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#     продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#     переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#     проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    __color = 0

    def __change_color(self):

        for i in range(1, 5):
            TrafficLight.__color = i
            if TrafficLight.__color == 1:
                print(' \033[31m\033[40m\033[7m', '\r', end="")
                print(TrafficLight.__color, 'red', end="")
                time.sleep(7)
            elif TrafficLight.__color == 2:
                print(' \033[33m\033[40m\033[7m', '\r', end="")
                print(TrafficLight.__color, 'yellow', end="")
                time.sleep(2)
            elif TrafficLight.__color == 3:
                print(' \033[32m\033[40m\033[7m', '\r', end="")
                print(TrafficLight.__color, 'green', end="")
                time.sleep(5)
            else:
                print(' \033[0m', '\r', end="")
                print("Off")
            print(' \033[0m', '\r', end="")

    def running(self):
        print("TrafficLight On!", TrafficLight.__color, )
        self.__change_color()


traf_lht = TrafficLight()  # создали светофор - два раза запускаем
traf_lht.running()  # включили светофор
