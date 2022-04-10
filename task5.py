# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title=title

    def draw(self):
        print("Запуск отрисовки.......")

class Pen2(Stationery):
    def __init__(self, title):
        super().__init__(title)

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        def __init__(self, title):
            super().__init__(title)
        print("Запуск отрисовки - 1")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки - 2")

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Запуск отрисовки -3")

eny_Stat_1 = Pen2('Oen')
eny_Stat_1.draw()
eny_Stat = Pen('Oen')
eny_Stat2 = Pencil('dfn')
eny_Stat3 = Handle('rrrn')
eny_Stat.draw()
eny_Stat2.draw()
eny_Stat3.draw()