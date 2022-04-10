# 3. Реализовать базовый класс Worker (работник)    .
# определить атрибуты: name, surname, position (д олжность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, _income):
        bonus=2000
        wage=500
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        salary = self._income

        print(salary["wage"]+ salary["bonus"])


p_r = Position('Вася', 'Иванов', 'дворник', 0)
print(vars(p_r))
p_r.get_full_name()
p_r.get_total_income()

p_r_2 = Position('Джао', 'Хунянь', 'директор',1)
# print(vars(p_r))
p_r_2.get_full_name()
p_r_2.get_total_income()
