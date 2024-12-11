import doctest
from typing import Union


class Gun:
    """
    Модель оружия, которая содержит максимальный обьем обоймы, ее реальное заполнение и флаг стрельбы
    """
    def __init__(self, clip_capacity: int, clip_stored: int = 0, is_shooting: bool = False):
        """
        Иницилизация атрибутов класса
        :param clip_capacity: максимальное кол-во патронов, которое может вместить модель
        :param clip_stored: кол-во патронов на данный момент в обойме
        :param is_shooting: стреляет ли оружие

        Пример:
        >>> gun = Gun(30, 20, True) #инициализация экземпляра класса
        """
        self.clip_capacity = None
        self.clip_stored = None
        self.is_shooting = None
        self.__init_clip_capacity(clip_capacity)
        self.__init_clip_stored(clip_stored)
        self.__init_is_shooting(is_shooting)
    def __init_clip_capacity(self, clip_capacity: int) -> None:
        """
        Защищенный метод для инициализации атрибута clip_capacity
        :param clip_capacity: кол-во патронов в новой обойме
        :return: None
        :raise TypeError: если clip_capacity не соответствует int
        :raise ValueError: если clip_capacity не натуральное число
        """
        if not isinstance(clip_capacity, int):
            raise TypeError("clip_capacity не имеет тип int")
        if clip_capacity < 0:
            raise ValueError("магазин не может иметь отрицательное кол-во патронов")
        self.clip_capacity = clip_capacity
    def __init_clip_stored(self, clip_stored: int) -> None:
        """
        Защищенный метод для инициализации атрибута clip_stored
        :param clip_stored: положительное целое число
        :return: None
        :raises TypeError: если clip_stored не соответствует int
        :raises ValueError: если clip_stored не целое положительное число или если больше self.clip_capacity
        """
        if not isinstance(clip_stored, int):
            raise TypeError
        if clip_stored > self.clip_capacity or clip_stored < 0:
            raise ValueError
        self.clip_stored = clip_stored
    def __init_is_shooting(self, is_shooting: bool) -> None:
        """
        Защищенный метод для инициализации атрибута is_shooting
        :param is_shooting: логическая переменная
        :return: None
        :raises TypeError: если is_shooting не соответствует bool
        """
        if not isinstance(is_shooting, bool):
            raise TypeError("is_shooting не имеет тип bool")
        self.is_shooting = is_shooting
    def shoot(self) -> int:
        """
        Выстреливает из оружия 1 раз, уменьшает self.clip_stored на 1
        :return: оставшееся кол-во патронов в обойме self.clip_stored
        :raises ValueError: если self.clip_stored == 0

        Пример:
        >>> gun = Gun(10, 9)
        >>> gun.shoot()
        8
        """
        if self.clip_stored == 0:
            raise ValueError("Нет патронов в магазине")
        self.clip_stored -= 1
        return self.clip_stored
    def reload(self, clip: int) -> int:
        """
        Перезаряжает магазин оружия
        :param clip: целое число большее нуля и не превышающее атрибут clip_capacity
        :return: кол-во патронов в обойме self.clip_stored
        :raises TypeError:  если clip не int
        :raises ValueError: eсли clip < 0 или clip > self.clip_capacity

        Пример:
        >>> gun = Gun(10, 9)
        >>> gun.reload(10)
        10
        """
        if not isinstance(clip, int):
            raise TypeError("clip не имеет тип int")
        if clip < 0 or clip > self.clip_capacity:
            raise ValueError ("Новый магазин не может быть пустым")
        self.clip_stored = clip
        return self.clip_stored
class Rect:
    """
    Модель прямоугольника, содержащая длину и ширину
    """
    def __init__(self, height: Union[int, float], width: Union[int, float]):
        """
        Инициализирует атрибуты height и width
        :param height: длина прямоугольника
        :param width: ширина прямоугольника
        :raises TypeError: если не соответствуют параметры типам
        :raises ValueError: если хотя бы один параметр меньше или равен нулю

        Пример:
        >>> rect = Rect(10, 11.1)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("height не имеет тип int или float")
        if not isinstance(width, (int, float)):
            raise TypeError("width не имеет тип int или float")
        if height <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть больше нуля")
        self.height = height
        self.width = width
    def increase(self, value: Union[int, float]) -> None:
        """
        Увеличивает атрибуты на значение value
        :param value: насколько увеличить длину и ширину
        :return: None
        :raise TypeError: если не соответствует параметр типам
        :raise ValueError: если value меньше нуля

        Пример:
        >>> rect = Rect(10, 10)
        >>> rect.increase(11.5)
        """
        if not isinstance(value, (int, float)):
            raise TypeError("value не имеет тип int или float")
        if value < 0:
            raise ValueError("value не может быть отрицательным числом")
        self.height += value
        self.width += value
    def area(self) -> Union[int, float]:
        """
        Вычисление площади прямоугольника
        :return: площадь прямоугольника

        Пример:
        >>> rect = Rect(10, 10)
        >>> rect.area()
        100
        """
        return self.height*self.width
class Employee:
    """
    Модель сотрудника, содержащая имя, тип работы и зарплату
    """
    def __init__(self, name: str, job: str, salary: int) -> None:
        """
        Инициализация атрибутов класса
        :param name: имя
        :param job: название работы
        :param salary: зарплата
        :raises TypeError: если параметры не подходят по типу
        :raises ValueError: если salary <= 0

        Пример:
        >>> employee = Employee("name", "job", 100)
        """
        if not isinstance(name, str):
            raise TypeError("name не имеет тип str")
        if not isinstance(job, str):
            raise TypeError("job не имеет тип str")
        if not isinstance(salary, int):
            raise TypeError("salary не имеет тип int")
        if salary <= 0:
            raise ValueError("Зарпалата не может быть меньше или равна нулю")
        self.name = name
        self.job = job
        self.salary = salary
    def changeSalary(self, value: int) -> int:
        """
        Меняет зарплату на значение value
        :param value: натуральное число при сложении с которым, зарплата будет > 0
        :return: новую зарплату
        :raises TypeError: если параметр не подходит по типу
        :raises ValueError: если сумма self.salary и value <= 0

        Пример:
        >>> employee = Employee("Name", "Job", 10)
        >>> employee.changeSalary(15)
        25
        """
        if not isinstance(value, int):
            raise TypeError
        if self.salary + value <= 0:
            raise ValueError
        self.salary += value
        return self.salary
    def changeJob(self, job: str) -> str:
        """
        Меняет значение работы
        :param job: строка
        :return: новую работу
        :raises TypeError: если параметр не соответствует типу

        Пример:
        >>> employee = Employee("Name", "job", 10)
        >>> employee.changeJob("Job")
        'Job'
        """
        if not isinstance(job, str):
            raise TypeError
        self.job = job
        return job

if __name__ == "__main__":
    doctest.testmod()
    pass
