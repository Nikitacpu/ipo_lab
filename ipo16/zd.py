class Pet:  # Определение класса Pet
    def __init__(self, name, age, breed, color, weight, height):  # Конструктор класса
        self._name = name  # Инициализация имени
        self._age = age  # Инициализация возраста
        self._breed = breed  # Инициализация породы
        self._color = color  # Инициализация цвета
        self._weight = weight  # Инициализация веса
        self._height = height  # Инициализация роста
    @property
    def name(self):  # Геттер для имени
        return self._name  # Возвращает имя
    @name.setter
    def name(self, value):  # Сеттер для имени
        if not isinstance(value, str):  # Проверка типа
            raise TypeError("Имя должно быть строкой")  # Вызов ошибки, если тип неверный
        self._name = value  # Присваивание нового значения имени
    @property
    def age(self):  # Геттер для возраста
        return self._age  # Возвращает возраст
    @age.setter
    def age(self, value):  # Сеттер для возраста
        if not isinstance(value, int):  # Проверка типа
            raise TypeError("Возраст должен быть целым числом")  # Вызов ошибки, если тип неверный
        self._age = value  # Присваивание нового значения возрасту
    @property
    def breed(self):  # Геттер для породы
        return self._breed  # Возвращает породу
    @breed.setter
    def breed(self, value):  # Сеттер для породы
        if not isinstance(value, str):  # Проверка типа
            raise TypeError("Порода должна быть строкой")  # Вызов ошибки, если тип неверный
        self._breed = value  # Присваивание нового значения породе
    @property
    def color(self):  # Геттер для цвета
        return self._color  # Возвращает цвет
    @color.setter
    def color(self, value):  # Сеттер для цвета
        if not isinstance(value, str):  # Проверка типа
            raise TypeError("Цвет должен быть строкой")  # Вызов ошибки, если тип неверный
        self._color = value  # Присваивание нового значения цвету
    @property
    def weight(self):  # Геттер для веса
        return self._weight  # Возвращает вес
    @weight.setter
    def weight(self, value):  # Сеттер для веса
        if not isinstance(value, float):  # Проверка типа
            raise TypeError("Вес должен быть числом с плавающей точкой")  # Вызов ошибки, если тип неверный
        self._weight = value  # Присваивание нового значения весу
    @property
    def height(self):  # Геттер для роста
        return self._height  # Возвращает рост
    @height.setter
    def height(self, value):  # Сеттер для роста
        if not isinstance(value, float):  # Проверка типа
            raise TypeError("Рост должен быть числом с плавающей точкой")  # Вызов ошибки, если тип неверный
        self._height = value  # Присваивание нового значения росту
pet = Pet("Шарик", 3, "Немецкая овчарка", "Коричневый", 15.0, 0.5)
print(pet.name)  # Шарик
print('Вес:',pet.weight)  # Вывод 15.0
pet.weight = 16.0  # Изменение веса
print("Изменение веса: ",pet.weight)  #Вывод 16.0
pet.weight = "небольшой"  # Вызовет ошибку TypeError
