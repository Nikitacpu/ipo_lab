class WaterResource:  # Определение класса WaterResource
    """
    Класс WaterResource описывает водные ресурсы.
    """  # Документация класса
    def __init__(self, name, volume, location, quality, swimming_spots, preservation_status, dams):  # Конструктор класса
        self.name = name  # Инициализация атрибута name
        self.volume = volume  # Инициализация атрибута volume
        self.location = location  # Инициализация атрибута location
        self.quality = quality  # Инициализация атрибута quality
        self.swimming_spots = swimming_spots  # Инициализация атрибута swimming_spots
        self.preservation_status = preservation_status  # Инициализация атрибута preservation_status
        self.dams = dams  # Инициализация атрибута dams

    @property
    def name(self):  # Геттер для атрибута name
        return self._name

    @name.setter
    def name(self, value):  # Сеттер для атрибута name
        self._name = value

    # Аналогично добавьте сеттеры для остальных атрибутов

    def __del__(self):  # Деструктор класса
        print(f"Деструктор класса WaterResource вызван для {self.name}")  # Вывод сообщения при вызове деструктора

# Выводим документацию класса
print(WaterResource.__doc__)  # Вывод документации класса

# Создаем и инициализируем десять экземпляров класса
water_resources = []  # Создание пустого списка для хранения объектов класса WaterResource
for i in range(10):  # Цикл для создания 10 объектов
    wr = WaterResource(None, None, None, None, None, None, None)  # Создание нового объекта класса WaterResource с пустыми значениями атрибутов
    wr.name = input("Введите название водного ресурса: ")  # Ввод значения атрибута name с клавиатуры
    wr.volume = int(input("Введите объем водного ресурса: "))  # Ввод значения атрибута volume с клавиатуры
    wr.location = input("Введите местоположение водного ресурса: ")  # Ввод значения атрибута location с клавиатуры
    wr.quality = input("Введите качество воды: ")  # Ввод значения атрибута quality с клавиатуры
    wr.swimming_spots = input("Есть ли места для купания? (да/нет): ") == "да"  # Ввод значения атрибута swimming_spots с клавиатуры
    wr.preservation_status = input("Введите статус сохранности ресурса: ")  # Ввод значения атрибута preservation_status с клавиатуры
    wr.dams = input("Есть ли плотины? (да/нет): ") == "да"  # Ввод значения атрибута dams с клавиатуры
    water_resources.append(wr)  # Добавление нового объекта в список water_resources
