class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Параметр 'name' должен иметь тип str")
        if not isinstance(author, str):
            raise TypeError("Параметр 'author' должен иметь тип str")
        self._name = name
        self._author = author
    @property
    def name(self) -> str:
        return self._name
    @property
    def author(self) -> str:
        return self._author
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages
    @property
    def pages(self) -> int:
        return self._pages
    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Параметр 'pages' должен иметь тип int")
        if not pages > 0:
            raise ValueError("Параметр 'pages' должен быть положительным")
        self._pages = pages
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), pages={self.pages!r}"
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    @property
    def duration(self) -> float:
        return self._duration
    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Параметр 'duration' должен иметь тип float")
        if not duration > 0:
            raise ValueError("Параметр 'duration' должен быть положительным")
        self._duration = duration
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), duration={self.duration!r}"
