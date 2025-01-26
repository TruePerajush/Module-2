from doctest import testmod
from typing import Union
from math import pi
class Figure:
    """
    Базовая модель для фигур, реализует методы и атрибуты для работы с центром любой наследуемой фигуры
    """
    def __init__(self, x: int, y: int):
        """
        :param x: координата x
        :param y: координата y
        Атрибуты непубличны, т.к. есть методы moveBy и moveTo для работы с ними

        :raise TypeError: если не параметры не соответствуют типу int

        Пример:
        >>> figure = Figure(5, 10)
        """
        if not isinstance(x, int):
            raise TypeError("Координата 'x' должна иметь тип int")
        if not isinstance(y, int):
            raise TypeError("Координата 'y' должна иметь тип int")
        self._x = x
        self._y = y
    def area(self) -> Union[int, float]:
        """
        Заглушка, которую должен реализовать наследник
        :return: int или float, зависит от перегрузки
        """
        pass
    def center(self) -> (int, int):
        """
        Возвращает tuple с координатами центра фигуры
        :return: центр фигуры

        Пример:
        >>> figure = Figure(10, 10)
        >>> figure.center()
        (10, 10)
        """
        return (self._x, self._y)
    def moveBy(self, x:int, y:int):
        """
        Сдвигает фигуру на координаты x и y
        :param x: int
        :param y: int
        :return: None
        :raise TypeError: если параметры не имеют тип int

        Пример:
        >>> figure = Figure(10, 10)
        >>> figure.moveBy(5, 3)
        >>> figure.center()
        (15, 13)
        """
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("Параметры должны иметь тип int")
        self._x += x
        self._y += y
    def moveTo(self, x:int, y:int):
        """
        Передвигает фигуру в точку (x;y)
        :param x: int
        :param y: int
        :return: None
        :raise TypeError: если параметры не имеют тип int

        Пример:
        >>> figure = Figure(10, 10)
        >>> figure.moveTo(5, 3)
        >>> figure.center()
        (5, 3)
        """
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError("Параметры должны иметь тип int")
        self._x = x
        self._y = y
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x!r}, y={self._y!r})"
    def __str__(self) -> str:
        return f"Фигура типа {self.__class__.__name__} с центром в ({self._x};{self._y})"
class Rectangle(Figure):
    """
    Модель прямоугольника с шириной и высотой, наследуемая от модели фигуры
    Все атрибуты инкапсулированы, т.к. есть свойства для работы с ними
    """
    def __init__(self, x:int, y:int, height: int, width: int):
        """
        Все проверки происходят в свойствах
        :param x: координата x
        :param y: координата y
        :param height: высота
        :param width: ширина

        Пример:
        >>> rect = Rectangle(1, 2, 3, 4)
        """
        super().__init__(x, y)
        self.height = height
        self.width = width
    @property
    def height(self) -> int:
        return self._height
    @height.setter
    def height(self, height:int):
        """
        Сеттер для self._height
        :param height: высота
        :return: None
        :raise TypeError: если параметр не соответствует типу int
        :raise ValureError: если параметр не положительный
        """
        if not isinstance(height, int):
            raise TypeError("Параметр 'height' должeн иметь тип int")
        if not height > 0:
            raise ValueError("Параметр 'height' должeн быть положительным")
        self._height = height
    @property
    def width(self) -> int:
        return self._width
    @width.setter
    def width(self, width: int):
        """
        Сеттер для self._width
        :param width: ширина
        :return:
        :raise TypeError: если параметр не соответствует типу int
        :raise ValureError: если параметр не положительный
        """
        if not isinstance(width, int):
            raise TypeError("Параметр 'width' должeн иметь тип int")
        if not width > 0:
            raise ValueError("Параметр 'width' должeн быть положительным")
        self._width = width

    def area(self) -> int:
        """
        Возвращает площадь прямоугольника
        :return: площадь

        Пример:
        >>> rect = Rectangle(1, 2, 3, 4)
        >>> rect.area()
        12
        """
        return self.width*self.height
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x!r}, y={self._y!r}, height={self.height!r}, width={self.width!r})"
class Circle(Figure):
    """
    Модель круга с радиусом, наследуемая от модели фигуры
    Все атрибуты инкапсулированы, т.к. есть свойства для работы с ними
    """
    def __init__(self, x: int, y: int, radius: int):
        """
        Все проверки происходят в свойствах
        :param x: координата x
        :param y: координата y
        :param radius: радиус

        Пример:
        >>> circle = Circle(1, 2, 3)
        """
        super().__init__(x, y)
        self.radius = radius
    @property
    def radius(self) -> int:
        return self._radius
    @radius.setter
    def radius(self, radius: int):
        """
        Сеттер для атрибуты self._radius
        :param radius: радиус
        :return: None
        :raise TypeError: если параметр не соответствует типу int
        :raise ValueError: если параметр не положительный
        """
        if not isinstance(radius, int):
            raise TypeError("Параметр 'radius' должeн иметь тип int")
        if not radius > 0:
            raise ValueError("Параметр 'height' должeн быть положительным")
        self._radius = radius

    def area(self) -> float:
        """
        Возвращает площадь круга
        :return: площадь

        Пример:
        >>> circle = Circle(1, 2, 3)
        >>> circle.area()
        9.42477796076938
        """
        return self.radius * pi
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x!r}, y={self._y!r}, radius={self.radius!r})"
if __name__ == "__main__":
    testmod()
