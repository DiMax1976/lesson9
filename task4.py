# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, direction, color, is_police):
        self.speed = speed
        # self.on_start()
        self.direction = direction
        self.color = color
        self.is_police = is_police

    # def on_start(self, speed=35): # начальная скорость, машина тронулась
    #     print(f"Let's go! initial speed of car now- {speed} km")

    def get_go(self):
        print(f"Car is going!")

    def get_stop(self):
        print(f"Car is stoping")

    def get_turn(self):
        print(f"Turn to the {self.direction}")

    def show_speed(self):
        print(f"Speed of car - {self.speed}, km")


class TownCar(Car):

    def __init__(self, speed, direction, color, is_police):
        super().__init__(speed, direction, color, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("speed exceeded!!")
        else:
            print(f"Speed of car - {self.speed}, km")


class SportCar(Car):
    def __init__(self, speed, direction, color, is_police):
        super().__init__(speed, direction, color, is_police)


class WorkCar(Car):
    def __init__(self, speed, direction, color, is_police):
        super().__init__(speed, direction, color, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("speed exceeded!!")
        else:
            print(f"Speed of car - {self.speed}, km")


class PoliceCar(Car):
    def __init__(self, speed, direction, color, is_police):
        super().__init__(speed, direction, color, is_police)


# eny_car = Car(80, 'left', 'black', False)
eny_car1 = WorkCar(60, 'right', 'red', False)
eny_car2 = PoliceCar(120, 'left', 'blue', True)
eny_car3 = TownCar(55, 'forward', 'white', False)
eny_car4 = SportCar(310, 'left', 'black', False)
# eny_car.get_go()
eny_car1.show_speed()
eny_car2.show_speed()
eny_car3.show_speed()
eny_car4.show_speed()
eny_car1.get_turn()
eny_car2.get_turn()
eny_car3.get_turn()
eny_car4.get_turn()

# eny_car.get_turn()
# eny_car4.get_go()
# eny_car3.show_speed()
# eny_car.get_stop()
