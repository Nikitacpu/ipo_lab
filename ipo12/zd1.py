# Класс STUDENT
class STUDENT:
    # Конструктор класса
    def __init__(self, surname, group_num, marks):
        self.surname = surname  # Фамилия студента
        self.group_num = group_num  # Номер группы
        self.marks = marks  # Оценки студента
# Список студентов
students_list = []
for i in range(10):  # Ввод дынных  о 10 студентах с помощью цикла For
    surname = input("Введите фамилию студента: ")  # Ввод фамилии студента
    group_num = input("Введите номер группы: ")  # Ввод номера группы
    marks = list(map(int, input("Введите  5 оценок студента (через пробел): ").split()))  # Ввод оценок
    students_list.append(STUDENT(surname, group_num, marks))  # Добавление студента в список
# Проверка студентов на наличие неудовлетворительных оценок
badstudents = [student for student in students_list if any(mark <= 2 for mark in student.marks)]
if badstudents:
    for student in badstudents:
        print(f"Студент {student.surname} из группы {student.group_num} имеет неудовлетворительные оценки.")  # Вывод информации о студенте
else:
    print("Студентов с неудовлетворительными оценками нет.")  # Сообщение, если таких студентов нет
