class Rub(object):
    """ Класс для работы с рублями и копейками."""
    def __init__(self, rub=0, kop=0):  # Инициализация объекта класса Rub
        self.rub = rub  # Установка значения рублей
        self.kop = kop  # Установка значения копеек
        self.normalize()  # Нормализация значений
    def normalize(self):  # Метод для нормализации значений
        self.rub += self.kop // 100  # Перевод копеек в рубли
        self.kop %= 100  # Оставшиеся копейки после перевода в рубли
    def __str__(self):  # Метод для преобразования объекта в строку
        return f'{self.rub}.{str(self.kop).zfill(2)} rub'  # Возвращает строку в формате "рубли.копейки rub"
    def __lt__(self, other):  # Метод для сравнения двух объектов класса Rub
        return self.rub < other.rub or (self.rub == other.rub and self.kop < other.kop)  # Сравнивает рубли, затем копейки
    def __add__(self, other):  # Метод для сложения двух объектов класса Rub
        return Rub(self.rub + other.rub, self.kop + other.kop)  # Возвращает новый объект Rub, который является суммой двух других
class Goods(object):
    """ Класс описания товара: название и цена"""
    def __init__(self, name='', rub=0, kop=0):  # Инициализация объекта класса Goods
        self.name = name  # Установка названия товара
        self.price = Rub(rub, kop)  # Установка цены товара
